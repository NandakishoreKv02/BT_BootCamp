"""Lab 6 Starter - Build complete EHR system with all modules"""
import json
# TODO: Implement patient, appointment, medication, reporting, persistence, and menu modules
ehr_data = {"patients": [], "appointments": [], "medications": []}

def add_patient(mrn, name, age, diagnosis):
    patient = {"mrn": mrn, "name": name, "age": age, "diagnosis": diagnosis}
    ehr_data["patients"].append(patient)
    return (True, "Patient added successfully")

def search_patient(mrn):
    for patient in ehr_data["patients"]:
        if patient["mrn"] == mrn:
            return patient
    return None

def schedule_appointment(mrn, date, time):
    if search_patient(mrn):
        appointment = {"mrn": mrn, "date": date, "time": time}
        ehr_data["appointments"].append(appointment)
        return (True, "Appointment scheduled")
    return (False, "Patient not found")

def view_schedule(date):
    return [a for a in ehr_data["appointments"] if a["date"] == date]

def prescribe_medication(mrn, medication, dosage):
    if search_patient(mrn):
        med = {"mrn": mrn, "medication": medication, "dosage": dosage}
        ehr_data["medications"].append(med)
        return (True, "Medication prescribed")
    return (False, "Patient not found")

def generate_daily_report(date):
    appointments = view_schedule(date)
    return f"Daily Report for {date}: {len(appointments)} appointments"

def patient_history(mrn):
    patient = search_patient(mrn)
    if not patient:
        return None
    appointments = [a for a in ehr_data["appointments"] if a["mrn"] == mrn]
    medications = [m for m in ehr_data["medications"] if m["mrn"] == mrn]
    return {"patient": patient, "appointments": appointments, "medications": medications}

def save_all_data(filename="ehr_data.json"):
    try:
        with open(filename, 'w') as f:
            json.dump(ehr_data, f)
        return True
    except:
        return False

def load_all_data(filename="ehr_data.json"):
    global ehr_data
    try:
        with open(filename, 'r') as f:
            ehr_data = json.load(f)
        return True
    except:
        return False

def display_menu():
    print("\n=== EHR System ===")
    print("1. Add Patient")
    print("2. Schedule Appointment")
    print("3. Prescribe Medication")
    print("4. Exit")

def main():
    print("EHR System Started")

if __name__ == "__main__":
    main()
