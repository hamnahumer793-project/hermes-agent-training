# Hermes Desktop Testing

## Overview

This repository contains my testing experience with Hermes Desktop. I wanted to see how it works in practice, how well it follows instructions, and whether it can handle tasks such as creating files, editing content, and completing multiple steps on its own.

## Testing Environment

- **Agent:** Hermes Desktop
- **Operating System:** Windows Desktop

## Tests Performed

### Test 1: Basic Communication

First, I sent a simple message to Hermes to check whether it was working properly and responding to my instructions.

**Result:** Hermes responded without any issues.

**Status:** Passed

### Test 2: Folder and File Creation

I asked Hermes to create a folder named `Kindergarten` and a text file called `lesson1.txt` inside that folder.

**Result:** Both the folder and the file were created successfully.

**Status:** Passed

### Test 3: Kindergarten Counting Lesson

Next, I asked Hermes to add a simple counting lesson to `lesson1.txt` for Kindergarten children. I wanted it to include numbers from 1 to 5, their number names, and easy examples that children could understand.

**Result:** Hermes added the lesson and saved it to the file as requested.

**Status:** Passed

### Test 4: Multi-Step Task and File Review

For this test, I gave Hermes several instructions at once. I asked it to check the counting lesson, make sure numbers 1 to 5 and their number names were included, review the examples and wording, and leave the original file unchanged. I also asked it to create a separate file named `lesson1_review.txt` containing the review.

### Test 5: Command Execution

I asked Hermes to execute some basic terminal commands to check whether it could interact with the system and return actual results. The commands included checking the current date and time, displaying the working directory, listing files and folders, and checking the installed Python version.

**Commands Tested:**
- `date`
- `pwd`
- `ls -la`
- `python --version`
- `python3 --version`

**Result:** Hermes executed all the commands successfully and displayed their outputs. It also identified the existing files in the Kindergarten folder and confirmed that Python 3.14.9 was installed.

### Test 6: Web Search and Web Extraction

I tested Hermes' web search capability by asking it to find the official Hermes Agent documentation. It used the `web_search` tool to find relevant results and `web_extract` to retrieve information from the documentation page.

**Tools Used:**
- `web_search`
- `web_extract`

**Result:** Hermes found the official Nous Research documentation and returned its page title, original link, and a short summary covering installation, configuration, tools, memory, skills, and integrations.

**Documentation:** https://hermes-agent.nousresearch.com/docs

**Status:** Passed
**Result:** Hermes completed the review, reported that no issues were found, and returned a final PASS result.

**Status:** Passed (Hermes-reported; manual verification pending)

## Conclusion

Overall, my experience with Hermes Desktop was good. It was able to respond to messages, create
