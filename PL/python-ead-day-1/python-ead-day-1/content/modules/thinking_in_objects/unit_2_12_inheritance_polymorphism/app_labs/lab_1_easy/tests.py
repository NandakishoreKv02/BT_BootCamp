import unittest
import starter_code

class TestBasicInheritance(unittest.TestCase):
    def test_relationship(self):
        s = starter_code.StaffMember("Test", "ID")
        self.assertTrue(isinstance(s, starter_code.Person))
        self.assertEqual(s.name, "Test")
        self.assertEqual(s.employee_id, "ID")

if __name__ == "__main__":
    unittest.main()
