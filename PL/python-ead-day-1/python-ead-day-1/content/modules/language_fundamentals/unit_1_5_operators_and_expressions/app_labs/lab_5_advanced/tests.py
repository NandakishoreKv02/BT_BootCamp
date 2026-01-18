import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestFluidBalance(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_positive_balance(self):
        # (1500+500) - (1000+200) = 800
        self.assertEqual(starter_code.calculate_fluid_status(1500, 500, 1000, 200), 800.0)

    def test_negative_balance(self):
        # (500+200) - (1000+500) = -800
        self.assertEqual(starter_code.calculate_fluid_status(500, 200, 1000, 500), -800.0)

    def test_with_scale_factor(self):
        # ((1000+500) - (500+500)) * 0.001 = 0.5 (mL to L)
        res = starter_code.calculate_fluid_status(1000, 500, 500, 500, scale_factor=0.001)
        self.assertEqual(res, 0.5)

if __name__ == '__main__':
    unittest.main()
