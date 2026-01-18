import unittest
from starter_code import process_waitlist, add_emergency, remove_duplicates, generate_numbered_report

class TestWaitlistManager(unittest.TestCase):
    
    def test_process(self):
        s = ["A"]
        w = ["B", "C"]
        process_waitlist(s, w)
        self.assertEqual(s, ["A", "B", "C"])
        self.assertEqual(w, [])
        
    def test_emergency(self):
        s = ["A", "B"]
        add_emergency(s, "URGENT")
        self.assertEqual(s, ["URGENT", "A", "B"])
        self.assertEqual(s[0], "URGENT")
        
    def test_dedup(self):
        s = ["A", "B", "A", "C", "B"]
        res = remove_duplicates(s)
        self.assertEqual(res, ["A", "B", "C"])
        
    def test_report(self):
        s = ["A", "B"]
        rep = generate_numbered_report(s)
        self.assertEqual(rep, ["Slot 1: A", "Slot 2: B"])

if __name__ == '__main__':
    unittest.main()
