import unittest
import starter_code

class TestRobotEncapsulation(unittest.TestCase):
    def test_private_methods(self):
        bot = starter_code.SurgicalRobot()
        # Public method should exist
        self.assertTrue(hasattr(bot, "deploy"))
        # Private check should be mangled/hidden
        with self.assertRaises(AttributeError):
            bot.__check_power()

    def test_successful_deployment(self):
        bot = starter_code.SurgicalRobot()
        bot.deploy(30)
        self.assertEqual(bot.arm_extension, 30)

if __name__ == "__main__":
    unittest.main()
