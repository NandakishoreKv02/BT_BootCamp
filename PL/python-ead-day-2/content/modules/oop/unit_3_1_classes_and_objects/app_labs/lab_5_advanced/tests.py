import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

class TestIdentityEquality(unittest.TestCase):
    def test_comparisons(self):
        try:
            from starter_code import record1, record2, record3, compare_records
            
            # Record 1 vs 2: Different objects, same data
            res12 = compare_records(record1, record2)
            self.assertFalse(res12[0]) # is_same_object
            self.assertTrue(res12[1])  # has_same_data
            
            # Record 1 vs 3: Same objects
            res13 = compare_records(record1, record3)
            self.assertTrue(res13[0])
            self.assertTrue(res13[1])
            
        except ImportError:
            self.fail("Missing variables or functions in starter_code")

if __name__ == "__main__":
    unittest.main()
