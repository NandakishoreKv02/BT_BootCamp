import unittest
import starter_code

class TestOverriding(unittest.TestCase):
    def test_overrides(self):
        tool = starter_code.MedicalTool()
        scope = starter_code.Stethoscope()
        
        self.assertNotEqual(tool.use(), scope.use())
        self.assertIn("heart", scope.use().lower())

if __name__ == "__main__":
    unittest.main()
