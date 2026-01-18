import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestFlowRate(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_with_override(self):
        self.assertEqual(starter_code.calculate_flow_rate(500, 2), 250.0)

    def test_default_usage(self):
        self.assertEqual(starter_code.calculate_flow_rate(100), 100.0)

if __name__ == '__main__':
    unittest.main()
