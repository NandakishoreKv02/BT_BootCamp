import unittest
import starter_code

class TestRegistryIndependence(unittest.TestCase):
    def test_list_independence(self):
        d1 = starter_code.Physician("1", "Dr. A")
        d2 = starter_code.Physician("2", "Dr. B")
        
        d1.assign_patient("John")
        
        self.assertIn("John", d1.assigned_patients)
        self.assertEqual(len(d2.assigned_patients), 0, "Wait! Lists are shared. Did you use a class level list?")

if __name__ == "__main__":
    unittest.main()
