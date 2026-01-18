import unittest
from starter_code import PatientFile, LoggerMixin, JSONMixin

class TestLab3(unittest.TestCase):
    def test_inheritance_chain(self):
        self.assertTrue(issubclass(PatientFile, LoggerMixin))
        self.assertTrue(issubclass(PatientFile, JSONMixin))

    def test_diagnosis_update(self):
        p = PatientFile("Test")
        p.update_diagnosis("Healthy")
        self.assertEqual(p.diagnosis, "Healthy")

    def test_json_conversion(self):
        p = PatientFile("Bob")
        js = p.to_json()
        self.assertIn('"name": "Bob"', js)

if __name__ == '__main__':
    unittest.main()
