import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestQueueManager(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_routine_capacity(self):
        queue = [
            {"name": "A", "urgent": False},
            {"name": "B", "urgent": False},
            {"name": "C", "urgent": False}
        ]
        # Only A and B should get in with capacity 2
        self.assertEqual(starter_code.admit_patients(queue, 2), ["A", "B"])

    def test_urgent_bypass(self):
        queue = [
            {"name": "A", "urgent": False},
            {"name": "U1", "urgent": True},
            {"name": "B", "urgent": False},
        ]
        # A and B take full routine capacity, but U1 gets in anyway
        self.assertEqual(starter_code.admit_patients(queue, 2), ["A", "U1", "B"])

    def test_absolute_limit(self):
        # 2x capacity = limit. Cap=1, limit=2.
        queue = [
            {"name": "U1", "urgent": True},
            {"name": "U2", "urgent": True},
            {"name": "U3", "urgent": True} # Should be stopped by absolute limit
        ]
        self.assertEqual(starter_code.admit_patients(queue, 1), ["U1", "U2"])

if __name__ == '__main__':
    unittest.main()
