import unittest

class TestNestedImmutability(unittest.TestCase):
    def test_integrity(self):
        from starter_code import study_data
        self.assertEqual(study_data[0], "Project-X")
        self.assertIn(40, study_data[1])
        
        # Ensure it is still a tuple
        self.assertIsInstance(study_data, tuple)

if __name__ == "__main__":
    unittest.main()
