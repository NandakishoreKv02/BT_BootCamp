import unittest
import starter_code

class TestPharmacyMethods(unittest.TestCase):
    def test_internal_call(self):
        rx = starter_code.Prescription("Aspirin", 50)
        rx.fulfill()
        self.assertEqual(rx.status, "Filled")

    def test_validation_failure(self):
        rx = starter_code.Prescription("Aspirin", 500)
        rx.fulfill()
        self.assertNotEqual(rx.status, "Filled")

if __name__ == "__main__":
    unittest.main()
