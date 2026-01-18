import unittest
import starter_code

class TestStandards(unittest.TestCase):
    def test_pep8_compliance(self):
        # Class check
        self.assertTrue(hasattr(starter_code, "SurgicalRobot"), "Class should be named SurgicalRobot")
        
        # Method check
        bot = starter_code.SurgicalRobot("R-9")
        self.assertTrue(hasattr(bot, "perform_calibration"), "Method should be named perform_calibration")
        self.assertTrue(hasattr(bot, "robot_id"), "Attribute should be named robot_id")

if __name__ == "__main__":
    unittest.main()
