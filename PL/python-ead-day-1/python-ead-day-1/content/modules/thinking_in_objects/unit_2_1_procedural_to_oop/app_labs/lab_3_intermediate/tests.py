import unittest
import starter_code

class TestTriageSystem(unittest.TestCase):
    def test_create(self):
        r = starter_code.create_triage_record("Test", 30, 80, "Flu")
        self.assertEqual(r['priority'], "Normal")

    def test_severity_logic(self):
        r_high = starter_code.create_triage_record("P1", 50, 130, "Flu")
        starter_code.assess_severity(r_high)
        self.assertEqual(r_high['priority'], "HIGH")

        r_norm = starter_code.create_triage_record("P2", 20, 80, "Flu")
        starter_code.assess_severity(r_norm)
        self.assertEqual(r_norm['priority'], "Normal")

if __name__ == "__main__":
    unittest.main()
