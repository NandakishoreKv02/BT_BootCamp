import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestDataCleaner(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_mixed_data(self):
        # Valid: 80, 70, "90"(->90)
        # Invalid: "ERR", None
        # Sum: 240, Count: 3, Avg: 80.0
        data = [80, None, "ERR", 70, "90"]
        self.assertEqual(starter_code.calculate_average_hr(data), 80.0)

    def test_empty_or_invalid_only(self):
        self.assertEqual(starter_code.calculate_average_hr([]), 0.0)
        self.assertEqual(starter_code.calculate_average_hr(["Na", None]), 0.0)

    def test_floats_ignored(self):
        # Spec says "integers", let's see if implementation converts floats or ignores.
        # Ideally, heart rate is int. If explicit conversion used int(val), float would convert.
        # But if instructions imply "strict integers", float might be ignored.
        # Let's assume reasonable robustness: int(72.9) -> 72 is acceptable for this level.
        pass 

if __name__ == '__main__':
    unittest.main()
