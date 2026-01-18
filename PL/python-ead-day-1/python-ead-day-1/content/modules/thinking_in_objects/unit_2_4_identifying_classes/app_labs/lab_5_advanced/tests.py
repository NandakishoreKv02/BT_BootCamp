import unittest
import starter_code

class TestBCEController(unittest.TestCase):
    def test_controller_validation(self):
        c = starter_code.RegistrationController()
        c.patients = []
        
        # Valid
        res1 = c.handle_registration("John", "1001")
        self.assertIsNotNone(res1)
        self.assertEqual(len(c.patients), 1)

        # Invalid
        res2 = c.handle_registration("Bad", "1")
        self.assertIsNone(res2)

    def test_ui_boundary(self):
        ui = starter_code.RegistrationUI()
        self.assertTrue(hasattr(ui, "show_message"))

if __name__ == "__main__":
    unittest.main()
