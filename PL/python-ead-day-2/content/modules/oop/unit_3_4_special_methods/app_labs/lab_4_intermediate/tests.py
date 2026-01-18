"""Lab 4: Tests - Diagnosis Codes"""
import unittest
from starter_code import DiagnosisCode


class TestDiagnosisCode(unittest.TestCase):
    def setUp(self):
        self.d1 = DiagnosisCode("J06.9", "URI")
        self.d2 = DiagnosisCode("J06.9", "Upper Respiratory")
        self.d3 = DiagnosisCode("K21.0", "GERD")
    
    def test_eq_same_code(self):
        self.assertEqual(self.d1, self.d2)
    
    def test_eq_different_code(self):
        self.assertNotEqual(self.d1, self.d3)
    
    def test_hash_equal_objects(self):
        self.assertEqual(hash(self.d1), hash(self.d2))
    
    def test_set_deduplication(self):
        codes = {self.d1, self.d2}
        self.assertEqual(len(codes), 1)
    
    def test_dict_key(self):
        code_counts = {self.d1: 5}
        self.assertEqual(code_counts[self.d2], 5)


if __name__ == "__main__":
    unittest.main()
