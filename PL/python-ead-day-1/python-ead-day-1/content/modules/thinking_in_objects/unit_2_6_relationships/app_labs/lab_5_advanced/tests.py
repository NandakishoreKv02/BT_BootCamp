import unittest
from io import StringIO
import sys
import starter_code

class TestRobotInteraction(unittest.TestCase):
    def test_robot_structure(self):
        robot = starter_code.SurgicalRobot()
        self.assertTrue(hasattr(robot, "camera"))
        self.assertTrue(hasattr(robot, "arm"))

    def test_operation_dependency(self):
        robot = starter_code.SurgicalRobot()
        power = starter_code.PowerSource("Grid")
        organ = starter_code.Organ("Kidney")
        
        captured_output = StringIO()
        sys.stdout = captured_output
        robot.operate(power, organ)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Kidney", output)
        self.assertIn("Grid", output)

if __name__ == "__main__":
    unittest.main()
