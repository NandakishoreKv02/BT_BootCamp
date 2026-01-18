import unittest
import starter_code

class TestDispatch(unittest.TestCase):
    def test_availability_toggle(self):
        amb = starter_code.Ambulance("A1")
        self.assertTrue(amb.is_available)
        amb.assign_mission()
        self.assertFalse(amb.is_available)
        
    def test_routing_logic(self):
        fleet = [starter_code.Ambulance("A1")]
        d = starter_code.Dispatcher(fleet)
        
        # First call success
        msg1 = d.dispatch_to_emergency("Loc X")
        self.assertIn("A1", msg1)
        
        # Second call fail
        msg2 = d.dispatch_to_emergency("Loc Y")
        self.assertIn("No units", msg2)

if __name__ == "__main__":
    unittest.main()
