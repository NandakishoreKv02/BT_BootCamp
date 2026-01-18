import unittest
from starter_code import SystemConfig

class TestLab1(unittest.TestCase):
    def test_singleton_identity(self):
        c1 = SystemConfig()
        c2 = SystemConfig()
        self.assertIs(c1, c2, "SystemConfig must be a Singleton")

    def test_threshold_persistence(self):
        c1 = SystemConfig()
        c2 = SystemConfig()
        c1.set_threshold("oxygen_min", 92)
        self.assertEqual(c2.get_threshold("oxygen_min"), 92)

    def test_init_not_wiped(self):
        c1 = SystemConfig()
        c1.set_threshold("custom", 100)
        c2 = SystemConfig() # Triggers __init__ again
        self.assertEqual(c2.get_threshold("custom"), 100, "__init__ should not wipe existing data")

if __name__ == '__main__':
    unittest.main()
