import unittest
import starter_code

class TestAnalyticsEngine(unittest.TestCase):
    def test_dataset(self):
        d = starter_code.create_dataset("T", [1, 2, 3])
        self.assertEqual(d['label'], "T")
        self.assertEqual(len(d['values']), 3)

    def test_extensibility(self):
        d = starter_code.create_dataset("Glucose", [100, 200])
        
        # Test with mean
        res = starter_code.analyze_dataset(d, starter_code.get_mean)
        self.assertIn("150", str(res))
        
        # Test with a lambda (proves extensibility)
        res_sum = starter_code.analyze_dataset(d, sum)
        self.assertIn("300", str(res_sum))

if __name__ == "__main__":
    unittest.main()
