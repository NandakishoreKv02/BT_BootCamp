import unittest
import starter_code

class TestWardComposition(unittest.TestCase):
    def test_one_to_many_init(self):
        ward = starter_code.HospitalWard("ICU", 5)
        self.assertEqual(len(ward.beds), 5)
        self.assertTrue(all(isinstance(b, starter_code.Bed) for b in ward.beds))
        self.assertEqual(ward.beds[0].bed_number, 1)

if __name__ == "__main__":
    unittest.main()
