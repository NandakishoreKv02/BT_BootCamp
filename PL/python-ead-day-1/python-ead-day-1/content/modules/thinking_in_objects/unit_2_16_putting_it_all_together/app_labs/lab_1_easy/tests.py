import unittest
import starter_code

class TestRefactoring(unittest.TestCase):
    def test_class_behavior(self):
        wr = starter_code.WaitingRoom()
        wr.check_in("Alice", "10:00")
        self.assertEqual(wr.get_wait_time("Alice"), "10:00")
        self.assertEqual(wr.get_wait_time("Bob"), -1)
        
    def test_encapsulation(self):
        # Ensure we aren't using the global lists from the starter
        wr = starter_code.WaitingRoom()
        wr.check_in("Charlie", "11:00")
        self.assertNotIn("Charlie", starter_code.p_names)

if __name__ == "__main__":
    unittest.main()
