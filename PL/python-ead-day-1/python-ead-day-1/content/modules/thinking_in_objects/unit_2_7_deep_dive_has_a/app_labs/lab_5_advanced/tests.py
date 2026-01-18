import unittest
import starter_code

class TestManytoMany(unittest.TestCase):
    def test_double_sync(self):
        n = starter_code.Nurse("Joy")
        d = starter_code.Department("ICU")
        n.assign_to_department(d)
        
        # Check both directions
        self.assertIn(d, n.depts)
        self.assertIn(n, d.staff)

    def test_duplicate_prevention(self):
        n = starter_code.Nurse("Joy")
        d = starter_code.Department("ICU")
        n.assign_to_department(d)
        n.assign_to_department(d)
        
        self.assertEqual(len(n.depts), 1)
        self.assertEqual(len(d.staff), 1)

if __name__ == "__main__":
    unittest.main()
