import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestConfigLoader(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_integers(self):
        self.assertEqual(starter_code.infer_type("123"), 123)
        self.assertEqual(starter_code.infer_type("-50"), -50)

    def test_floats(self):
        self.assertEqual(starter_code.infer_type("3.14"), 3.14)
        self.assertEqual(starter_code.infer_type("-0.001"), -0.001)

    def test_booleans(self):
        self.assertIs(starter_code.infer_type("true"), True)
        self.assertIs(starter_code.infer_type("True"), True)
        self.assertIs(starter_code.infer_type("FALSE"), False)

    def test_none(self):
        self.assertIsNone(starter_code.infer_type("None"))
        self.assertIsNone(starter_code.infer_type("NULL"))

    def test_strings(self):
        # Fallback
        self.assertEqual(starter_code.infer_type("prod_db"), "prod_db")
        self.assertEqual(starter_code.infer_type("127.0.0.1"), "127.0.0.1") # Looks like float but isn't

    def test_full_dict(self):
        raw = {
            "A": "10",
            "B": "3.5",
            "C": "False"
        }
        res = starter_code.load_config(raw)
        self.assertEqual(res["A"], 10)
        self.assertEqual(res["B"], 3.5)
        self.assertIs(res["C"], False)

if __name__ == '__main__':
    unittest.main()
