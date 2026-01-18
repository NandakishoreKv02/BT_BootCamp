import unittest
import starter_code

class TestLabRequestDefaults(unittest.TestCase):
    def test_default_priority(self):
        req = starter_code.LabRequest("CBC")
        self.assertEqual(req.priority, "Routine")
        
    def test_override_priority(self):
        req = starter_code.LabRequest("Glucose", "STAT")
        self.assertEqual(req.priority, "STAT")

if __name__ == "__main__":
    unittest.main()
