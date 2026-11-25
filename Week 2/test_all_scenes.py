
import json
import unittest
from copy import deepcopy
from pathlib import Path

from jsonschema import validate, ValidationError


class TestAllScenes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open("all_nine_scenes.json", "r", encoding="utf-8") as file:
            cls.lesson = json.load(file)

        with open("all_scenes_schema.json", "r", encoding="utf-8") as file:
            cls.schema = json.load(file)

    # Test 1: Complete valid lesson should pass
    def test_valid_lesson(self):
        validate(instance=self.lesson, schema=self.schema)

        self.assertEqual(len(self.lesson["scenes"]), 9)

        print("\nTest 1 PASSED: Valid nine-scene lesson accepted.")

    # Test 2: Missing narration should fail
    def test_missing_narration(self):
        invalid_lesson = deepcopy(self.lesson)

        del invalid_lesson["scenes"][0]["narration"]

        with self.assertRaises(ValidationError):
            validate(
                instance=invalid_lesson,
                schema=self.schema
            )

        print("\nTest 2 PASSED: Missing narration correctly rejected.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
