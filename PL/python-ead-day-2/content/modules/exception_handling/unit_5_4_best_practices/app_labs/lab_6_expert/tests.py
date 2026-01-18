import unittest
from starter_code import filter_stream_eafp, filter_stream_lbyl

class TestLab6(unittest.TestCase):
    def test_eafp_correctness(self):
        data = ["10.5", "abc", 5, None]
        self.assertEqual(filter_stream_eafp(data), 15.5)

    def test_lbyl_correctness(self):
        # LBYL is trickier with strings, but we'll test basic numeric support
        data = [10.5, 5]
        self.assertEqual(filter_stream_lbyl(data), 15.5)

if __name__ == "__main__":
    unittest.main()
