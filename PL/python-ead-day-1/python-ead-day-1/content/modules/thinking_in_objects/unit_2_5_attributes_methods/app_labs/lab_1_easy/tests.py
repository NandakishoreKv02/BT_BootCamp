import unittest
import starter_code

class TestInstanceState(unittest.TestCase):
    def test_init(self):
        p = starter_code.PatientState("1", 70, 98)
        self.assertEqual(p.pid, "1")
        self.assertEqual(p.hr, 70)

    def test_independence(self):
        p1 = starter_code.PatientState("1", 70, 98)
        p2 = starter_code.PatientState("2", 80, 99)
        p1.hr = 100
        self.assertEqual(p2.hr, 80)

if __name__ == "__main__":
    unittest.main()
