"""
Lab 2 (Intermediate): Doctor Schedule Management
Solution Code

Module: Collections - Unit 3: Dictionaries
"""

def register_doctor(db, doc_id, name, specialty):
    """Register a new doctor with an empty schedule."""
    # Create nested structure
    db[doc_id] = {
        "name": name,
        "specialty": specialty,
        "schedule": {} 
    }
    return True


def add_availability(db, doc_id, date):
    """Initialize a date in the doctor's schedule."""
    if doc_id not in db:
        return False
        
    # Define empty slots
    slots = {
        "09:00": None,
        "10:00": None,
        "11:00": None,
        "14:00": None
    }
    
    # Assign to nested dictionary key
    db[doc_id]["schedule"][date] = slots
    return True


def book_appointment(db, doc_id, date, time, patient_id):
    """Book a patient into a specific slot if available."""
    # Validate entire path existence before access
    if doc_id not in db:
        return False
        
    schedule = db[doc_id]["schedule"]
    if date not in schedule:
        return False
        
    day_slots = schedule[date]
    if time not in day_slots:
        return False
        
    # Check availability
    if day_slots[time] is not None:
        return False  # Already booked
        
    # Book it
    day_slots[time] = patient_id
    return True


def find_doctors_by_specialty(db, specialty):
    """Return list of doctor names matching the specialty."""
    matching_names = []
    
    # Iterate through keys/values
    for doc_id, info in db.items():
        if info["specialty"] == specialty:
            matching_names.append(info["name"])
            
    return matching_names


def get_doctor_workload(db, doc_id):
    """Count total number of patients assigned to a doctor."""
    if doc_id not in db:
        return None
        
    count = 0
    schedule = db[doc_id]["schedule"]
    
    # Iterate through all dates
    for date, day_slots in schedule.items():
        # Iterate through all times in that day
        for time, patient in day_slots.items():
            if patient is not None:
                count += 1
                
    return count
