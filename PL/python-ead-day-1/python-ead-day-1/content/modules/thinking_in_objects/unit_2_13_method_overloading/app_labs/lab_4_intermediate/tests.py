import unittest
import starter_code

class TestKwargsTaging(unittest.TestCase):
    def test_dynamic_attributes(self):
        p = starter_code.PatientProfile("Alice")
        p.add_tags(priority="High", fasting=True)
        
        self.assertEqual(p.tags["priority"], "High")
        self.assertTrue(p.tags["fasting"])
        
    def test_accumulation(self):
        p = starter_code.PatientProfile("Bob")
        p.add_tags(t1=1)
        p.add_tags(t2=2)
        self.assertEqual(len(p.tags), 2)

if __name__ == "__main__":
    unittest.main()
