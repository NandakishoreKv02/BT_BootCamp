import unittest

class TestNamedTuple(unittest.TestCase):
    def test_named_tuple(self):
        from starter_code import LabResult, glucose_test
        self.assertTrue(hasattr(glucose_test, 'test_name'))
        self.assertTrue(hasattr(glucose_test, 'value'))
        self.assertTrue(hasattr(glucose_test, 'unit'))
        self.assertEqual(glucose_test.test_name, "Glucose")
        
        # Test immutability
        with self.assertRaises(AttributeError):
            glucose_test.value = 100

if __name__ == "__main__":
    unittest.main()
