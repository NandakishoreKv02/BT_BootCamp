import unittest
import starter_code

class TestHospitalRefactor(unittest.TestCase):
    def test_structures(self):
        p = starter_code.create_patient(1, "TestP")
        d = starter_code.create_doctor(10, "TestD")
        
        # Check basic keys
        self.assertIn('name', p)
        self.assertIn('status', p)
        self.assertIn('name', d)
        # We expect doctors to track patients now (better design)
        self.assertIn('assigned_patients', d)

    def test_assignment(self):
        p = starter_code.create_patient(1, "TestP")
        d = starter_code.create_doctor(10, "TestD")
        
        starter_code.assign_doctor(d, p)
        
        # Check bidirectional link if implemented, or at least Doctor -> Patient
        # (Assuming the student follows the better design of list on doc)
        self.assertIn(p['id'], d['assigned_patients'])
        # Or Patient -> Doctor
        self.assertEqual(p['doctor_id'], d['id'])

    def test_discharge(self):
        p = starter_code.create_patient(1, "TestP")
        starter_code.discharge_patient(p)
        self.assertEqual(p['status'], "Discharged")

if __name__ == "__main__":
    unittest.main()
