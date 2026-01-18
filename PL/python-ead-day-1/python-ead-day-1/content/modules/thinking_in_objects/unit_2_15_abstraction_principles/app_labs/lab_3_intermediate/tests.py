import unittest
from starter_code import PatientProfile, CostCalculator, StatementRenderer

class TestSRP(unittest.TestCase):
    def test_calculator_logic(self):
        calc = CostCalculator()
        res = calc.calculate([{"price": 10}, {"price": 20}])
        self.assertEqual(res, 30)
        
    def test_renderer_output(self):
        p = PatientProfile("John", [])
        render = StatementRenderer()
        out = render.render(p, 100)
        self.assertIn("John", out)
        self.assertIn("$100", out)

if __name__ == "__main__":
    unittest.main()
