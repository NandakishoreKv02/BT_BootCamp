import unittest
import starter_code

class TestDeviceRegistry(unittest.TestCase):
    def test_multi_attribute(self):
        dev = starter_code.MedicalDevice("Monitor", "M-101", "Cardiac")
        self.assertEqual(dev.model, "Monitor")
        self.assertEqual(dev.serial, "M-101")
        self.assertEqual(dev.dept, "Cardiac")
        self.assertEqual(dev.status, "Active")

    def test_independence(self):
        d1 = starter_code.MedicalDevice("A", "1", "X")
        d2 = starter_code.MedicalDevice("B", "2", "Y")
        self.assertNotEqual(d1.serial, d2.serial)

if __name__ == "__main__":
    unittest.main()
