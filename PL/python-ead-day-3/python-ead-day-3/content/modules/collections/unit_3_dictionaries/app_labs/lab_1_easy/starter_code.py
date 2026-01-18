"""
Lab 1 (Easy): Patient Records Management - Part 1
Starter Code with TODO markers

Module: Collections - Unit 3: Dictionaries
"""

def initialize_database():
    """
    Initialize the patient database with default records.
    
    Returns:
        dict: A dictionary containing at least 2 default patient records.
              Key: patient_id (int)
              Value: dict {"name": str, "age": int, "blood_type": str}
    """
    # TODO: Create a dictionary with a few dummy records
    pass


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
    # TODO: Create a dictionary for the patient details
    # TODO: Add it to the db using patient_id as key
    # TODO: Return True
    pass


def get_patient_details(db, patient_id):
    """
    Retrieve patient details by ID safely.
    
    Args:
        db (dict): The patient database
        patient_id (int): ID to look up
        
    Returns:
        dict or None: Patient record if found, else None
    """
    # TODO: Use .get() to retrieve the record safely
    pass


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
    # TODO: Check if patient_id exists in db
    # TODO: If yes, update the 'age' field and return True
    # TODO: If no, return False
    pass


# ============================================================================
# Manual Testing Section
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Lab 1 (Easy): Patient Records Management")
    print("=" * 80)
    
    # 1. Initialize
    print("\n[Task 1] Initializing Database...")
    patients_db = initialize_database()
    print(f"Database: {patients_db}")
    
    # 2. Add
    print("\n[Task 2] Adding Patient 103...")
    success = add_patient(patients_db, 103, "Sam Brown", 45, "B+")
    print(f"Added: {success}")
    print(f"Database: {patients_db}")
    
    # 3. Lookup
    print("\n[Task 3] Looking up Patient 103...")
    record = get_patient_details(patients_db, 103)
    print(f"Found: {record}")
    
    print("Looking up missing Patient 999...")
    missing = get_patient_details(patients_db, 999)
    print(f"Found: {missing}")
    
    # 4. Update
    print("\n[Task 4] Updating Patient 103 Age to 46...")
    updated = update_patient_age(patients_db, 103, 46)
    print(f"Updated: {updated}")
    print(f"New Record: {patients_db.get(103)}")
    
    print("\n" + "=" * 80)
    print("Run tests.py to verify your solution!")
    print("=" * 80)
