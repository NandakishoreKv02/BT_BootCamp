import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestBatchProcessor(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_analysis(self):
        data = [
            {"type": "A", "val": 10},
            {"type": "A", "val": 20},
            {"type": "B", "val": 30}
        ]
        avg, filtered = starter_code.analyze_batch(data, "A", 15)
        
        # Check Average
        self.assertEqual(avg, 15.0)
        
        # Check Filtering
        self.assertEqual(len(filtered), 2)
        
        # Check Alert Logic
        self.assertFalse(filtered[0]["is_alert"])
        self.assertTrue(filtered[1]["is_alert"])

    def test_missing_type(self):
        data = [{"type": "A", "val": 10}]
        avg, filtered = starter_code.analyze_batch(data, "B", 15)
        self.assertEqual(avg, 0.0)
        self.assertEqual(filtered, [])

if __name__ == '__main__':
    unittest.main()
