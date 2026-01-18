import unittest
import starter_code

class TestPolymorphicLoop(unittest.TestCase):
    def test_overriding_logic(self):
        p = starter_code.PhysicalExam()
        l = starter_code.LabExam()
        
        self.assertNotEqual(p.generate_summary(), l.generate_summary())
        self.assertTrue(isinstance(p, starter_code.DiagnosticOutput))
        self.assertTrue(isinstance(l, starter_code.DiagnosticOutput))

if __name__ == "__main__":
    unittest.main()
