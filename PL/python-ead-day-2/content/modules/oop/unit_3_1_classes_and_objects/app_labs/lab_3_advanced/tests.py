import unittest
from starter_code import Patient, HospitalRegistry

class TestHospitalSystem(unittest.TestCase):
    def test_class_variable(self):
        """Verify class variables are shared and updatable."""
        p1 = Patient("1", "A", 10)
        p2 = Patient("2", "B", 20)
        
        # Initial check
        self.assertEqual(p1.clinic_name, p2.clinic_name)
        
        # Global update
        Patient.clinic_name = "Updated Clinic"
        self.assertEqual(p1.clinic_name, "Updated Clinic")
        self.assertEqual(p2.clinic_name, "Updated Clinic")

    def test_registry_management(self):
        """Test adding and finding patients."""
        reg = HospitalRegistry()
        p = Patient("PID-007", "James Bond", 45)
        reg.register_patient(p)
        
        self.assertEqual(len(reg.patients), 1)
        
        found = reg.get_patient("PID-007")
        self.assertEqual(found.name, "James Bond")
        
        not_found = reg.get_patient("MISSING")
        self.assertIsNone(not_found)

if __name__ == "__main__":
    unittest.main()
