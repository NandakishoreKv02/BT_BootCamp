import unittest
import starter_code

class TestTriageMapper(unittest.TestCase):
    def test_classes_exist(self):
        p = starter_code.PatientRecord("John", "Chest Pain")
        n = starter_code.TriageNurse("Nightingale")
        self.assertEqual(p.name, "John")
        self.assertEqual(n.nurse_name, "Nightingale")

    def test_verb_logic(self):
        n = starter_code.TriageNurse("Test")
        p_high = starter_code.PatientRecord("A", "Chest Pain")
        p_low = starter_code.PatientRecord("B", "Cough")
        
        self.assertEqual(n.calculate_urgency(p_high), 5)
        self.assertEqual(n.calculate_urgency(p_low), 2)

if __name__ == "__main__":
    unittest.main()
