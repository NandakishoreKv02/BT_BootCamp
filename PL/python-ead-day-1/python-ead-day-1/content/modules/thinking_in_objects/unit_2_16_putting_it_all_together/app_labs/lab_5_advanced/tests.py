import unittest
from starter_code import Phase1Safety, Phase2Efficacy, TrialPhase

class TestClinicalTrial(unittest.TestCase):
    def test_inheritance(self):
        p1 = Phase1Safety("P1")
        self.assertTrue(isinstance(p1, TrialPhase))
        
    def test_logic_flow(self):
        p1 = Phase1Safety("P1")
        p1.enroll(15)
        self.assertIn("Passed", p1.evaluate())
        
        p2 = Phase2Efficacy("P2")
        p2.enroll(10) # Too low
        self.assertIn("Failed", p2.evaluate())

if __name__ == "__main__":
    unittest.main()
