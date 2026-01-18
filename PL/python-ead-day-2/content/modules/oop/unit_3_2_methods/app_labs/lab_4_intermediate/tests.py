import unittest
from starter_code import Patient

class TestFactories(unittest.TestCase):
    def test_from_string(self):
        p = Patient.from_string("Michael-55")
        self.assertEqual(p.name, "Michael")
        self.assertEqual(p.age, 55)

    def test_from_dict(self):
        p = Patient.from_dict({"name": "Sara", "age": 22})
        self.assertEqual(p.name, "Sara")
        self.assertEqual(p.age, 22)

if __name__ == "__main__":
    unittest.main()
