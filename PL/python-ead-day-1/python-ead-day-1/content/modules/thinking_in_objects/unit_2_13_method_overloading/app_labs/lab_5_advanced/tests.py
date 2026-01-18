import unittest
import starter_code

class TestSmartDispatch(unittest.TestCase):
    def test_id_query(self):
        dc = starter_code.DiagnosticCenter()
        self.assertIn("Report ID: 5", dc.fetch_details(5))
        
    def test_dict_query(self):
        dc = starter_code.DiagnosticCenter()
        self.assertIn("metrics", dc.fetch_details({"date": "today"}))
        
    def test_invalid_type(self):
        dc = starter_code.DiagnosticCenter()
        with self.assertRaises(TypeError):
            dc.fetch_details(["list"])

if __name__ == "__main__":
    unittest.main()
