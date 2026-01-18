import unittest
import starter_code

class TestConfigManager(unittest.TestCase):
    def test_prod_env(self):
        c = starter_code.make_config("prod")
        self.assertEqual(c['secure'], True)
        self.assertIn("hospital.com", c['url'])

    def test_test_env(self):
        c = starter_code.make_config("test")
        self.assertEqual(c['secure'], False)
        self.assertEqual(c['url'], "http://localhost:8080")

    def test_connection_string(self):
        c = starter_code.make_config("prod")
        info = starter_code.get_connection_info(c)
        self.assertIn("City General", info)
        self.assertIn("hospital.com", info)

if __name__ == "__main__":
    unittest.main()
