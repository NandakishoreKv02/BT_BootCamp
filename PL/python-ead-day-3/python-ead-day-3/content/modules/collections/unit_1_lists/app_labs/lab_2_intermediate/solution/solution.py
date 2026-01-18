"""
Lab 2 (Intermediate): Appointment Scheduling - Part 2
Solution Code

Module: Collections - Unit 1: Lists
"""

def cancel_appointment(schedule, appointment_string):
    """Remove an appointment from the schedule."""
    if appointment_string in schedule:
        schedule.remove(appointment_string)
        return True
    return False


def organize_schedule(schedule):
    """Sort the schedule chronologically in-place."""
    schedule.sort()
    return schedule


def get_morning_appointments(schedule):
    """Get all appointments before 12:00."""
    morning = []
    # Can also be done with slicing if sorted:
    # return [slot for slot in schedule if slot < "12:00"]
    for slot in schedule:
        # String comparison works for ISO time "09:00" < "12:00"
        if slot[:5] < "12:00":
            morning.append(slot)
    return morning


def find_patient_slot(schedule, patient_name):
    """Find appointment string for a patient name."""
    for slot in schedule:
        if patient_name in slot:
            return slot
    return None
