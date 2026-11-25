
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Permission: read Google Docs only
SCOPES = [
    "https://www.googleapis.com/auth/documents.readonly"
]

# Your boss's approved French lesson document
DOCUMENT_ID = "1WBZZN2smA0_FpNrpWiQa7qXtwSXM971sqkg8UESDf_s"

CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.pickle"


def authenticate_google():
    credentials = None

    # Reuse an existing valid token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            credentials = pickle.load(token)

    # Refresh or request authorization if necessary
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    if not credentials or not credentials.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE,
            SCOPES
        )
        credentials = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(credentials, token)

    return credentials


def extract_text(elements):
    """Extract text from paragraphs and tables."""
    text = ""

    for element in elements:
        if "paragraph" in element:
            for item in element["paragraph"].get("elements", []):
                text += item.get("textRun", {}).get("content", "")

        elif "table" in element:
            for row in element["table"].get("tableRows", []):
                for cell in row.get("tableCells", []):
                    text += extract_text(cell.get("content", []))

    return text


def main():
    try:
        print("Connecting to Google Docs...")

        credentials = authenticate_google()

        service = build(
            "docs",
            "v1",
            credentials=credentials
        )

        print("Reading the French lesson document...")

        document = service.documents().get(
            documentId=DOCUMENT_ID
        ).execute()

        title = document.get("title", "Untitled document")
        content = extract_text(
            document.get("body", {}).get("content", [])
        )

        print("\n" + "=" * 50)
        print("DOCUMENT TITLE:", title)
        print("=" * 50)
        print(content)
        print("=" * 50)

        print("\nSUCCESS: Document retrieved in read-only mode.")

    except Exception as error:
        print("\nERROR:", error)
        print("\nPlease share the error message so we can troubleshoot.")


if __name__ == "__main__":
    main()
