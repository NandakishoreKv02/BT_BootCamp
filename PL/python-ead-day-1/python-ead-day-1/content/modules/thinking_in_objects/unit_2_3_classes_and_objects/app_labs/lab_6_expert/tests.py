import unittest
import starter_code

class TestBedInteractions(unittest.TestCase):
    def test_bidirectional_link(self):
        d = starter_code.Doctor("X")
        p = starter_code.Patient("Y", "1")
        
        starter_code.link_doctor_patient(d, p)
        
        # Check patient side
        self.assertEqual(p.doctor, d)
        # Check doctor side
        self.assertIn(p, d.patient_list)

    def test_summary(self):
        d = starter_code.Doctor("House")
        p = starter_code.Patient("John", "1")
        starter_code.link_doctor_patient(d, p)
        
        self.assertIn("House", d.get_summary())
        self.assertIn("1", d.get_summary())

if __name__ == "__main__":
    unittest.main()
