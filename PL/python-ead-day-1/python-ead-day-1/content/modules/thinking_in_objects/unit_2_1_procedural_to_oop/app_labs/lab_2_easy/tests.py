import unittest
import starter_code

class TestLabResults(unittest.TestCase):
    def test_create(self):
        r = starter_code.create_lab_result("P99", "TestX", 100)
        self.assertEqual(r['pid'], "P99")
        self.assertEqual(r['value'], 100)

    def test_update(self):
        r = starter_code.create_lab_result("P99", "TestX", 100)
        starter_code.update_result(r, 200)
        self.assertEqual(r['value'], 200)

if __name__ == "__main__":
    unittest.main()
