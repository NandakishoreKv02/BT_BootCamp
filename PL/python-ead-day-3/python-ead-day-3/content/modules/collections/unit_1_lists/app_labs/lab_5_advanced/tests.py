import unittest

class TestAudit(unittest.TestCase):
    def test_search(self):
        from starter_code import alice_count, emergency_index, is_john_present, second_emergency_index
        self.assertEqual(alice_count, 2)
        self.assertEqual(emergency_index, 2)
        self.assertFalse(is_john_present)
        self.assertEqual(second_emergency_index, 5)

if __name__ == "__main__":
    unittest.main()
