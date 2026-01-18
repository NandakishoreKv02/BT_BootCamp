master_schedule = [
    {"patient": "Alice", "doctor": "Smith", "time": "10:00"},
    {"patient": "Bob", "doctor": "Jones", "time": "10:30"},
    {"patient": "Charlie", "doctor": "Smith", "time": "11:00"},
    {"patient": "David", "doctor": "Brown", "time": "11:30"}
]

dr_smith_list = [appt for appt in master_schedule if appt["doctor"] == "Smith"]

print(dr_smith_list)
