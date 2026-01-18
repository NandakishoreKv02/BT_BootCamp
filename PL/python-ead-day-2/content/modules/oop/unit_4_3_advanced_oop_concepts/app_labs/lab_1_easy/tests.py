import unittest
from dataclasses import is_dataclass
from starter_code import VitalsRecord, PatientHeader

class TestLab1(unittest.TestCase):
    def test_vitals_record_is_dataclass(self):
        self.assertTrue(is_dataclass(VitalsRecord))

    def test_patient_header_is_dataclass(self):
        self.assertTrue(is_dataclass(PatientHeader))

    def test_vitals_equality(self):
        v1 = VitalsRecord(80, 99.0, "110/70")
        v2 = VitalsRecord(80, 99.0, "110/70")
        self.assertEqual(v1, v2)

    def test_repr_generation(self):
        v = VitalsRecord(80, 99.0, "110/70")
        self.assertIn("80", repr(v))
        self.assertIn("110/70", repr(v))

if __name__ == '__main__':
    unittest.main()
