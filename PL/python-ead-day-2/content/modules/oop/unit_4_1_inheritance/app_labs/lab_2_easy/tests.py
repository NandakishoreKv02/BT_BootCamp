import unittest
from starter_code import Staff, MedicalStaff

class TestLab2(unittest.TestCase):
    def test_default_access(self):
        s = Staff("Jim", "101")
        self.assertEqual(s.access_records(), "Access Denied")

    def test_overridden_access(self):
        m = MedicalStaff("Dr. A", "202", "L1")
        self.assertEqual(m.access_records(), "Access Granted for Dr. A")

    def test_polymorphism(self):
        # Verify both have the method but behave differently
        s = Staff("S", "1")
        m = MedicalStaff("M", "2", "L")
        self.assertTrue(hasattr(s, 'access_records'))
        self.assertTrue(hasattr(m, 'access_records'))
        self.assertNotEqual(s.access_records(), m.access_records())

if __name__ == '__main__':
    unittest.main()
