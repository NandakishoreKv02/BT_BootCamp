import unittest
from starter_code import get_contact_info_pythonic

class TestLab1(unittest.TestCase):
    def test_found(self):
        data = {"email": "test@test.com"}
        self.assertEqual(get_contact_info_pythonic(data, "email"), "test@test.com")

    def test_not_found(self):
        data = {"phone": "123"}
        self.assertEqual(get_contact_info_pythonic(data, "email"), "Contact info not provided")

if __name__ == "__main__":
    unittest.main()
