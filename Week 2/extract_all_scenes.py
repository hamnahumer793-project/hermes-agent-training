
import re
import json
from pathlib import Path

from read_french_doc import (
    authenticate_google,
    DOCUMENT_ID
)
from googleapiclient.discovery import build

def extract_text(elements):
    """Extract text from Google Docs paragraphs and tables."""
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

def extract_scenes(document_text):
    """Extract only the nine lesson scenes, excluding quizzes and games."""

    pattern = re.compile(
        r"⏱️\s*SCÈNE\s+(\d+)\s*[—–-]\s*(.*?)\n"
        r"(.*?)(?=\n⏱️\s*SCÈNE\s+\d+\s*[—–-]|\n_+|\nQUIZ|\Z)",
        re.DOTALL
    )

    scenes = []

    for match in pattern.finditer(document_text):
        scene_number = int(match.group(1))
        title = match.group(2).strip()
        content = match.group(3).strip()

        duration_match = re.search(
            r"(\d+)\s*secondes?",
            content
        )

        narration_match = re.search(
            r"Voix off(?:\s*\([^)]*\))?\s*:\s*«\s*(.*?)\s*»",
            content,
            re.DOTALL
        )

        if not duration_match or not narration_match:
            raise ValueError(
                f"Could not extract duration or narration "
                f"for Scene {scene_number}"
            )

        duration = int(duration_match.group(1))
        narration = narration_match.group(1).strip()

        visual_prompt = content[:duration_match.start()].strip()

        scenes.append({
            "scene_number": scene_number,
            "title": title,
            "duration_seconds": duration,
            "visual_prompt": visual_prompt,
            "narration": narration
        })

    if len(scenes) != 9:
        raise ValueError(
            f"Expected 9 scenes, but extracted {len(scenes)}"
        )

    for expected_number, scene in enumerate(scenes, start=1):
        if scene["scene_number"] != expected_number:
            raise ValueError("Scene order is incorrect.")

    return scenes

def main():
    print("Connecting to Google Docs...")

    credentials = authenticate_google()

    service = build(
        "docs",
        "v1",
        credentials=credentials
    )

    print("Retrieving the French lesson...")

    document = service.documents().get(
        documentId=DOCUMENT_ID
    ).execute()

    document_text = extract_text(
        document.get("body", {}).get("content", [])
    )

    scenes = extract_scenes(document_text)

    lesson = {
        "grade": "CP1",
        "language": "French",
        "learning_objective": (
            "Introduce the letter A and help children "
            "recognize its name and sound."
        ),
        "scenes": scenes
    }

    output_file = Path("all_nine_scenes.json")

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(
            lesson,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("\nSUCCESS!")
    print("Extracted all 9 scenes.")
    print("Quizzes and games were excluded.")
    print("Saved to:", output_file)

if __name__ == "__main__":
    main()