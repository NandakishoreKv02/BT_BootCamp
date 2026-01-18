import unittest
from starter_code import LabAnalytics

class TestAbstractionLayers(unittest.TestCase):
    def test_public_api_returns_valid_average(self):
        la = LabAnalytics()
        avg = la.get_average_glucose()
        # Expected: (110 + 125 + 120 + 115) / 4 = 117.5
        self.assertAlmostEqual(avg, 117.5, places=1)
        
    def test_private_methods_exist(self):
        la = LabAnalytics()
        self.assertTrue(hasattr(la, '_fetch_raw_data'))
        self.assertTrue(hasattr(la, '_validate'))
        self.assertTrue(hasattr(la, '_compute_mean'))

if __name__ == "__main__":
    unittest.main()
