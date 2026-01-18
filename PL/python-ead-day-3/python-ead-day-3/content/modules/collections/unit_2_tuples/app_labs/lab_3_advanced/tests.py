import unittest
from starter_code import Reading, convert_to_namedtuples, analyze_overall_trend, find_rapid_changes

class TestTrends(unittest.TestCase):
    
    def test_convert(self):
        raw = [("10:00", 60, 36)]
        res = convert_to_namedtuples(raw)
        self.assertEqual(len(res), 1)
        self.assertIsInstance(res[0], Reading)
        self.assertEqual(res[0].hr, 60)
        
    def test_trend(self):
        readings = [Reading("Start", 60, 36.0), Reading("End", 80, 38.0)]
        delta = analyze_overall_trend(readings)
        self.assertEqual(delta, (20, 2.0))
        
    def test_rapid_changes(self):
        readings = [
            Reading("01:00", 60, 36),
            Reading("02:00", 65, 36), # +5 (Safe)
            Reading("03:00", 90, 36), # +25 (Spike)
            Reading("04:00", 60, 36)  # -30 (Drop)
        ]
        spikes = find_rapid_changes(readings)
        self.assertEqual(len(spikes), 2)
        self.assertEqual(spikes[0], ("03:00", 25))
        self.assertEqual(spikes[1], ("04:00", -30))

if __name__ == '__main__':
    unittest.main()
