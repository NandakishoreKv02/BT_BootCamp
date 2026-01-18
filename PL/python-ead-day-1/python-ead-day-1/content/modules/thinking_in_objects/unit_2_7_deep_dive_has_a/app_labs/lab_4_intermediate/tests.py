import unittest
import starter_code

class TestLifecycleAudit(unittest.TestCase):
    def test_composition_vs_aggregation(self):
        dr = starter_code.Doctor("Wilson")
        f1 = starter_code.PatientFile("Alice")
        f2 = starter_code.PatientFile("Bob")
        f1.assign_doctor(dr)
        f2.assign_doctor(dr)
        
        # History must be unique to file
        self.assertNotEqual(id(f1.history), id(f2.history))
        # Doctor must be shared
        self.assertIs(f1.reviewer, f2.reviewer)

if __name__ == "__main__":
    unittest.main()
