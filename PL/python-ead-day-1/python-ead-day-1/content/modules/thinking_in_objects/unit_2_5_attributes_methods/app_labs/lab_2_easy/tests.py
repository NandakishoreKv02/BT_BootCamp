import unittest
import starter_code

class TestClassAttributes(unittest.TestCase):
    def test_counter_increments(self):
        # Reset counter
        starter_code.Admission.total_patients = 0
        a1 = starter_code.Admission("A")
        a2 = starter_code.Admission("B")
        self.assertEqual(starter_code.Admission.total_patients, 2)

    def test_shared_state(self):
        starter_code.Admission.total_patients = 0
        a = starter_code.Admission("X")
        self.assertEqual(a.total_patients, 1)

if __name__ == "__main__":
    unittest.main()
