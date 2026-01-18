import unittest
from io import StringIO
import sys
from starter_code import VitalMonitor, NurseStation

class TestLab3(unittest.TestCase):
    def test_attachment(self):
        m = VitalMonitor()
        n = NurseStation()
        m.attach(n)
        self.assertIn(n, m._observers)

    def test_detachment(self):
        m = VitalMonitor()
        n = NurseStation()
        m.attach(n)
        m.detach(n)
        self.assertNotIn(n, m._observers)

    def test_notification_called(self):
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        m = VitalMonitor()
        n = NurseStation()
        m.attach(n)
        m.check_heart_rate(150, "Test")
        
        sys.stdout = sys.__stdout__
        self.assertIn("Test", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
