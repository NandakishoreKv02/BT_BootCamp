import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestHospitalHierarchy(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.hosp = {}

    def test_registration(self):
        starter_code.register_doctor(self.hosp, "ER", "A", "Trauma")
        starter_code.register_doctor(self.hosp, "ER", "A", "Trauma") # Duplicate
        self.assertEqual(len(self.hosp["ER"]["A"]), 1)

    def test_doctors_list(self):
        starter_code.register_doctor(self.hosp, "ICU", "A", "X")
        starter_code.register_doctor(self.hosp, "ICU", "B", "Y")
        doctors = starter_code.get_dept_doctors(self.hosp, "ICU")
        self.assertIn("A", doctors)
        self.assertIn("B", doctors)
        self.assertEqual(len(doctors), 2)

    def test_specialty_aggregation(self):
        starter_code.register_doctor(self.hosp, "A", "Doc1", "S1")
        starter_code.register_doctor(self.hosp, "A", "Doc2", "S1")
        starter_code.register_doctor(self.hosp, "A", "Doc2", "S2")
        
        specs = starter_code.get_unique_specialties_for_dept(self.hosp, "A")
        self.assertEqual(specs, {"S1", "S2"})

if __name__ == '__main__':
    unittest.main()
