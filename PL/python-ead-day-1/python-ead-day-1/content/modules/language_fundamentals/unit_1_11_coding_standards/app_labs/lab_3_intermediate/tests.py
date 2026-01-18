import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestPythonicPortal(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_class_naming(self):
        self.assertTrue(hasattr(starter_code, "PatientData"))

    def test_membership_logic(self):
        self.assertTrue(starter_code.is_admitted("A", ["A", "B"]))
        self.assertFalse(starter_code.is_admitted("C", ["A", "B"]))

if __name__ == '__main__':
    unittest.main()
