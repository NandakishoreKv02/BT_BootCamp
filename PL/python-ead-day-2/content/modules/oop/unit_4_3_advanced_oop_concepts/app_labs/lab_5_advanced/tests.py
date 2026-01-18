import unittest
from starter_code import TelemetryPacket, LegacyPacket

class TestLab5(unittest.TestCase):
    def test_slots_defined(self):
        self.assertTrue(hasattr(TelemetryPacket, "__slots__"))
        self.assertEqual(TelemetryPacket.__slots__, ('device_id', 'timestamp', 'value'))

    def test_dict_absence(self):
        p = TelemetryPacket("A", "B", 10)
        self.assertFalse(hasattr(p, "__dict__"))

    def test_restriction_enforcement(self):
        p = TelemetryPacket("A", "B", 10)
        with self.assertRaises(AttributeError):
            p.extra = "value"

if __name__ == '__main__':
    unittest.main()
