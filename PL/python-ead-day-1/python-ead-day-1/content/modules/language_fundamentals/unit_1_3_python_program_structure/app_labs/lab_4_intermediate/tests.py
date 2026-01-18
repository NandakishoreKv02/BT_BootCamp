import unittest
import importlib
import sys
import io
from contextlib import redirect_stdout

class TestLogger(unittest.TestCase):
    def test_log_message_format(self):
        """Test formatting of log message."""
        try:
            import starter_code
        except ImportError:
            self.fail("Could not import starter_code")
        
        msg = starter_code.log_message("INFO", "Test")
        # Check format somewhat loosely to handle timestamp variants
        self.assertIn("[INFO] Test", msg)
        self.assertIn("[", msg)
        self.assertIn("]", msg)

    def test_no_side_effects_on_import(self):
        """Test that importing the module produces NO output."""
        # Unload module if present
        if 'starter_code' in sys.modules:
            del sys.modules['starter_code']
        
        # Capture stdout during import
        f = io.StringIO()
        with redirect_stdout(f):
            import starter_code
        
        output = f.getvalue()
        self.assertEqual(output, "", "Module printed output during import! Did you forget the main guard?")

if __name__ == '__main__':
    unittest.main()
