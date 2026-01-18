import unittest
from dataclasses import FrozenInstanceError
from starter_code import PrescriptionRecord, ArchiveRecord

class TestLab4(unittest.TestCase):
    def test_default_factory(self):
        r1 = PrescriptionRecord("P-1")
        r2 = PrescriptionRecord("P-2")
        r1.medications.append("MedA")
        # Ensure list is NOT shared
        self.assertEqual(len(r2.medications), 0)

    def test_validation(self):
        with self.assertRaises(ValueError):
            PrescriptionRecord("BAD-ID")

    def test_frozen_state(self):
        arch = ArchiveRecord("2024", "Data")
        with self.assertRaises(FrozenInstanceError):
            arch.content = "New"

if __name__ == '__main__':
    unittest.main()
