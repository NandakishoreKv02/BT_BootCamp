import unittest
import starter_code

class TestStationAggregation(unittest.TestCase):
    def test_aggregation(self):
        n1 = starter_code.Nurse("A")
        n2 = starter_code.Nurse("B")
        station = starter_code.NursingStation("S1")
        station.assign_nurse(n1)
        station.assign_nurse(n2)
        
        self.assertEqual(len(station.nurses), 2)
        self.assertIs(station.nurses[0], n1)

if __name__ == "__main__":
    unittest.main()
