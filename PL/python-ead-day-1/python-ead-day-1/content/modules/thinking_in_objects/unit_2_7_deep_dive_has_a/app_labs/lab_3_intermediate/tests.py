import unittest
import starter_code

class TestBidirectionalLink(unittest.TestCase):
    def test_link_sync(self):
        dr = starter_code.Doctor("Smith")
        p = starter_code.Patient("John")
        dr.add_patient(p)
        
        # Test Doctor -> Patient
        self.assertIn(p, dr.patients)
        # Test Patient -> Doctor (Bidirectional)
        self.assertEqual(p.doctor, dr)

if __name__ == "__main__":
    unittest.main()
