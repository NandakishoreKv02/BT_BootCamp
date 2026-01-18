import unittest
import starter_code

class TestBatchProcessing(unittest.TestCase):
    def test_variable_counts(self):
        la = starter_code.LabAnalyzer()
        self.assertEqual(la.average_glucose(100, 200), 150)
        self.assertEqual(la.average_glucose(10, 20, 30), 20)
        
    def test_empty_guards(self):
        la = starter_code.LabAnalyzer()
        self.assertEqual(la.average_glucose(), 0)

if __name__ == "__main__":
    unittest.main()
