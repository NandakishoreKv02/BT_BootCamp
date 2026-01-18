import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestAccessValidator(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        class MockUser: pass
        self.mock_user = MockUser()

    def test_authorized_doctor(self):
        self.assertTrue(starter_code.is_access_authorized(self.mock_user, "Doctor"))

    def test_authorized_nurse(self):
        self.assertTrue(starter_code.is_access_authorized(self.mock_user, "Nurse"))

    def test_unauthorized_role(self):
        self.assertFalse(starter_code.is_access_authorized(self.mock_user, "Intern"))
        self.assertFalse(starter_code.is_access_authorized(self.mock_user, "Guest"))

    def test_null_user(self):
        # Should be False even if role is valid
        self.assertFalse(starter_code.is_access_authorized(None, "Doctor"))

if __name__ == '__main__':
    unittest.main()
