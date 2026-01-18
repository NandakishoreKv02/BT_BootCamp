import unittest
import starter_code

class TestValidator(unittest.TestCase):
    def test_validator_flow(self):
        v = starter_code.make_validator()
        starter_code.add_rule(v, starter_code.check_mrn)
        
        p_bad = {'mrn': '12'}
        errors = starter_code.run_validation(v, p_bad)
        self.assertEqual(len(errors), 1)
        self.assertIn("MRN", errors[0])

    def test_multiple_rules(self):
        v = starter_code.make_validator()
        
        def dummy_rule(p): return "ErrorX"
        
        starter_code.add_rule(v, dummy_rule)
        starter_code.add_rule(v, dummy_rule)
        
        errors = starter_code.run_validation(v, {})
        self.assertEqual(len(errors), 2)

if __name__ == "__main__":
    unittest.main()
