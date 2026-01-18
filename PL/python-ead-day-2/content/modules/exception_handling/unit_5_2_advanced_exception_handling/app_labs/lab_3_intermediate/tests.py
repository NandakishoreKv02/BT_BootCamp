import unittest
from starter_code import connect_to_service, ServiceUnavailable, ConnectionTimeout

class TestLab3(unittest.TestCase):
    def test_chaining(self):
        try:
            connect_to_service()
            self.fail("Should have raised ServiceUnavailable")
        except ServiceUnavailable as e:
            self.assertEqual(str(e), "Service is down")
            self.assertIsInstance(e.__cause__, ConnectionTimeout)
            self.assertEqual(str(e.__cause__), "30s limit")

if __name__ == "__main__":
    unittest.main()
