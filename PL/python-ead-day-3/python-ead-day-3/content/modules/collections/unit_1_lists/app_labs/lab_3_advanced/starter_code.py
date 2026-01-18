"""
Lab 3 (Advanced): Appointment Scheduling - Part 3
Starter Code

Module: Collections - Unit 1: Lists
"""

def process_waitlist(schedule, waitlist):
    """
    Move all waitlist items to schedule and clear waitlist.
    
    Args:
        schedule (list): Active appointments
        waitlist (list): Waiting patients
        
    Returns:
        list: Updated schedule
    """
    # TODO: Extend schedule
    # TODO: Clear waitlist
    pass


def add_emergency(schedule, appointment):
    """
    Insert appointment at the front of the line.
    
    Args:
        schedule (list): Active appointments
        appointment (str): Emergency appointment
        
    Returns:
        list: Updated schedule
    """
    # TODO: Insert at index 0
    pass


def remove_duplicates(schedule):
    """
    Remove duplicate entries, keeping first occurrence.
    
    Args:
        schedule (list): List with duplicates
        
    Returns:
        list: New unique list
    """
    # TODO: Iterate and check seen items
    pass


def generate_numbered_report(schedule):
    """
    Create numbered report lines.
    
    Args:
        schedule (list): Appointments
        
    Returns:
        list: ["Slot 1: Appt1", "Slot 2: Appt2"...]
    """
    # TODO: Use list comprehension with enumerate
    pass


# ============================================================================
# Manual Testing
# ============================================================================

if __name__ == "__main__":
    print("="*60)
    print("Lab 3 (Advanced): Waitlist Manager")
    print("="*60)
    
    sched = ["10:00 - A"]
    wait = ["11:00 - B", "12:00 - C"]
    
    print(f"Start: {sched}, Wait: {wait}")
    
    # Process
    process_waitlist(sched, wait)
    print(f"Processed: {sched}, Wait(Cleared): {wait}")
    
    # Emergency
    add_emergency(sched, "09:00 - URGENT")
    print(f"Emergency: {sched}")
    
    # Duplicates
    dup_list = ["A", "B", "A", "C", "B"]
    uniq = remove_duplicates(dup_list)
    print(f"Unique: {uniq}")
    
    # Report
    rep = generate_numbered_report(sched)
    print(f"Report: {rep}")
