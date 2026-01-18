import unittest
import starter_code

class TestVitalLogging(unittest.TestCase):
    def test_single_arg(self):
        log = starter_code.VitalLogger()
        self.assertEqual(log.log_hr(70), "Logged BPM: 70")
        
    def test_multi_arg_simulation(self):
        log = starter_code.VitalLogger()
        self.assertIn("S-1", log.log_hr(70, "S-1"))

if __name__ == "__main__":
    unittest.main()
