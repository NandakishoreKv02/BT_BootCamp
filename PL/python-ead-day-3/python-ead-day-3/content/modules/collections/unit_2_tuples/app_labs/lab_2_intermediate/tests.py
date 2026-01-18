import unittest
from starter_code import calculate_average_hr, find_fever_incidents, generate_summary

class TestVitalsAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.data = [
            ("08:00", 60, 36.0),
            ("09:00", 80, 39.0),
            ("10:00", 100, 36.0)
        ]
        
    def test_average(self):
        # (60+80+100)/3 = 80
        self.assertEqual(calculate_average_hr(self.data), 80.0)
        self.assertEqual(calculate_average_hr([]), 0)
        
    def test_fever(self):
        res = find_fever_incidents(self.data)
        self.assertEqual(res, ["09:00"])
        
    def test_summary(self):
        # min_hr=60, max_hr=100, avg_temp=(36+39+36)/3 = 37.0
        res = generate_summary(self.data)
        self.assertEqual(res, (60, 100, 37.0))

if __name__ == '__main__':
    unittest.main()
