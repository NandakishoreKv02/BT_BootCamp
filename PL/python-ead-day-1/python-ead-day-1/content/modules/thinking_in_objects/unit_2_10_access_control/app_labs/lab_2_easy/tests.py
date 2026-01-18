import unittest
import starter_code

class TestReadOnlyProperty(unittest.TestCase):
    def test_property_exists(self):
        m = starter_code.HeartMonitor(70)
        self.assertEqual(m.bpm, 70)
        
    def test_read_only_enforcement(self):
        m = starter_code.HeartMonitor(70)
        with self.assertRaises(AttributeError):
            m.bpm = 80

if __name__ == "__main__":
    unittest.main()
