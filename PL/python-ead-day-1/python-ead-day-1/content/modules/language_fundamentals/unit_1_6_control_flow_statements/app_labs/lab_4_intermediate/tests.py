import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestLabFilter(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_standard_filter(self):
        data = [1, None, 2, 3]
        self.assertEqual(starter_code.sanitize_lab_results(data), [1, 2, 3])

    def test_break_logic(self):
        data = [10, "CRITICAL_ERROR", 20]
        # Should stop before 20
        self.assertEqual(starter_code.sanitize_lab_results(data), [10])

    def test_combined(self):
        data = [None, 5, "CRITICAL_ERROR", None, 10]
        self.assertEqual(starter_code.sanitize_lab_results(data), [5])

if __name__ == '__main__':
    unittest.main()
