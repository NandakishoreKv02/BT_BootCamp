import unittest
from starter_code import book_appointment, collect_payment, run_clinic_op, ClinicError, SchedulingError, BillingError

class TestLab3(unittest.TestCase):
    def test_scheduling_fail(self):
        msg = run_clinic_op(book_appointment, "Alice", "night")
        self.assertEqual(msg, "Doctors not available at night")

    def test_billing_fail(self):
        msg = run_clinic_op(collect_payment, -10)
        self.assertEqual(msg, "Invalid payment amount")

    def test_success(self):
        res = run_clinic_op(book_appointment, "Bob", "morning")
        self.assertEqual(res, "Appointment Confirmed")

    def test_hierarchy(self):
        # Verify inheritance
        self.assertTrue(issubclass(SchedulingError, ClinicError))
        self.assertTrue(issubclass(BillingError, ClinicError))

if __name__ == "__main__":
    unittest.main()
