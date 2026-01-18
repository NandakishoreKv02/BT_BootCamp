import unittest

class TestFiltering(unittest.TestCase):
    def test_filter(self):
        from starter_code import dr_smith_list
        self.assertEqual(len(dr_smith_list), 2)
        for item in dr_smith_list:
            self.assertEqual(item["doctor"], "Smith")

if __name__ == "__main__":
    unittest.main()
