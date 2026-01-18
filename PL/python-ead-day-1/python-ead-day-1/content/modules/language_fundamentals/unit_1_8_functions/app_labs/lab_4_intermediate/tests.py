import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestTriageLogic(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_critical(self):
        self.assertEqual(starter_code.get_triage_category(190), "CRITICAL")

    def test_urgent(self):
        self.assertEqual(starter_code.get_triage_category(150), "URGENT")

    def test_normal(self):
        self.assertEqual(starter_code.get_triage_category(115), "NORMAL")

if __name__ == '__main__':
    unittest.main()
