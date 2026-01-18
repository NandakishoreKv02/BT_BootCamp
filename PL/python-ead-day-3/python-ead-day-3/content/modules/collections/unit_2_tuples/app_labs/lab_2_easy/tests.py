import unittest

class TestUnpacking(unittest.TestCase):
    def test_unpack_and_swap(self):
        from starter_code import temperature, heart_rate, systolic_bp, doc_a, doc_b
        self.assertEqual(temperature, 38.2)
        self.assertEqual(heart_rate, 85)
        self.assertEqual(systolic_bp, 120)
        self.assertEqual(doc_a, "Dr. Jones")
        self.assertEqual(doc_b, "Dr. Smith")

if __name__ == "__main__":
    unittest.main()
