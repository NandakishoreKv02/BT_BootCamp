import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestTriageLevel(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_red_cases(self):
        self.assertEqual(starter_code.classify_triage(145), "RED")
        self.assertEqual(starter_code.classify_triage(35), "RED")

    def test_yellow_cases(self):
        self.assertEqual(starter_code.classify_triage(120), "YELLOW")
        self.assertEqual(starter_code.classify_triage(45), "YELLOW")

    def test_green_cases(self):
        self.assertEqual(starter_code.classify_triage(72), "GREEN")
        self.assertEqual(starter_code.classify_triage(90), "GREEN")

if __name__ == '__main__':
    unittest.main()
