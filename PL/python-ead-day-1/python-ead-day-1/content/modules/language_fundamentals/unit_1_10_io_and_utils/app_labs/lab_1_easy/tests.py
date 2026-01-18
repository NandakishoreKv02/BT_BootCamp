import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestTriageIntake(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_not_yet_eligible(self):
        res = starter_code.get_screening_status("John", 60)
        self.assertEqual(res, "Patient John will be 65 in 5 years.")

    def test_eligible(self):
        res = starter_code.get_screening_status("Alice", 70)
        self.assertEqual(res, "Patient Alice is eligible for screening.")

if __name__ == '__main__':
    unittest.main()
