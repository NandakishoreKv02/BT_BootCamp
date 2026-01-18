import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestProfessionalAuditor(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_flagging_logic(self):
        attempts = ["nurse1", "admin", "dr_smith"]
        res = starter_code.audit_logins(attempts)
        self.assertEqual(res, ["admin"])

    def test_constant_naming(self):
        # We look for something like FORBIDDEN_USERNAMES
        constants = [name for name in dir(starter_code) if name.isupper()]
        self.assertTrue(len(constants) > 0)

    def test_main_block(self):
        with open(starter_code.__file__) as f:
            content = f.read()
        self.assertIn("__name__", content)
        self.assertIn("__main__", content)

if __name__ == '__main__':
    unittest.main()
