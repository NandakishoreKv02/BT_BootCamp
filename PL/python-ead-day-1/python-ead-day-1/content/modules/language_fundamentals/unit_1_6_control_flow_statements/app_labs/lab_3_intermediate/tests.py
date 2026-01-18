import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestVitalPolling(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_found_stable(self):
        readings = [120, 110, 85, 75]
        self.assertEqual(starter_code.poll_until_stable(readings), 85)

    def test_immediate_stable(self):
        readings = [72, 110, 85]
        self.assertEqual(starter_code.poll_until_stable(readings), 72)

    def test_never_stable(self):
        readings = [150, 160, 40, 30]
        self.assertIsNone(starter_code.poll_until_stable(readings))

    def test_empty_list(self):
        self.assertIsNone(starter_code.poll_until_stable([]))

if __name__ == '__main__':
    unittest.main()
