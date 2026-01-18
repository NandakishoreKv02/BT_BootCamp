import unittest
from starter_code import initialize_database, add_patient, get_patient_details, update_patient_age

class TestPatientRecords(unittest.TestCase):
    
    def setUp(self):
        """Run before each test to start with a fresh DB."""
        self.db = initialize_database()
        if not isinstance(self.db, dict):
            self.db = {} # Fallback if init is not implemented yet

    def test_task_1_initialize(self):
        """Task 1: Initialize database"""
        db = initialize_database()
        self.assertIsInstance(db, dict, "Database should be a dictionary")
        self.assertTrue(len(db) >= 2, "Database should have at least 2 default records")
        # Check structure of values
        first_key = list(db.keys())[0]
        self.assertIsInstance(db[first_key], dict, "Values should be dictionaries")
        self.assertIn("name", db[first_key], "Record should have 'name'")
        self.assertIn("age", db[first_key], "Record should have 'age'")
        self.assertIn("blood_type", db[first_key], "Record should have 'blood_type'")

    def test_task_2_add_patient(self):
        """Task 2: Add patient"""
        # Test basic add
        result = add_patient(self.db, 301, "Test User", 25, "O+")
        self.assertTrue(result, "add_patient should return True")
        self.assertIn(301, self.db, "Patient ID 301 should be in db")
        self.assertEqual(self.db[301]["name"], "Test User")
        
        # Test overwriting (standard dict behavior)
        add_patient(self.db, 301, "UpdatedUser", 26, "O+")
        self.assertEqual(self.db[301]["name"], "UpdatedUser", "Should overwrite existing ID")

    def test_task_3_get_patient(self):
        """Task 3: Safe lookup"""
        # Add a known patient
        self.db[401] = {"name": "Lookup Me", "age": 40, "blood_type": "A-"}
        
        # Test success
        result = get_patient_details(self.db, 401)
        self.assertEqual(result["name"], "Lookup Me")
        
        # Test failure (missing ID)
        result_missing = get_patient_details(self.db, 9999)
        self.assertIsNone(result_missing, "Should return None for missing ID")

    def test_task_4_update_age(self):
        """Task 4: Update age"""
        # Add a known patient
        self.db[501] = {"name": "Update Me", "age": 50, "blood_type": "AB+"}
        
        # Test success
        result = update_patient_age(self.db, 501, 51)
        self.assertTrue(result, "Should return True on success")
        self.assertEqual(self.db[501]["age"], 51, "Age should be updated to 51")
        self.assertEqual(self.db[501]["name"], "Update Me", "Name should remain unchanged")
        
        # Test failure (missing patient)
        result_missing = update_patient_age(self.db, 8888, 20)
        self.assertFalse(result_missing, "Should return False for missing patient")

if __name__ == '__main__':
    print("Running tests for Lab 1...")
    unittest.main()
