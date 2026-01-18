import unittest
import starter_code

class TestArgumentMixing(unittest.TestCase):
    def test_full_signature(self):
        dh = starter_code.DataHarvester()
        res = dh.log_event("Surgery", 3, "HR", "BP", surgeon="Smith")
        
        self.assertEqual(res["type"], "Surgery")
        self.assertEqual(res["severity"], 3)
        self.assertEqual(len(res["vitals"]), 2)
        self.assertEqual(res["tags"]["surgeon"], "Smith")
        
    def test_partial_signature(self):
        dh = starter_code.DataHarvester()
        res = dh.log_event("Checkup")
        self.assertEqual(res["severity"], 1)
        self.assertEqual(len(res["vitals"]), 0)

if __name__ == "__main__":
    unittest.main()
