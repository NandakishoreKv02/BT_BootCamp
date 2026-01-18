master_schedule = []

def add_appointment(name, time, dr):
    master_schedule.append({"name": name, "time": time, "dr": dr})

def sort_schedule():
    # Sort by the 'time' value in the dictionary
    master_schedule.sort(key=lambda x: x["time"])

def get_dr_queue(dr_name):
    return [appt for appt in master_schedule if appt["dr"] == dr_name]

def serve_patient(index):
    if 0 <= index < len(master_schedule):
        return master_schedule.pop(index)
    return None

if __name__ == "__main__":
    add_appointment("Alice", "10:00", "Smith")
    add_appointment("Bob", "08:00", "Smith")
    sort_schedule()
    print(master_schedule)
