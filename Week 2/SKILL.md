---
name: french-letter-a-extraction
description: Use when extracting CP1 French Letter A scenes.
version: 1.0.0
platforms: [windows]
metadata:
  hermes:
    tags: [python, google-docs, json, extraction, validation]
    category: productivity
    requires_toolsets: [terminal]
---

# French Letter A Extraction

## Purpose

Automate the extraction and validation of the nine scenes in the CP1 French Letter A lesson.

## Project Location

Use this Windows project directory:

`C:\Users\Missj\OneDrive\Documents\french reader`

Use the project's Python 3.10.11 virtual environment:

`venv\Scripts\python.exe`

## Procedure

When the user requests the complete extraction workflow:

1. Use the terminal and navigate to the project directory.
2. Use the project's virtual-environment interpreter, not a global Python. Run each workflow command separately and stop immediately if a command fails:
   - `venv\Scripts\python.exe extract_all_scenes.py`
   - Confirm `all_nine_scenes.json` exists before continuing.
   - `venv\Scripts\python.exe validate_all_scenes.py`
   - `venv\Scripts\python.exe -m unittest test_all_scenes.py -v`
3. Report each command's result separately, including warnings and any failed step. Do not continue to validation or tests after an earlier failure.

When asked to identify an installed dependency version or investigate a warning, inspect package metadata read-only with `venv\Scripts\python.exe -m pip show <package>`. Report the displayed package name, version, and requirements; do not infer a package version from a warning's module path.

## Expected Results

- Exactly nine scenes are extracted.
- Scene order is preserved.
- Original French narration is retained.
- Visual descriptions are retained.
- Scene durations are retained.
- Separate quiz and game sections are excluded.
- JSON Schema validation passes.
- Both automated tests pass.

## Safety Rules

- Never display, copy, upload, or modify `credentials.json` or `token.pickle`.
- Do not modify the original Google Doc, Python scripts, or JSON schema during extraction.
- Do not silently change original French narration or visual descriptions.
- Do not upload project files or publish to GitHub unless the user explicitly asks.
- If Google authentication requires user interaction, ask the user to complete it.

## Final Report

After execution, report:

- Whether extraction succeeded.
- Number of scenes extracted.
- Whether validation passed.
- Number of automated tests passed.
- Any errors or warnings.
