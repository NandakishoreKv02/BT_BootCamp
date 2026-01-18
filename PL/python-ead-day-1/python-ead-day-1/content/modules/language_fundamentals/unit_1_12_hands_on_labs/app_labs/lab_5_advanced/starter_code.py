"""Lab 5 Starter - TODO: Implement all CRUD and filter functions"""
def add_patient(patients, mrn, name, age, diagnosis):
    patient = {"mrn": mrn, "name": name, "age": age, "diagnosis": diagnosis}
    patients.append(patient)
    return True

def find_patient_by_mrn(patients, mrn):
    for patient in patients:
        if patient["mrn"] == mrn:
            return patient
    return None

def update_patient(patients, mrn, **kwargs):
    patient = find_patient_by_mrn(patients, mrn)
    if patient:
        patient.update(kwargs)
        return True
    return False

def delete_patient(patients, mrn):
    patient = find_patient_by_mrn(patients, mrn)
    if patient:
        patients.remove(patient)
        return True
    return False

def filter_by_age_range(patients, min_age, max_age):
    return [p for p in patients if min_age <= p["age"] <= max_age]

def filter_by_diagnosis(patients, diagnosis):
    return [p for p in patients if p["diagnosis"] == diagnosis]

def display_patients(patients):
    for p in patients:
        print(f"MRN: {p['mrn']}, Name: {p['name']}, Age: {p['age']}, Diagnosis: {p['diagnosis']}")

def export_to_file(patients, filename):
    try:
        with open(filename, 'w') as f:
            for p in patients:
                f.write(f"{p['mrn']},{p['name']},{p['age']},{p['diagnosis']}\n")
        return True
    except:
        return False
