import unittest
from starter_code import MonitorRegistry, BaseMonitor, HeartMonitor

class TestLab6(unittest.TestCase):
    def test_registration(self):
        # HeartMonitor should be in the registry
        self.assertIn("HR_SCANNER", MonitorRegistry.plugins)
        self.assertEqual(MonitorRegistry.plugins["HR_SCANNER"], HeartMonitor)

    def test_validation_failure(self):
        # Define a class without ID inside a try block
        def create_bad_class():
            class BadMonitor(BaseMonitor):
                pass
        
        with self.assertRaises(TypeError):
            create_bad_class()

    def test_base_not_registered(self):
        # The base monitor itself shouldn't be in the registry keys
        self.assertNotIn("BaseMonitor", MonitorRegistry.plugins.values())

if __name__ == '__main__':
    unittest.main()
