import unittest
from starter_code import Doctor, Administrator, ChiefMedicalOfficer

class TestLab4(unittest.TestCase):
    def test_parents(self):
        d = Doctor()
        a = Administrator()
        self.assertEqual(d.work(), "Treating patient")
        self.assertEqual(a.work(), "Doing paperwork")

    def test_cmo_inheritance(self):
        cmo = ChiefMedicalOfficer()
        self.assertTrue(isinstance(cmo, Doctor))
        self.assertTrue(isinstance(cmo, Administrator))

    def test_cmo_work(self):
        cmo = ChiefMedicalOfficer()
        result = cmo.work()
        self.assertIn("Treating patient", result)
        self.assertIn("Doing paperwork", result)
        self.assertIn("AND", result)

    def test_mro(self):
        mro = ChiefMedicalOfficer.mro()
        # Ensure Doctor comes before Administrator
        self.assertTrue(mro.index(Doctor) < mro.index(Administrator))

if __name__ == '__main__':
    unittest.main()
