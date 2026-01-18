import unittest
import starter_code

class TestInheritance(unittest.TestCase):
    def test_department_init(self):
        d = starter_code.Department("Lab", "Floor 1")
        self.assertEqual(d.name, "Lab")
        self.assertEqual(d.location, "Floor 1")

    def test_er_inheritance(self):
        er = starter_code.EmergencyDepartment("ER", "North")
        self.assertEqual(er.name, "ER")
        self.assertFalse(er.is_diverting)
        self.assertTrue(issubclass(starter_code.EmergencyDepartment, starter_code.Department))

if __name__ == "__main__":
    unittest.main()
