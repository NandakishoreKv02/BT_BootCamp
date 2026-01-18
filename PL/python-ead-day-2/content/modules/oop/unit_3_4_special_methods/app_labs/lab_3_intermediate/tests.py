"""Lab 3: Tests - Priority Queue"""
import unittest
from starter_code import TriagePatient


class TestTriagePatient(unittest.TestCase):
    def setUp(self):
        self.p1 = TriagePatient("P001", "Alice", 3)
        self.p2 = TriagePatient("P002", "Bob", 1)
        self.p3 = TriagePatient("P003", "Carol", 2)
    
    def test_eq_same_id(self):
        p1_copy = TriagePatient("P001", "Alice Copy", 5)
        self.assertEqual(self.p1, p1_copy)
    
    def test_eq_different_id(self):
        self.assertNotEqual(self.p1, self.p2)
    
    def test_lt_by_urgency(self):
        self.assertTrue(self.p2 < self.p1)  # 1 < 3
    
    def test_sorting(self):
        patients = [self.p1, self.p2, self.p3]
        sorted_p = sorted(patients)
        self.assertEqual(sorted_p[0].urgency, 1)
        self.assertEqual(sorted_p[1].urgency, 2)
        self.assertEqual(sorted_p[2].urgency, 3)
    
    def test_total_ordering(self):
        self.assertTrue(self.p2 <= self.p3)
        self.assertTrue(self.p1 > self.p2)
        self.assertTrue(self.p1 >= self.p3)


if __name__ == "__main__":
    unittest.main()
