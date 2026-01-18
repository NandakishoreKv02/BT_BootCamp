import unittest
import starter_code

class TestEquipmentState(unittest.TestCase):
    def test_global_threshold(self):
        v1 = starter_code.Ventilator("SN1")
        v2 = starter_code.Ventilator("SN2")
        
        # Initial threshold 1000
        starter_code.Ventilator.service_threshold = 1000
        v1.log_usage(900)
        self.assertFalse(v1.check_status())
        
        # Global change
        starter_code.Ventilator.service_threshold = 800
        self.assertTrue(v1.check_status())
        self.assertFalse(v2.check_status()) # v2 has 0 hours

    def test_instance_independence(self):
        v1 = starter_code.Ventilator("SN1")
        v2 = starter_code.Ventilator("SN2")
        v1.log_usage(500)
        self.assertEqual(v1.hours_run, 500)
        self.assertEqual(v2.hours_run, 0)

if __name__ == "__main__":
    unittest.main()
