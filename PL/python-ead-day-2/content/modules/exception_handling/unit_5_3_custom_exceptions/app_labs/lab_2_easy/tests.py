import unittest
from starter_code import access_resource, SecurityError

class TestLab2(unittest.TestCase):
    def test_attributes(self):
        try:
            access_resource("guest", "vault")
            self.fail("Should raise")
        except SecurityError as e:
            self.assertEqual(e.user, "guest")
            self.assertEqual(e.resource, "vault")
            self.assertIn("User guest denied access to vault", str(e))

    def test_access_granted(self):
        self.assertEqual(access_resource("admin", "vault"), "Access Granted")

if __name__ == "__main__":
    unittest.main()
