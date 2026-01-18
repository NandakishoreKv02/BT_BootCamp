import unittest
from starter_code import Patient, Doctor, Department, BillingSystem

class TestHospitalSim(unittest.TestCase):
    def test_treatment_flow(self):
        p = Patient("Test")
        d = Doctor("Dr. T", "Gen")
        
        d.treat(p, "Checkup", 100)
        
        self.assertEqual(p.get_balance(), 100)
        self.assertIn("Checkup", p.history)
        
    def test_department_assign(self):
        dept = Department("ER")
        doc = Doctor("Dr. E", "Emergency")
        dept.add_doctor(doc)
        
        assigned = dept.assign_doctor("Emergency")
        self.assertEqual(assigned.name, "Dr. E")

if __name__ == "__main__":
    unittest.main()
