import unittest
from starter_code import Staff, MedicalStaff

class TestLab1(unittest.TestCase):
    def test_staff_init(self):
        s = Staff("John", "001")
        self.assertEqual(s.name, "John")
        self.assertEqual(s.employee_id, "001")
        
    def test_medical_staff_inheritance(self):
        m = MedicalStaff("Jane", "002", "LIC-123")
        self.assertTrue(isinstance(m, Staff))
        self.assertEqual(m.name, "Jane")
        self.assertEqual(m.license_number, "LIC-123")
        
    def test_clock_in_inheritance(self):
        m = MedicalStaff("Jane", "002", "LIC-123")
        self.assertEqual(m.clock_in(), "Staff 002 clocked in")

if __name__ == '__main__':
    unittest.main()
