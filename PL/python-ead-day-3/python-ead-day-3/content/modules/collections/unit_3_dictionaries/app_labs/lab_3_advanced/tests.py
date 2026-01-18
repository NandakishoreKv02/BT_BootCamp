import unittest
from starter_code import merge_datasets, validate_records, search_patients, get_blood_type_distribution

class TestAnalytics(unittest.TestCase):
    
    def test_task_1_merge(self):
        """Test safe merging logic."""
        main = {1: "A", 2: "B"}
        archive = {2: "Overwrote?", 3: "C"}
        
        conflicts = merge_datasets(main, archive)
        
        self.assertEqual(len(main), 3, "Should have 3 records total")
        self.assertEqual(main[1], "A")
        self.assertEqual(main[2], "B", "Should preserve main record")
        self.assertEqual(main[3], "C", "Should add missing record")
        self.assertEqual(conflicts, [2], "Should report conflict ID")

    def test_task_2_validation(self):
        """Test schema validation."""
        db = {
            1: {"name": "A", "age": 20, "blood_type": "O+"}, # Valid
            2: {"name": "B", "age": 20}, # Missing blood_type
            3: {"name": "C", "age": 20, "blood_type": "A-"} # Valid
        }
        
        valid_count, invalid_count = validate_records(db)
        
        self.assertEqual(valid_count, 2)
        self.assertEqual(invalid_count, 1)
        self.assertEqual(db[2]["status"], "incomplete")
        self.assertEqual(db[1].get("status"), "active", "Should default to active")

    def test_task_3_search(self):
        """Test multi-criteria search."""
        db = {
            1: {"name": "Alice", "age": 30, "blood_type": "A+"},
            2: {"name": "Bob", "age": 60, "blood_type": "O+"},
            3: {"name": "Charlie", "age": 70, "blood_type": "AB+"},
            4: {"name": "Dave", "age": 25, "blood_type": "O+"}
        }
        
        # Criteria: O+ AND Age >= 50
        results = search_patients(db, {"blood_type": "O+", "min_age": 50})
        self.assertEqual(results, [2], "Should match Bob only")
        
        # Criteria: Name contains 'li'
        res_name = search_patients(db, {"name_contains": "li"})
        self.assertIn(1, res_name) # Alice
        self.assertIn(3, res_name) # Charlie
        
        # Criteria: Empty (should result all? or none? Logic usually assumes match all filters, empty=match all)
        # We'll assert behavior based on standard implementation
        # But advanced task implies filters. Let's assume matches all.
        res_all = search_patients(db, {})
        self.assertEqual(len(res_all), 4)

    def test_task_4_demographics(self):
        """Test aggregation."""
        db = {
            1: {"blood_type": "A+", "status": "active"},
            2: {"blood_type": "A+", "status": "active"},
            3: {"blood_type": "B-", "status": "active"},
            4: {"blood_type": "A+", "status": "incomplete"} # Should ignore
        }
        
        stats = get_blood_type_distribution(db)
        self.assertEqual(stats["A+"], 2, "Should count 2 valid A+")
        self.assertEqual(stats["B-"], 1)
        self.assertNotIn("O", stats)

if __name__ == '__main__':
    unittest.main()
