import unittest
from starter_code import get_patient, PatientNotFound

class TestLab1(unittest.TestCase):
    def test_found(self):
        db = {"A": "Alice"}
        self.assertEqual(get_patient(db, "A"), "Alice")

    def test_not_found(self):
        db = {}
        with self.assertRaises(PatientNotFound) as cm:
            get_patient(db, "B")
        self.assertIn("ID B missing", str(cm.exception))

if __name__ == "__main__":
    unittest.main()
