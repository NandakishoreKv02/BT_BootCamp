import unittest
import starter_code

class TestDynamicProperties(unittest.TestCase):
    def test_formatted_display(self):
        m = starter_code.VitalsMonitor(37.5)
        self.assertEqual(m.display_temp, "37.5 °C")
        
    def test_logic_property(self):
        m = starter_code.VitalsMonitor(37.0)
        self.assertFalse(m.is_fever)
        m._temp = 39.0
        self.assertTrue(m.is_fever)

if __name__ == "__main__":
    unittest.main()
