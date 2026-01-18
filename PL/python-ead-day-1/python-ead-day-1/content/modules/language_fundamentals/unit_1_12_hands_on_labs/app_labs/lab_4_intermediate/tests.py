import unittest
import starter_code

class TestLabAnalyzer(unittest.TestCase):
    def test_statistics(self):
        values = [100, 110, 120]
        stats = starter_code.calculate_statistics(values)
        self.assertEqual(stats["average"], 110)
        self.assertEqual(stats["min"], 100)
        self.assertEqual(stats["max"], 120)

    def test_trend_detection(self):
        improving = [120, 115, 110, 105]
        trend = starter_code.detect_trend(improving)
        self.assertEqual(trend, "Improving")

if __name__ == '__main__':
    unittest.main()
