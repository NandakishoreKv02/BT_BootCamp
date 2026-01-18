import unittest
from starter_code import MedGuardSystem, SystemConfig

class TestLab6(unittest.TestCase):
    def test_singleton_availability(self):
        sys = MedGuardSystem()
        self.assertEqual(sys.config.threshold, 120)

    def test_integration_logic(self):
        # We test that the orchestrator correctly uses strategies and notifications
        # This usually requires mocks, but for this lab we check state
        app = MedGuardSystem()
        app.enroll_patient("Alice", "A") # Adult
        self.assertIn("Alice", app.patients)

if __name__ == '__main__':
    unittest.main()
