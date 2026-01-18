import unittest
from starter_code import InfusionPump, HeartMonitor, MedicalDevice

class TestConcreteDevices(unittest.TestCase):
    def test_pump_implementation(self):
        pump = InfusionPump()
        self.assertIsInstance(pump, MedicalDevice)
        self.assertIn("5ml/hr", pump.operate())
        
    def test_monitor_implementation(self):
        monitor = HeartMonitor()
        self.assertIsInstance(monitor, MedicalDevice)
        self.assertIn("Monitoring", monitor.operate())

if __name__ == "__main__":
    unittest.main()
