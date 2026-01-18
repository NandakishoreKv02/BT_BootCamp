import unittest
import starter_code

class TestPharmacy(unittest.TestCase):
    def setUp(self):
        self.p = starter_code.create_pharmacy()
        starter_code.add_medication(self.p, "DrugA", 10, 5)
        self.pat = starter_code.create_patient("Test", 20)

    def test_success(self):
        res = starter_code.dispense_medication(self.p, self.pat, "DrugA")
        self.assertTrue(res)
        self.assertEqual(self.pat['cash'], 10)
        self.assertIn("DrugA", self.pat['meds'])
        self.assertEqual(self.p['inventory']['DrugA']['stock'], 4)

    def test_broke(self):
        broke_pat = starter_code.create_patient("Broke", 5)
        res = starter_code.dispense_medication(self.p, broke_pat, "DrugA")
        self.assertFalse(res)

if __name__ == "__main__":
    unittest.main()
