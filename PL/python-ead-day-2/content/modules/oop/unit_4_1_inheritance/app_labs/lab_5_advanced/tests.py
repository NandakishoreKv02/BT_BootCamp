import unittest
from abc import ABC
from starter_code import MedicalProcedure, Surgery, Checkup

class TestLab5(unittest.TestCase):
    def test_abc_properties(self):
        # Ensure it inherits from ABC
        self.assertTrue(issubclass(MedicalProcedure, ABC))
        # Ensure it cannot be instantiated
        with self.assertRaises(TypeError):
            m = MedicalProcedure()

    def test_surgery_implementation(self):
        s = Surgery()
        self.assertEqual(s.perform(), "Performing surgery")
        self.assertEqual(s.get_duration(), 60)
        self.assertTrue(isinstance(s, MedicalProcedure))

    def test_checkup_implementation(self):
        c = Checkup()
        self.assertEqual(c.perform(), "Performing checkup")
        self.assertEqual(c.get_duration(), 15)
        self.assertTrue(isinstance(c, MedicalProcedure))

    def test_incomplete_class_error(self):
        class Incomplete(MedicalProcedure):
            def perform(self): pass
            # Missing get_duration
        
        with self.assertRaises(TypeError):
            i = Incomplete()

if __name__ == '__main__':
    unittest.main()
