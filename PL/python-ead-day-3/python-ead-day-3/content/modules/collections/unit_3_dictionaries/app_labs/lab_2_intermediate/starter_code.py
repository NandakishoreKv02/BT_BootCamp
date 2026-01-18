"""
Lab 2 (Intermediate): Doctor Schedule Management
Starter Code with TODO markers

Module: Collections - Unit 3: Dictionaries
"""

def register_doctor(db, doc_id, name, specialty):
    """
    Register a new doctor with an empty schedule.
    
    Args:
        db (dict): The main database
        doc_id (int): Unique Doctor ID
        name (str): Doctor's name
        specialty (str): Medical specialty
        
    Returns:
        bool: True if registered successfully
    """
    # TODO: Add doctor to db with schema:
    # { "name": name, "specialty": specialty, "schedule": {} }
    pass


def add_availability(db, doc_id, date):
    """
    Initialize a date in the doctor's schedule with 4 empty slots.
    Slots: "09:00", "10:00", "11:00", "14:00"
    
    Args:
        db (dict): The main database
        doc_id (int): Doctor ID
        date (str): Date string (e.g., "2023-10-27")
        
    Returns:
        bool: True if successful, False if doctor not found
    """
    # TODO: Check if doc_id exists
    # TODO: Initialize db[doc_id]["schedule"][date] with the 4 time slots set to None
    pass


def book_appointment(db, doc_id, date, time, patient_id):
    """
    Book a patient into a specific slot if available.
    
    Args:
        db (dict): The main database
        doc_id (int): Doctor ID
        date (str): Date
        time (str): Time slot
        patient_id (int): Patient ID
        
    Returns:
        bool: True if booked, False if failed (not found or taken)
    """
    # TODO: Navigate nested dicts to find the slot
    # TODO: Check if slot is None (empty)
    # TODO: If empty, assign patient_id and return True
    pass


def find_doctors_by_specialty(db, specialty):
    """
    Return list of doctor names matching the specialty.
    
    Args:
        db (dict): The main database
        specialty (str): Specialty to search for
        
    Returns:
        list: List of doctor names (strings)
    """
    # TODO: Iterate over db and filter by specialty
    pass


def get_doctor_workload(db, doc_id):
    """
    Count total number of patients assigned to a doctor.
    
    Args:
        db (dict): The main database
        doc_id (int): Doctor ID
        
    Returns:
        int: Total appointment count (or None if doctor missing)
    """
    # TODO: Iterate through doctor's schedule (dates -> times)
    # TODO: Count non-None values
    pass


# ============================================================================
# Manual Testing Section
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Lab 2 (Intermediate): Doctor Schedule Management")
    print("=" * 80)
    
    # Initialize DB
    hospital_db = {}
    
    # 1. Register
    print("\n[Task 1] Registering Doctors...")
    register_doctor(hospital_db, 101, "Dr. House", "Diagnostic")
    register_doctor(hospital_db, 102, "Dr. Wilson", "Oncology")
    register_doctor(hospital_db, 103, "Dr. Cuddy", "Diagnostic")
    print(f"DB Keys: {list(hospital_db.keys())}")
    
    # 2. Add Availability
    print("\n[Task 2] Adding Availability...")
    success = add_availability(hospital_db, 101, "2023-11-01")
    print(f"Added slots for Dr. House: {success}")
    # print(hospital_db[101]["schedule"]) # Uncomment to peek
    
    # 3. Book Appointment
    print("\n[Task 3] Booking Appointment...")
    booked = book_appointment(hospital_db, 101, "2023-11-01", "09:00", 5001)
    print(f"Booked Patient 5001: {booked}")
    
    fail_book = book_appointment(hospital_db, 101, "2023-11-01", "09:00", 5002) # Should fail
    print(f"Booked Patient 5002 (should fail): {fail_book}")
    
    # 4. Filter
    print("\n[Task 4] Finding Diagnostic Doctors...")
    diag_docs = find_doctors_by_specialty(hospital_db, "Diagnostic")
    print(f"Diagnostic Docs: {diag_docs}")
    
    # 5. Workload
    print("\n[Task 5] Checking Workload...")
    # Add another booking
    book_appointment(hospital_db, 101, "2023-11-01", "10:00", 5003)
    count = get_doctor_workload(hospital_db, 101)
    print(f"Dr. House Workload: {count} patients")
    
    print("\n" + "=" * 80)
    print("Run tests.py to verify nested logic!")
    print("=" * 80)
