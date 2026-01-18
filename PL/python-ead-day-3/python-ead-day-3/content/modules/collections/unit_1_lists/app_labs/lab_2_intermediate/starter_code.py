"""
Lab 2 (Intermediate): Appointment Scheduling - Part 2
Starter Code

Module: Collections - Unit 1: Lists
"""

def cancel_appointment(schedule, appointment_string):
    """
    Remove an appointment from the schedule.
    
    Args:
        schedule (list): List of appointment strings
        appointment_string (str): Exact string to remove
        
    Returns:
        bool: True if removed, False if not found
    """
    # TODO: Check if exists, then remove
    pass


def organize_schedule(schedule):
    """
    Sort the schedule chronologically in-place.
    
    Args:
        schedule (list): List of appointment strings
        
    Returns:
        list: The sorted schedule (same object)
    """
    # TODO: Sort the list
    pass


def get_morning_appointments(schedule):
    """
    Get all appointments before 12:00.
    
    Args:
        schedule (list): List of appointment strings
        
    Returns:
        list: New list of morning appointments
    """
    # TODO: Filter items starting < "12:00"
    pass


def find_patient_slot(schedule, patient_name):
    """
    Find appointment string for a patient name.
    
    Args:
        schedule (list): List of appointment strings
        patient_name (str): Name to search for
        
    Returns:
        str: Full appointment string or None
    """
    # TODO: Search for substring match
    pass


# ============================================================================
# Manual Testing
# ============================================================================

if __name__ == "__main__":
    print("="*60)
    print("Lab 2 (Intermediate): Schedule Organizer")
    print("="*60)
    
    my_schedule = ["14:00 - Smith", "09:00 - Doe", "11:30 - Jones"]
    
    print(f"\nOriginal: {my_schedule}")
    
    # Organize
    organize_schedule(my_schedule)
    print(f"Sorted: {my_schedule}")
    
    # Cancel
    removed = cancel_appointment(my_schedule, "09:00 - Doe")
    print(f"Cancelled '09:00 - Doe': {removed}")
    print(f"Current: {my_schedule}")
    
    # Morning
    morning = get_morning_appointments(my_schedule)
    print(f"Morning: {morning}")
    
    # Find
    slot = find_patient_slot(my_schedule, "Smith")
    print(f"Smith is at: {slot}")
