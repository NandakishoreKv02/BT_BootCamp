import unittest
import importlib.util
import sys
import inspect

try:
    import starter_code
except ImportError:
    pass

class TestProfessionalDocs(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_docstring_exists(self):
        doc = starter_code.calculate_concentration.__doc__
        self.assertIsNotNone(doc)
        self.assertIn("Args", doc)

    def test_parameter_names(self):
        sig = inspect.signature(starter_code.calculate_concentration)
        self.assertIn("dose_mg", sig.parameters)
        self.assertIn("time_hr", sig.parameters)

if __name__ == '__main__':
    unittest.main()
