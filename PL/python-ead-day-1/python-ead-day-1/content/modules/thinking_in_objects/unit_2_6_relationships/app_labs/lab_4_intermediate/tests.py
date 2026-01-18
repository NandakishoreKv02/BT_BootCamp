import unittest
import starter_code

class TestLifecycle(unittest.TestCase):
    def test_composition_vs_aggregation(self):
        dr = starter_code.Doctor("Smith")
        p1 = starter_code.Patient("A", 101, dr)
        p2 = starter_code.Patient("B", 102, dr)
        
        # Composition: Charts must be distinct and owned
        self.assertNotEqual(p1.chart, p2.chart)
        self.assertEqual(p1.chart.chart_id, 101)
        
        # Aggregation: Doctor must be the exact same object
        self.assertIs(p1.primary_doctor, p2.primary_doctor)
        self.assertIs(p1.primary_doctor, dr)

if __name__ == "__main__":
    unittest.main()
