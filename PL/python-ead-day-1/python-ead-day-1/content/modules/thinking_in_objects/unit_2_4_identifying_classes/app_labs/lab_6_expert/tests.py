import unittest
import starter_code

class TestClinicalWorkflow(unittest.TestCase):
    def test_workflow_logic(self):
        p = starter_code.Patient("Tony")
        pr = starter_code.Procedure("Appendectomy", 5000)
        room = starter_code.OperatingRoom("OR5")
        ctrl = starter_code.SurgeryController()
        
        # Test Scheduling
        ctrl.schedule_surgery(p, pr, room)
        self.assertTrue(room.is_reserved)
        
        # Test Billing failure (before check-in)
        claim1 = ctrl.generate_billing(p, pr)
        self.assertIsNone(claim1)
        
        # Test Billing success (after check-in)
        p.is_checked_in = True
        claim2 = ctrl.generate_billing(p, pr)
        self.assertIsNotNone(claim2)
        self.assertEqual(claim2.cost, 5000)

if __name__ == "__main__":
    unittest.main()
