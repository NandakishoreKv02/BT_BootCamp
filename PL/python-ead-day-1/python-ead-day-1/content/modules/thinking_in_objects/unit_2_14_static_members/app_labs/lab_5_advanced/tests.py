import unittest
import starter_code

class TestStaticValidation(unittest.TestCase):
    def test_validation_logic_positive(self):
        self.assertTrue(starter_code.SurgicalRobot.is_safe(220))
        
    def test_validation_logic_negative(self):
        self.assertFalse(starter_code.SurgicalRobot.is_safe(100))
        self.assertFalse(starter_code.SurgicalRobot.is_safe(250))
        
    def test_constructor_enforcement(self):
        r = starter_code.SurgicalRobot(300)
        self.assertEqual(r.voltage, 0)

if __name__ == "__main__":
    unittest.main()
