import unittest
import starter_code

class TestPatientManagement(unittest.TestCase):
    def setUp(self):
        self.patients = []

    def test_add_patient(self):
        result = starter_code.add_patient(self.patients, "MRN001", "Test", 30, "Flu")
        self.assertTrue(result)
        self.assertEqual(len(self.patients), 1)

    def test_find_patient(self):
        starter_code.add_patient(self.patients, "MRN001", "Test", 30, "Flu")
        patient = starter_code.find_patient_by_mrn(self.patients, "MRN001")
        self.assertIsNotNone(patient)
        self.assertEqual(patient["name"], "Test")

    def test_filter_by_age(self):
        starter_code.add_patient(self.patients, "MRN001", "Young", 25, "Flu")
        starter_code.add_patient(self.patients, "MRN002", "Old", 70, "Flu")
        filtered = starter_code.filter_by_age_range(self.patients, 20, 30)
        self.assertEqual(len(filtered), 1)

if __name__ == '__main__':
    unittest.main()
