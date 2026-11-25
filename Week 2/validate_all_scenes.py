
import json
from pathlib import Path
from jsonschema import validate, ValidationError


def main():
    data_file = Path("all_nine_scenes.json")
    schema_file = Path("all_scenes_schema.json")

    # Load the extracted lesson JSON
    with data_file.open("r", encoding="utf-8") as file:
        lesson = json.load(file)

    # Load the JSON Schema
    with schema_file.open("r", encoding="utf-8") as file:
        schema = json.load(file)

    # Validate the complete lesson
    validate(instance=lesson, schema=schema)

    print("JSON Schema validation PASSED!")

    # Check the number and order of scenes
    scenes = lesson["scenes"]

    assert len(scenes) == 9, "Expected exactly 9 scenes."

    for expected_number, scene in enumerate(scenes, start=1):
        assert scene["scene_number"] == expected_number, (
            f"Scene order error at position {expected_number}."
        )

    print("Scene count check PASSED!")
    print("Scene order check PASSED!")

    # Check original expected durations
    expected_durations = [8, 8, 8, 10, 10, 10, 10, 10, 8]

    actual_durations = [
        scene["duration_seconds"] for scene in scenes
    ]

    assert actual_durations == expected_durations, (
        "Scene durations do not match the source document."
    )

    print("Duration check PASSED!")

    print("\nAll validation checks passed successfully!")


if __name__ == "__main__":
    main()
