import unittest
from starter_code import (
    Scanner, MRIScanner, CTScanner, UltrasoundScanner,
    ImagingOrder, CostEstimator, ReportGenerator, DiagnosticWorkflow
)

class TestEnterpriseDiagnostic(unittest.TestCase):
    def test_scanner_abstraction(self):
        mri = MRIScanner()
        self.assertTrue(isinstance(mri, Scanner))
        self.assertEqual(mri.get_cost(), 1200)
        
    def test_cost_estimator_srp(self):
        ce = CostEstimator()
        scanner = CTScanner()
        self.assertEqual(ce.estimate(scanner), 800)
        
    def test_workflow_integration(self):
        order = ImagingOrder(1001, "P-555", "MRI")
        wf = DiagnosticWorkflow()
        report = wf.execute_scan(order)
        self.assertIn("P-555", report)
        self.assertIn("1200", report)

if __name__ == "__main__":
    unittest.main()
