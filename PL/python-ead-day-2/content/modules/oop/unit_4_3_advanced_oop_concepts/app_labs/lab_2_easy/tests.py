import unittest
from starter_code import Sensor, MonitoringDevice

class TestLab2(unittest.TestCase):
    def test_sensor_init(self):
        s = Sensor("EKG", "Model-A")
        self.assertEqual(s.sensor_type, "EKG")

    def test_composition(self):
        device = MonitoringDevice("Unit-Test")
        s1 = Sensor("1", "A")
        s2 = Sensor("2", "B")
        device.add_sensor(s1)
        device.add_sensor(s2)
        
        self.assertEqual(len(device.sensors), 2)
        self.assertEqual(device.sensors[0].model, "A")

    def test_inventory_logic(self):
        device = MonitoringDevice("Unit-Test")
        device.add_sensor(Sensor("TypeX", "X1"))
        inventory = device.get_inventory()
        self.assertEqual(inventory[0], "TypeX: X1")

if __name__ == '__main__':
    unittest.main()
