import unittest
from starter_code import Patient

class TestCensus(unittest.TestCase):
    def setUp(self):
        # Reset census for each test
        Patient.census = 0

    def test_increment(self):
        p1 = Patient("A")
        p2 = Patient("B")
        self.assertEqual(Patient.get_census(), 2)

    def test_decrement(self):
        p1 = Patient("A")
        p1.discharge()
        self.assertEqual(Patient.get_census(), 0)

    def test_boundary(self):
        # Census should not go negative (though in this simple code it might if called incorrectly)
        Patient.census = 0
        p = Patient("A")
        p.discharge()
        p.discharge() 
        self.assertEqual(Patient.get_census(), 0)

if __name__ == "__main__":
    unittest.main()
