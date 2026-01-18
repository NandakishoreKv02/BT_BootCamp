import unittest
from starter_code import PatientAssessor, AdultStrategy, PediatricStrategy

class TestLab4(unittest.TestCase):
    def test_adult_logic(self):
        assessor = PatientAssessor(AdultStrategy())
        self.assertEqual(assessor.get_risk_level(120), "CRITICAL")
        self.assertEqual(assessor.get_risk_level(70), "NORMAL")

    def test_pediatric_logic(self):
        assessor = PatientAssessor(PediatricStrategy())
        self.assertEqual(assessor.get_risk_level(120), "NORMAL")
        self.assertEqual(assessor.get_risk_level(160), "CRITICAL")

    def test_strategy_swap(self):
        assessor = PatientAssessor(AdultStrategy())
        # Adult at 120 is critical
        self.assertEqual(assessor.get_risk_level(120), "CRITICAL")
        
        assessor.set_strategy(PediatricStrategy())
        # Pediatric at 120 is NORMAL
        self.assertEqual(assessor.get_risk_level(120), "NORMAL")

if __name__ == '__main__':
    unittest.main()
