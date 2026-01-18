import unittest
import starter_code

class TestDepartmentHierarchy(unittest.TestCase):
    def test_urgency_logic(self):
        icu = starter_code.HospitalDepartment("ICU Ward", 3)
        ped = starter_code.HospitalDepartment("Pediatrics", 2)
        
        self.assertEqual(icu.urgency, "High")
        self.assertEqual(ped.urgency, "Normal")

    def test_hierarchy(self):
        dept = starter_code.HospitalDepartment("Main", 1)
        sub = starter_code.HospitalDepartment("Sub", 1)
        dept.add_subunit(sub) # Checking if method exists
        self.assertIn(sub, dept.sub_units)

if __name__ == "__main__":
    unittest.main()
