import unittest
from starter_code import Thermometer, Oximeter, get_reading

class TestLab1(unittest.TestCase):
    def test_thermometer_read(self):
        t = Thermometer()
        # Ensure it has read method
        self.assertTrue(hasattr(t, 'read'))
        self.assertIsInstance(t.read(), str)

    def test_oximeter_read(self):
        o = Oximeter()
        self.assertTrue(hasattr(o, 'read'))
        self.assertIsInstance(o.read(), str)

    def test_duck_typing(self):
        t = Thermometer()
        o = Oximeter()
        # Function should work for both types
        self.assertTrue(len(get_reading(t)) > 0)
        self.assertTrue(len(get_reading(o)) > 0)

if __name__ == '__main__':
    unittest.main()
