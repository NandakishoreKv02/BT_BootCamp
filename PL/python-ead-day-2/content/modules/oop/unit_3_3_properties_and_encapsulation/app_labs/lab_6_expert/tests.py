"""Lab 6: Tests"""
import unittest
from starter_code import CriticalCareUnit, Patient, CapacityError

class TestCCU(unittest.TestCase):
    def setUp(self):
        self.ccu = CriticalCareUnit("Main CCU", 3)
        self.p1 = Patient("P1", "Alice")
        self.p2 = Patient("P2", "Bob")
        self.p3 = Patient("P3", "Charlie")
        self.p4 = Patient("P4", "David")
        
    def test_admit_discharge(self):
        self.ccu.admit_patient(self.p1)
        self.assertIn("P1", self.ccu.patient_ids)
        
        self.ccu.discharge_patient("P1")
        self.assertNotIn("P1", self.ccu.patient_ids)
        self.assertTrue(any("DISCHARGE: P1" in log for log in self.ccu.audit_log))
        
    def test_capacity_limits(self):
        self.ccu.admit_patient(self.p1)
        self.ccu.admit_patient(self.p2)
        self.ccu.admit_patient(self.p3)
        
        # Unit is full
        self.assertTrue(self.ccu.is_full)
        
        # Should fail
        with self.assertRaises(CapacityError):
            self.ccu.admit_patient(self.p4)
            
    def test_set_capacity_validation(self):
        self.ccu.admit_patient(self.p1)
        self.ccu.admit_patient(self.p2) # 2 patients
        
        # Try reducing to 1 (should fail)
        with self.assertRaises(ValueError):
            self.ccu.max_capacity = 1
            
        # Increasing should work and log
        before_log_len = len(self.ccu.audit_log)
        self.ccu.max_capacity = 5
        self.assertEqual(self.ccu.max_capacity, 5)
        self.assertGreater(len(self.ccu.audit_log), before_log_len)
        
    def test_occupancy_rate(self):
        self.assertEqual(self.ccu.occupancy_rate, 0.0)
        self.ccu.admit_patient(self.p1)
        # 1/3 = 33.33%
        self.assertAlmostEqual(self.ccu.occupancy_rate, 33.33, places=1)
        
    def test_audit_log_security(self):
        # Ensure returned log is a copy
        logs = self.ccu.audit_log
        logs.append("FAKE LOG")
        self.assertNotIn("FAKE LOG", self.ccu.audit_log)

if __name__ == "__main__":
    unittest.main()
