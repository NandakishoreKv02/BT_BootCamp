"""Lab 3: Patient Appointment Scheduler - Starter"""
import json

def create_schedule():
    # TODO: Return empty dict
    return {}

def is_slot_available(schedule, time):
    # TODO: Check if time slot is available
    return time not in schedule or schedule[time] is None

def book_appointment(schedule, time, patient_name):
    # TODO: Book appointment if available
    if is_slot_available(schedule, time):
        schedule[time] = patient_name
        return True
    return False

def cancel_appointment(schedule, time):
    # TODO: Cancel appointment
    if time in schedule:
        schedule[time] = None

def display_schedule(schedule):
    # TODO: Display formatted schedule
    print("\n=== Appointment Schedule ===")
    for time, patient in sorted(schedule.items()):
        status = patient if patient else "[Available]"
        print(f"{time}: {status}")
    print("===========================\n")

def save_schedule(schedule, filename):
    # TODO: Save to file
    try:
        with open(filename, 'w') as f:
            json.dump(schedule, f)
    except Exception as e:
        print(f"Error saving schedule: {e}")

def load_schedule(filename):
    # TODO: Load from file
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error loading schedule: {e}")
        return {}

if __name__ == "__main__":
    schedule = create_schedule()
    book_appointment(schedule, "09:00", "John Doe")
    display_schedule(schedule)
