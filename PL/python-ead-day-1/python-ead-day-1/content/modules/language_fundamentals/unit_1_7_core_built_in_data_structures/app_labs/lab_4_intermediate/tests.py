import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestEHRSystem(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.system = {}

    def test_add_and_get(self):
        starter_code.add_patient(self.system, "1", "Alice", "Stable")
        status = starter_code.get_patient_status(self.system, "1")
        self.assertEqual(status, "Stable")

    def test_missing_get(self):
        status = starter_code.get_patient_status(self.system, "999")
        self.assertEqual(status, "Not Found")

    def test_update(self):
        starter_code.add_patient(self.system, "2", "Bob", "Routine")
        success = starter_code.update_status(self.system, "2", "Urgent")
        self.assertTrue(success)
        self.assertEqual(self.system["2"]["status"], "Urgent")

    def test_update_missing(self):
        success = starter_code.update_status(self.system, "999", "Urgent")
        self.assertFalse(success)

if __name__ == '__main__':
    unittest.main()
