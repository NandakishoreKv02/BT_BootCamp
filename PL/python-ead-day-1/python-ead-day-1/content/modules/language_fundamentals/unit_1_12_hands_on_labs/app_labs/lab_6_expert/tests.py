import unittest
import starter_code

class TestEHRSystem(unittest.TestCase):
    def setUp(self):
        starter_code.ehr_data = {"patients": [], "appointments": [], "medications": []}

    def test_add_patient(self):
        success, msg = starter_code.add_patient("MRN001", "Test", 30, "Flu")
        self.assertTrue(success)

    def test_schedule_appointment(self):
        starter_code.add_patient("MRN001", "Test", 30, "Flu")
        success, msg = starter_code.schedule_appointment("MRN001", "2024-01-15", "10:00")
        self.assertTrue(success)

    def test_prescribe_medication(self):
        starter_code.add_patient("MRN001", "Test", 30, "Flu")
        success, msg = starter_code.prescribe_medication("MRN001", "Aspirin", "500mg")
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
