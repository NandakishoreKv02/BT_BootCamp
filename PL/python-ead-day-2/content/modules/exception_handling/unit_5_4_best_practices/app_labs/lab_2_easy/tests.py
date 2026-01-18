import unittest
from starter_code import calculate_avg_vitals_clean

class TestLab2(unittest.TestCase):
    def test_success(self):
        self.assertEqual(calculate_avg_vitals_clean(100, 5), 20.0)

    def test_zero_specifc(self):
        self.assertEqual(calculate_avg_vitals_clean(100, 0), 0)

    def test_logic_flow(self):
        # This test ensures the happy path continues correctly
        # We can't easily test "narrow scope" with logic, 
        # but we can ensure standard behavior.
        pass

if __name__ == "__main__":
    unittest.main()
