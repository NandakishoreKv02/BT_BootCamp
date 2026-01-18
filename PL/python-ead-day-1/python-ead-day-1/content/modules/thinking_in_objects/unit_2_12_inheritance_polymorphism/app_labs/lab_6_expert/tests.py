import unittest
import starter_code

class TestPolymorphicAggregation(unittest.TestCase):
    def test_logic_overrides(self):
        d = starter_code.DrugTherapy("Meds", 10)
        e = starter_code.ClinicalExercise("Walk", 30)
        
        self.assertEqual(d.get_intensity_score(), 20)
        self.assertEqual(e.get_intensity_score(), 15)
        
    def test_aggregation(self):
        plan = starter_code.CarePlan("Alice")
        plan.add_treatment(starter_code.DrugTherapy("A", 10))
        plan.add_treatment(starter_code.ClinicalExercise("B", 30))
        
        self.assertEqual(plan.total_intensity(), 35)

if __name__ == "__main__":
    unittest.main()
