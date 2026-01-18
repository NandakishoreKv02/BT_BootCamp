import unittest
import starter_code

class TestFactoryRegistry(unittest.TestCase):
    def test_registry_tracking(self):
        # Clear registry if possible
        starter_code.MedicalStaff.ALL_STAFF = []
        s = starter_code.MedicalStaff.spawn_from_name("Staff 1")
        p = starter_code.Physician.spawn_from_name("Dr. 1")
        
        self.assertEqual(len(starter_code.MedicalStaff.ALL_STAFF), 2)
        self.assertTrue(isinstance(starter_code.MedicalStaff.ALL_STAFF[1], starter_code.Physician))

if __name__ == "__main__":
    unittest.main()
