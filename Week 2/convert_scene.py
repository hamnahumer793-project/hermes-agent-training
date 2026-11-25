
import json
from pathlib import Path
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Sample extracted from the CP1 French - Letter A document
lesson = {
    "grade": "CP1",
    "language": "French",
    "learning_objective": (
        "Introduce the letter A and help children recognize "
        "its name and sound."
    ),
    "duration_seconds": 8,

    "scenes": [
        {
            "scene_number": 1,
            "title": "Introduction"
        }
    ],

    "narration": (
        "Bienvenue les enfants ! Aujourd'hui, on apprend "
        "une lettre magique : la lettre A !"
    ),

    "visual_prompt": (
        "Animation 2D cartoon, style livre scolaire africain, "
        "classe africaine colorée et ensoleillée. "
        "La maîtresse en pagne wax entre avec un grand sourire. "
        "Le tableau noir s'illumine d'étincelles magiques. "
        "Les petits élèves Kofi et Adjoua sont assis, attentifs. "
        "Voix off enfantine française."
    )
}


def validate_lesson(data):

    required_fields = [
        "grade",
        "language",
        "learning_objective",
        "duration_seconds",
        "scenes",
        "narration",
        "visual_prompt"
    ]

    # Check that all required fields exist
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    # Check that text fields are not empty
    checks = {
        "has_grade": bool(data["grade"].strip()),
        "has_language": bool(data["language"].strip()),
        "has_learning_objective": bool(
            data["learning_objective"].strip()
        ),
        "has_narration": bool(data["narration"].strip()),
        "has_visual_prompt": bool(data["visual_prompt"].strip()),
        "duration_is_positive": (
            isinstance(data["duration_seconds"], int)
            and not isinstance(data["duration_seconds"], bool)
            and data["duration_seconds"] > 0
        ),
        "has_scenes": (
            isinstance(data["scenes"], list)
            and len(data["scenes"]) > 0
        )
    }

    # Check the scene information
    if checks["has_scenes"]:
        checks["scenes_are_valid"] = all(
            isinstance(scene, dict)
            and isinstance(scene.get("scene_number"), int)
            and isinstance(scene.get("title"), str)
            and bool(scene["title"].strip())
            for scene in data["scenes"]
        )
    else:
        checks["scenes_are_valid"] = False

    # Stop if any quality check fails
    failed_checks = [
        name for name, passed in checks.items()
        if not passed
    ]

    if failed_checks:
        raise ValueError(
            f"Quality checks failed: {failed_checks}"
        )

    print("All quality checks passed!")

    return checks


def validate_with_schema(data):

    schema_file = Path("scene_schema.json")

    with schema_file.open("r", encoding="utf-8") as file:
        schema = json.load(file)

    try:
        validate(instance=data, schema=schema)
        print("JSON Schema validation passed!")

    except ValidationError as error:
        print("JSON Schema validation failed!")
        print("Reason:", error.message)
        raise

def main():

    quality_checks = validate_lesson(lesson)

    # Add actual validation results
    lesson["quality_checks"] = quality_checks

    # Validate using the JSON Schema
    validate_with_schema(lesson)

    # Save the final JSON file
    output_file = Path("scene1.json")

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(
            lesson,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"JSON file created successfully: {output_file}")


if __name__ == "__main__":
    main()
