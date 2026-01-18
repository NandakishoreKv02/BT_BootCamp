import unittest
import starter_code

class TestBedBehavior(unittest.TestCase):
    def test_state_change(self):
        m = starter_code.BPMonitor("Test")
        m.take_reading(120, 80)
        self.assertEqual(m.systolic, 120)
        self.assertEqual(m.analyze(), "NORMAL")
        
    def test_hypertension(self):
        m = starter_code.BPMonitor("Test")
        m.take_reading(150, 95)
        self.assertEqual(m.analyze(), "HYPERTENSION")

    def test_hypotension(self):
        m = starter_code.BPMonitor("Test")
        m.take_reading(80, 50)
        self.assertEqual(m.analyze(), "HYPOTENSION")

if __name__ == "__main__":
    unittest.main()
