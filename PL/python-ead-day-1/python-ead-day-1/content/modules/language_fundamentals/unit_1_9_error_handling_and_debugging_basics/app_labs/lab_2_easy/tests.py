import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestHistoryNavigator(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_valid_access(self):
        self.assertEqual(starter_code.get_historical_result([1, 2, 3], 0), 1)

    def test_invalid_access(self):
        self.assertEqual(starter_code.get_historical_result([1], 10), "Result Not Available")

    def test_empty_list(self):
        self.assertEqual(starter_code.get_historical_result([], 0), "Result Not Available")

if __name__ == '__main__':
    unittest.main()
