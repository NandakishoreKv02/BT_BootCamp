import unittest

class TestTupleBasics(unittest.TestCase):
    def test_tuple(self):
        from starter_code import patient_identity
        self.assertIsInstance(patient_identity, tuple)
        self.assertEqual(len(patient_identity), 3)

if __name__ == "__main__":
    unittest.main()
