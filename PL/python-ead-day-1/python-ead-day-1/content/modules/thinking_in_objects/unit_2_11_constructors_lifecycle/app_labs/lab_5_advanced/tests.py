import unittest
import starter_code

class TestSurgicalInitialization(unittest.TestCase):
    def test_mixed_params_and_auto_logic(self):
        case = starter_code.SurgicalCase("John", "Appendix")
        self.assertEqual(case.surgeon, "TBD")
        self.assertEqual(case.complexity_score, 8)
        
    def test_overrides(self):
        case = starter_code.SurgicalCase("Jane", "Heart", surgeon="Smith", room=9)
        self.assertEqual(case.surgeon, "Smith")
        self.assertEqual(case.room, 9)

if __name__ == "__main__":
    unittest.main()
