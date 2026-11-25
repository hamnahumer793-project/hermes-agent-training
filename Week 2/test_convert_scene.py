
import unittest
from copy import deepcopy

from convert_scene import lesson, validate_lesson


class TestLessonValidation(unittest.TestCase):

    # Test 1: Valid lesson data should pass
    def test_valid_lesson(self):
        test_data = deepcopy(lesson)

        result = validate_lesson(test_data)

        self.assertTrue(result["has_grade"])
        self.assertTrue(result["has_language"])
        self.assertTrue(result["has_narration"])

    # Test 2: Missing narration should fail
    def test_missing_narration(self):
        test_data = deepcopy(lesson)

        test_data["narration"] = ""

        with self.assertRaises(ValueError):
            validate_lesson(test_data)


if __name__ == "__main__":
    unittest.main()
