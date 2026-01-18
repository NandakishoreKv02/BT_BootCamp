import unittest
from starter_code import Staff, MedicalStaff, Surgeon

class TestLab3(unittest.TestCase):
    def test_staff_pay(self):
        s = Staff("Basic")
        self.assertEqual(s.calculate_pay(), 50000)

    def test_medical_pay(self):
        m = MedicalStaff("Medi")
        self.assertEqual(m.calculate_pay(), 60000) # 50k + 10k

    def test_surgeon_pay(self):
        sg = Surgeon("Surg")
        self.assertEqual(sg.calculate_pay(), 90000) # 60k + 30k

if __name__ == '__main__':
    unittest.main()
