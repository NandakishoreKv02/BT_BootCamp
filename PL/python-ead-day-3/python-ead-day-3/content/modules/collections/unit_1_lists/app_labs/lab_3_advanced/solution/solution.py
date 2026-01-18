"""
Lab 3 (Advanced): Appointment Scheduling - Part 3
Solution Code

Module: Collections - Unit 1: Lists
"""

def process_waitlist(schedule, waitlist):
    """Move all waitlist items to schedule and clear waitlist."""
    schedule.extend(waitlist)
    waitlist.clear()
    return schedule


def add_emergency(schedule, appointment):
    """Insert appointment at the front of the line."""
    schedule.insert(0, appointment)
    return schedule


def remove_duplicates(schedule):
    """Remove duplicate entries, keeping first occurrence."""
    # Efficient logic for lists (since we don't know Sets yet in Unit 1 context)
    unique = []
    for item in schedule:
        if item not in unique:
            unique.append(item)
    return unique


def generate_numbered_report(schedule):
    """Create numbered report lines."""
    return [f"Slot {i+1}: {appt}" for i, appt in enumerate(schedule)]
