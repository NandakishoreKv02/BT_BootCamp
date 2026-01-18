import unittest
from starter_code import Device, XRayMachine, HeartMonitor

class TestLab2(unittest.TestCase):
    def test_base_behavior(self):
        d = Device()
        self.assertEqual(d.start(), "Starting generic device")

    def test_xray_override(self):
        x = XRayMachine()
        self.assertEqual(x.start(), "Warming up radiation source")
        # Ensure it inherits stop
        self.assertEqual(x.stop(), "Stopping generic device")

    def test_monitor_override(self):
        h = HeartMonitor()
        self.assertEqual(h.start(), "Calibrating sensors")

    def test_polymorphism(self):
        devices = [XRayMachine(), HeartMonitor()]
        results = [d.start() for d in devices]
        self.assertIn("Warming up radiation source", results)
        self.assertIn("Calibrating sensors", results)

if __name__ == '__main__':
    unittest.main()
