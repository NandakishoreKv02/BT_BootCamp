import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestHospitalManager(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_report_logic(self):
        """Test calculation implementation."""
        test_data = {
            "Dept 1": {
                "W1": {"occupied": 5, "total": 10},
                "W2": {"occupied": 2, "total": 10}
            },
            "Dept 2": {
                "W3": {"occupied": 3, "total": 5}
            }
        }
        # Total Beds: 25, Occ: 10 => 40.0%
        result = starter_code.generate_report(test_data)
        self.assertEqual(result['total_beds'], 25)
        self.assertEqual(result['total_occupied'], 10)
        self.assertEqual(result['occupancy_rate'], 40.0)

    def test_empty_hospital(self):
        """Test division by zero protection."""
        result = starter_code.generate_report({})
        self.assertEqual(result['occupancy_rate'], 0.0)

    def test_empty_department(self):
        """Test handling empty sub-dictionaries."""
        test_data = {
            "EmptyDept": {},
            "RealDept": {"W1": {"occupied": 10, "total": 10}}
        }
        result = starter_code.generate_report(test_data)
        self.assertEqual(result['total_beds'], 10)
        self.assertEqual(result['total_occupied'], 10)
        self.assertEqual(result['occupancy_rate'], 100.0)

if __name__ == '__main__':
    unittest.main()
