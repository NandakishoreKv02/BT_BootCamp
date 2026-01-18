import unittest
from starter_code import VitalHistory

class TestLab5(unittest.TestCase):
    def test_collection_protocol(self):
        """Test len, getitem and iter."""
        data = [98.6, 99.1, 98.4]
        h = VitalHistory(data)
        self.assertEqual(len(h), 3)
        self.assertEqual(h[1], 99.1)
        self.assertEqual(list(h), data)

    def test_subtraction(self):
        """Test the __sub__ operator for average difference."""
        h1 = VitalHistory([10, 20, 30]) # Avg 20
        h2 = VitalHistory([5, 10, 15])  # Avg 10
        self.assertEqual(h1 - h2, 10.0)
        self.assertEqual(h2 - h1, -10.0)

    def test_subtraction_empty(self):
        """Ensure it handles empty lists."""
        h1 = VitalHistory([10, 20])
        h2 = VitalHistory([])
        self.assertEqual(h1 - h2, 15.0)

    def test_type_safety(self):
        """Ensure __sub__ only accepts VitalHistory."""
        h = VitalHistory([10])
        with self.assertRaises(TypeError):
            _ = h - [10]

    def test_repr(self):
        """Verify __repr__ implementation."""
        h = VitalHistory([1.1, 2.2])
        self.assertIn("VitalHistory", repr(h))
        self.assertIn("[1.1, 2.2]", repr(h))

if __name__ == '__main__':
    unittest.main()
