import unittest
import starter_code

class TestUltimateScheduler(unittest.TestCase):
    def setUp(self):
        starter_code.master_schedule = []

    def test_workflow(self):
        starter_code.add_appointment("Alice", "10:00", "Smith")
        starter_code.add_appointment("Bob", "08:00", "Smith")
        starter_code.add_appointment("Charlie", "09:00", "Jones")
        
        self.assertEqual(len(starter_code.master_schedule), 3)
        
        starter_code.sort_schedule()
        self.assertEqual(starter_code.master_schedule[0]["name"], "Bob") # 08:00
        
        smith_queue = starter_code.get_dr_queue("Smith")
        self.assertEqual(len(smith_queue), 2)
        
        served = starter_code.serve_patient(0) # Serve Bob
        self.assertEqual(served["name"], "Bob")
        self.assertEqual(len(starter_code.master_schedule), 2)

if __name__ == "__main__":
    unittest.main()
