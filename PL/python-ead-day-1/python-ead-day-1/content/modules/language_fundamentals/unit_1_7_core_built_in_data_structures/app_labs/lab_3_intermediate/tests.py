import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestAllergySets(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_intersection(self):
        a = ["Latex", "Penicillin", "Latex"]
        b = ["Penicillin", "Peanuts"]
        res = starter_code.get_common_allergies(a, b)
        self.assertIsInstance(res, set)
        self.assertEqual(res, {"Penicillin"})

    def test_no_overlap(self):
        a = ["Latex"]
        b = ["Peanuts"]
        self.assertEqual(starter_code.get_common_allergies(a, b), set())

    def test_empty(self):
        self.assertEqual(starter_code.get_common_allergies([], ["Latex"]), set())

if __name__ == '__main__':
    unittest.main()
