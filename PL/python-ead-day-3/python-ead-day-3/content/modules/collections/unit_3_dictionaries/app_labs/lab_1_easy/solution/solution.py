"""
Lab 1 (Easy): Patient Records Management - Part 1
Solution Code

Module: Collections - Unit 3: Dictionaries
"""

def initialize_database():
    """
    Initialize the patient database with default records.
    
    Returns:
        dict: A dictionary containing at least 2 default patient records.
    """
    db = {
        101: {"name": "John Doe", "age": 30, "blood_type": "A+"},
        102: {"name": "Jane Smith", "age": 25, "blood_type": "O-"}
    }
    return db


def add_patient(db, patient_id, name, age, blood_type):
    """
    Add a new patient to the database.
    
    Args:
        db (dict): The patient database
        patient_id (int): Unique ID
        name (str): Patient name
        age (int): Patient age
        blood_type (str): Patient blood type
        
    Returns:
        bool: True if added successfully
    """
    # Create the patient record
    record = {
        "name": name,
        "age": age,
        "blood_type": blood_type
    }
    
    # Add to database using ID as key
    db[patient_id] = record
    
    return True


def get_patient_details(db, patient_id):
    """
    Retrieve patient details by ID safely.
    
    Args:
        db (dict): The patient database
        patient_id (int): ID to look up
        
    Returns:
        dict or None: Patient record if found, else None
    """
    # Use .get() method to safely retrieve value
    # Returns None if key is missing (default behavior of get without 2nd arg)
    return db.get(patient_id)


def update_patient_age(db, patient_id, new_age):
    """
    Update the age of an existing patient.
    
    Args:
        db (dict): The patient database
        patient_id (int): ID to look up
        new_age (int): New age value
        
    Returns:
        bool: True if updated, False if patient not found
    """
    # Check if patient exists
    if patient_id in db:
        # Access the nested dictionary and update age
        db[patient_id]["age"] = new_age
        return True
    else:
        return False


# ============================================================================
# Manual Testing Section
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Lab 1 Solution Verification")
    print("=" * 80)
    
    # 1. Initialize
    db = initialize_database()
    print(f"Initialized with {len(db)} records.")
    
    # 2. Add
    add_patient(db, 103, "Sam Brown", 45, "B+")
    print("Added Patient 103.")
    
    # 3. Lookup
    p103 = get_patient_details(db, 103)
    print(f"Retrieved 103: {p103}")
    
    # 4. Update
    success = update_patient_age(db, 103, 46)
    print(f"Updated 103 age (success={success}). New age: {db[103]['age']}")
    
    print("=" * 80)
