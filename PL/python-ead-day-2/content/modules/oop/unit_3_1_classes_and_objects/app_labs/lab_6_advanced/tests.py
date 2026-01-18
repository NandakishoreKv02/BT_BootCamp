import unittest
from starter_code import Patient

class TestIdentity(unittest.TestCase):
    def test_identity_check(self):
        p1 = Patient("Test")
        p2 = Patient("Test")
        p3 = p1
        
        self.assertFalse(p1 is p2)
        self.assertTrue(p1 is p3)

if __name__ == "__main__":
    unittest.main()
