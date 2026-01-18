import unittest
from starter_code import VitalSign, check_alert

class TestLab3(unittest.TestCase):
    def test_str_repr(self):
        v = VitalSign(120, "bpm")
        self.assertEqual(str(v), "120 bpm")

    def test_comparisons(self):
        v1 = VitalSign(100, "bpm")
        v2 = VitalSign(90, "bpm")
        self.assertTrue(v1 > v2)
        self.assertFalse(v1 < v2)
        self.assertFalse(v2 > v1)

    def test_unit_mismatch(self):
        v1 = VitalSign(100, "F")
        v2 = VitalSign(37, "C")
        with self.assertRaises(ValueError):
            _ = v1 > v2

    def test_type_error(self):
        v1 = VitalSign(100, "F")
        with self.assertRaises(TypeError):
            _ = v1 > 100

    def test_check_alert(self):
        # Assuming alert is triggers
        self.assertEqual(check_alert(VitalSign(101, "F"), VitalSign(100, "F")), "CRITICAL")
        self.assertEqual(check_alert(VitalSign(99, "F"), VitalSign(100, "F")), "NORMAL")

if __name__ == '__main__':
    unittest.main()
