import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestERQueue(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.queue = []

    def test_workflow(self):
        starter_code.arrive_patient(self.queue, "A")
        starter_code.arrive_patient(self.queue, "B")
        self.assertEqual(starter_code.get_queue_length(self.queue), 2)
        
        patient = starter_code.see_next_patient(self.queue)
        self.assertEqual(patient, "A")
        self.assertEqual(starter_code.get_queue_length(self.queue), 1)

    def test_empty_behavior(self):
        self.assertIsNone(starter_code.see_next_patient(self.queue))
        self.assertEqual(starter_code.get_queue_length(self.queue), 0)

if __name__ == '__main__':
    unittest.main()
