import unittest
import starter_code

class TestImmutableIdentity(unittest.TestCase):
    def test_mrn_read_only(self):
        rec = starter_code.ClinicalRecord("123", "John")
        self.assertEqual(rec.mrn, "123")
        with self.assertRaises(AttributeError):
            rec.mrn = "999"

    def test_name_mutable(self):
        rec = starter_code.ClinicalRecord("123", "John")
        rec.name = "John Smith"
        self.assertEqual(rec.name, "John Smith")

if __name__ == "__main__":
    unittest.main()
