import unittest
import starter_code

class TestCohesion(unittest.TestCase):
    def test_cohesive_report(self):
        report = starter_code.LabReport("999")
        report.add_result("Glucose", 150)
        self.assertEqual(report.results["Glucose"], 150)
        self.assertTrue(report.is_abnormal())

    def test_normal_result(self):
        report = starter_code.LabReport("999")
        report.add_result("Glucose", 90)
        self.assertFalse(report.is_abnormal())

if __name__ == "__main__":
    unittest.main()
