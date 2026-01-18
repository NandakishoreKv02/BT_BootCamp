import unittest
from starter_code import route_request, ServiceError

class TestLab6(unittest.TestCase):
    def test_retry(self):
        def f(): raise ServiceError(503)
        self.assertEqual(route_request(f), "Retry")

    def test_abort(self):
        def f(): raise ServiceError(404)
        self.assertEqual(route_request(f), "Abort")

    def test_refresh(self):
        def f(): raise ServiceError(401)
        self.assertEqual(route_request(f), "Refresh")

    def test_unknown(self):
        def f(): raise ServiceError(999)
        self.assertEqual(route_request(f), "Unknown")

    def test_success(self):
        self.assertEqual(route_request(lambda: None), "Success")

if __name__ == "__main__":
    unittest.main()
