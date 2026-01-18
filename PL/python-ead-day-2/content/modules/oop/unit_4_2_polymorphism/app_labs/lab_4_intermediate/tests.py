import unittest
from abc import ABC
from starter_code import MedicalDevice, InfusionPump

class TestLab4(unittest.TestCase):
    def test_abc_enforcement(self):
        """Verify that MedicalDevice is an abstract class."""
        self.assertTrue(issubclass(MedicalDevice, ABC))
        with self.assertRaises(TypeError):
            MedicalDevice()

    def test_infusion_pump_implementation(self):
        """Verify InfusionPump implements necessary methods."""
        pump = InfusionPump()
        self.assertTrue(pump.connect())
        status = pump.get_status()
        self.assertIsInstance(status, dict)
        self.assertIn("battery", status)

    def test_broken_implementation(self):
        """Verify that a class missing methods cannot be instantiated."""
        class BrokenDevice(MedicalDevice):
            def connect(self): return True
            # missing get_status
            
        with self.assertRaises(TypeError):
            BrokenDevice()

if __name__ == '__main__':
    unittest.main()
