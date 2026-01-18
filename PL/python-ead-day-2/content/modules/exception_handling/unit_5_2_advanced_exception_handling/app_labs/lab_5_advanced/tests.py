import unittest
import os
from starter_code import process_patient_file

class TestLab5(unittest.TestCase):
    def setUp(self):
        with open("patients.txt", "w") as f:
            f.write("20\n30\nbad\n40")

    def tearDown(self):
        if os.path.exists("patients.txt"):
            os.remove("patients.txt")

    def test_processing(self):
        # Should contain 20, 30, 40. "bad" is skipped.
        res = process_patient_file("patients.txt")
        self.assertEqual(res, [20, 30, 40])

    def test_missing_file(self):
        res = process_patient_file("missing.txt")
        self.assertEqual(res, [])

if __name__ == "__main__":
    unittest.main()
