import unittest
from abc import ABC
from starter_code import AlertStrategy, ThresholdStrategy, AverageStrategy, PatientMonitor

class TestLab6(unittest.TestCase):
    def test_abc_interface(self):
        """Verify AlertStrategy is an ABC."""
        self.assertTrue(issubclass(AlertStrategy, ABC))
        with self.assertRaises(TypeError):
            AlertStrategy()

    def test_threshold_logic(self):
        """Verify ThresholdStrategy alerts on any high value."""
        s = ThresholdStrategy(100)
        self.assertTrue(s.evaluate([90, 101, 90]))
        self.assertFalse(s.evaluate([90, 99, 80]))

    def test_average_logic(self):
        """Verify AverageStrategy alerts on mean average."""
        s = AverageStrategy(100)
        # Avg is 105
        self.assertTrue(s.evaluate([100, 110]))
        # One high value but avg is 95
        self.assertFalse(s.evaluate([110, 80]))

    def test_monitor_integration(self):
        """Verify Monitor correctly uses the passed strategy."""
        m = PatientMonitor("Test", ThresholdStrategy(100))
        m.add_data(105)
        self.assertTrue(m.check_status())
        
        # Runtime swap
        m.strategy = AverageStrategy(110)
        self.assertFalse(m.check_status())

    def test_empty_data_handling(self):
        """Verify strategies handle empty lists."""
        s1 = ThresholdStrategy(100)
        s2 = AverageStrategy(100)
        self.assertFalse(s1.evaluate([]))
        self.assertFalse(s2.evaluate([]))

if __name__ == '__main__':
    unittest.main()
