import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestTupleRange(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_range_retrieval(self):
        res = starter_code.get_hr_range()
        self.assertIsInstance(res, tuple)
        self.assertEqual(res, (60, 100))

    def test_normal_check(self):
        ref = (60, 100)
        self.assertTrue(starter_code.is_value_normal(72, ref))
        self.assertTrue(starter_code.is_value_normal(60, ref))
        self.assertTrue(starter_code.is_value_normal(100, ref))
        self.assertFalse(starter_code.is_value_normal(59, ref))
        self.assertFalse(starter_code.is_value_normal(120, ref))

if __name__ == '__main__':
    unittest.main()
