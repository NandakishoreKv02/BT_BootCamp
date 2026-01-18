import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestDataParser(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_basic_parsing(self):
        res = starter_code.parse_patient_data("101", "30", "75.5", "No")
        self.assertIsInstance(res['id'], int)
        self.assertIsInstance(res['age'], int)
        self.assertIsInstance(res['weight'], float)
        self.assertIsInstance(res['is_smoker'], bool)
        
        self.assertEqual(res['id'], 101)
        self.assertEqual(res['weight'], 75.5)
        self.assertFalse(res['is_smoker'])

    def test_whitespace_handling(self):
        res = starter_code.parse_patient_data("  202  ", " 40 ", " 80.0 ", "Yes")
        self.assertEqual(res['id'], 202)
        self.assertEqual(res['age'], 40)
        self.assertTrue(res['is_smoker'])

    def test_boolean_logic(self):
        self.assertTrue(starter_code.parse_patient_data("","","","Yes")['is_smoker'])
        self.assertTrue(starter_code.parse_patient_data("","","","true")['is_smoker'])
        self.assertFalse(starter_code.parse_patient_data("","","","No")['is_smoker'])
        self.assertFalse(starter_code.parse_patient_data("","","","AnythingElse")['is_smoker'])

if __name__ == '__main__':
    unittest.main()
