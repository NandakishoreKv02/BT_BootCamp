import unittest
import starter_code

class TestBedIdentity(unittest.TestCase):
    def test_state_init(self):
        b = starter_code.Bed("Twin")
        self.assertEqual(b.model, "Twin")
        self.assertFalse(b.is_occupied)

    def test_identity_distinct(self):
        # Even if data is the same, objects must be different
        b1 = starter_code.Bed("X")
        b2 = starter_code.Bed("X")
        self.assertIsNot(b1, b2)
        self.assertNotEqual(id(b1), id(b2))

if __name__ == "__main__":
    unittest.main()
