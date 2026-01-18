import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestNamingRefactor(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_surplus(self):
        res = starter_code.refactor_balance_logic(100, 50)
        self.assertEqual(res.get("balance"), 50)
        self.assertEqual(res.get("status"), "SURPLUS")

    def test_deficit(self):
        res = starter_code.refactor_balance_logic(50, 100)
        self.assertEqual(res.get("status"), "DEFICIT")

if __name__ == '__main__':
    unittest.main()
