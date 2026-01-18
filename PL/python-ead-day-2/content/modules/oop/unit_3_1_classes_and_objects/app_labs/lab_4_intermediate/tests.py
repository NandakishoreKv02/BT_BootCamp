import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

class TestWardManagement(unittest.TestCase):
    def test_list_contents(self):
        try:
            from starter_code import ward_census, Patient
            self.assertEqual(len(ward_census), 4)
            for p in ward_census:
                self.assertIsInstance(p, Patient)
        except ImportError:
            self.fail("ward_census or Patient not found")

    def test_report_generation(self):
        from starter_code import Patient, generate_report
        test_patients = [Patient("A", "B")]
        res = generate_report(test_patients)
        self.assertEqual(res[0], "NAME: A, CONDITION: B")

if __name__ == "__main__":
    unittest.main()
