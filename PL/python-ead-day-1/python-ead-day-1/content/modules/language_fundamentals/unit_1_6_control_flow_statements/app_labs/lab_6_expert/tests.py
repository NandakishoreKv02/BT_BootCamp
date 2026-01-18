import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestBillingGenerator(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_basic_and_emergency(self):
        data = [
            {"service": "A", "cost": 100, "is_emergency": False, "status": "Done"},
            {"service": "B", "cost": 100, "is_emergency": True, "status": "Done"}
        ]
        # 100 + (100 + 20) = 220
        self.assertEqual(starter_code.calculate_bill(data), 220.0)

    def test_skip_cancelled(self):
        data = [
            {"service": "A", "cost": 100, "is_emergency": False, "status": "Done"},
            {"service": "B", "cost": 100, "is_emergency": False, "status": "Cancelled"}
        ]
        self.assertEqual(starter_code.calculate_bill(data), 100.0)

    def test_discount_rule(self):
        # 600 total -> 600 * 0.9 = 540
        data = [
            {"service": "A", "cost": 500, "is_emergency": True, "status": "Done"}
        ]
        # 500 + 100 (emergency) = 600. 600 > 500, so 600 * 0.9 = 540
        self.assertEqual(starter_code.calculate_bill(data), 540.0)
        
    def test_no_discount_at_threshold(self):
        # 500 exactly -> no discount
        data = [{"service": "A", "cost": 500, "is_emergency": False, "status": "Done"}]
        self.assertEqual(starter_code.calculate_bill(data), 500.0)

if __name__ == '__main__':
    unittest.main()
