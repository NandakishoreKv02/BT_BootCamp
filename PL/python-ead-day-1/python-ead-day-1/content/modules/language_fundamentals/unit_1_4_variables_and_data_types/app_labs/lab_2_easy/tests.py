import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestBMI(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_standard_calculation(self):
        # 70 / (1.75^2) = 22.857... -> 22.86
        self.assertEqual(starter_code.calculate_bmi(70, 1.75), 22.86)

    def test_integer_inputs(self):
        # Should handle ints gracefully
        # 80 / (2^2) = 20.0
        self.assertEqual(starter_code.calculate_bmi(80, 2), 20.0)

    def test_zero_height(self):
        self.assertEqual(starter_code.calculate_bmi(70, 0), 0.0)

    def test_negative_height(self):
        self.assertEqual(starter_code.calculate_bmi(70, -1.8), 0.0)

if __name__ == '__main__':
    unittest.main()
