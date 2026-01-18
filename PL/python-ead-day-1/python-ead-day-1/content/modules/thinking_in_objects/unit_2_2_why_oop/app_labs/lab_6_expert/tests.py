import unittest
import starter_code

class TestHL7Simulator(unittest.TestCase):
    def test_rendering(self):
        m = starter_code.create_message()
        s1 = starter_code.create_segment("MSH", ["A", "B"])
        s2 = starter_code.create_segment("PID", ["1", "X"])
        
        starter_code.add_segment(m, s1)
        starter_code.add_segment(m, s2)
        
        out = starter_code.to_hl7_string(m)
        
        # Check format
        self.assertIn("MSH|A|B", out)
        self.assertIn("PID|1|X", out)
        self.assertEqual(len(out.split('\n')), 2)

    def test_empty(self):
        m = starter_code.create_message()
        self.assertEqual(starter_code.to_hl7_string(m), "")

if __name__ == "__main__":
    unittest.main()
