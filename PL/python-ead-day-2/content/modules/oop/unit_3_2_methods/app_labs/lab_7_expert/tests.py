import unittest
from starter_code import Patient

class TestAuditor(unittest.TestCase):
    def setUp(self):
        Patient.census = 0

    def test_full_workflow(self):
        p = Patient("Alice")
        self.assertEqual(Patient.census, 1)
        self.assertIn("Initialization performed", p.audit_logs)
        
        recovery = p.apply_treatment(5)
        self.assertEqual(recovery, 10)
        self.assertEqual(p.recovery_est, 10)
        self.assertIn("Treatment Applied performed", p.audit_logs)

    def test_factory_audit(self):
        recs = [{"name": "P1"}, {"name": "P2"}]
        patients = Patient.from_records(recs)
        self.assertEqual(len(patients), 2)
        self.assertEqual(Patient.census, 2)
        self.assertEqual(patients[0].name, "P1")
        self.assertIn("Initialization performed", patients[1].audit_logs)

if __name__ == "__main__":
    unittest.main()
