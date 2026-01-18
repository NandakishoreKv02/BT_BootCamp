import unittest
import starter_code

class TestScalableWard(unittest.TestCase):
    def setUp(self):
        self.policy_map = {
            "General": starter_code.general_policy,
            "ICU": starter_code.icu_policy,
            "Peds": starter_code.peds_policy
        }

    def test_icu_policy(self):
        w = {"type": "ICU", "total": 10, "occupied": 0}
        p_high = {"priority": "High", "age": 40}
        p_low = {"priority": "Low", "age": 40}
        
        # We test the logic function directly if implemented, 
        # but the engine is usually what the student uses.
        res = starter_code.admit_to_ward(w, p_high, self.policy_map)
        self.assertTrue(res)
        
        res_fail = starter_code.admit_to_ward(w, p_low, self.policy_map)
        self.assertFalse(res_fail)

    def test_peds_policy(self):
        w = {"type": "Peds", "total": 10, "occupied": 0}
        p_child = {"age": 5}
        p_adult = {"age": 50}
        
        self.assertTrue(starter_code.admit_to_ward(w, p_child, self.policy_map))
        self.assertFalse(starter_code.admit_to_ward(w, p_adult, self.policy_map))

if __name__ == "__main__":
    unittest.main()
