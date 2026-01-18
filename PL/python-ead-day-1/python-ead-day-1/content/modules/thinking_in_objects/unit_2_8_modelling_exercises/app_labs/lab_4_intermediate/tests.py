import unittest
import starter_code

class TestLabDependency(unittest.TestCase):
    def test_processing_factory(self):
        analyzer = starter_code.Analyzer("Axon")
        sample = starter_code.BloodSample("S-001")
        
        result = analyzer.process(sample)
        
        self.assertTrue(isinstance(result, starter_code.LabResult))
        self.assertEqual(result.value, "Normal")
        self.assertEqual(result.status, "Verified")

if __name__ == "__main__":
    unittest.main()
