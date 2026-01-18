import unittest
import starter_code

class TestNetworkModelling(unittest.TestCase):
    def test_bidirectional_aggregations(self):
        c1 = starter_code.Clinic("ClinicA")
        c2 = starter_code.Clinic("ClinicB")
        dr = starter_code.Specialist("Dr. Jones")
        
        c1.onboard_specialist(dr)
        c2.onboard_specialist(dr)
        
        # Specialist should have both clinics
        self.assertEqual(len(dr.clinics), 2)
        self.assertIn(c1, dr.clinics)
        self.assertIn(c2, dr.clinics)
        
        # Clinics should have the specialist
        self.assertIn(dr, c1.staff)
        self.assertIn(dr, c2.staff)

if __name__ == "__main__":
    unittest.main()
