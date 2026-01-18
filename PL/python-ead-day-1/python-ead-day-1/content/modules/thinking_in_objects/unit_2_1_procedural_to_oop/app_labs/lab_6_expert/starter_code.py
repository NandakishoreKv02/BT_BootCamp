"""
Lab 6: The Procedural Nightmare - Starter Code
"""

# --- LEGACY SPAGHETTI CODE ---
# Everything is global. Indices must match.
p_names = ["John", "Jane", "Bob"]
p_status = ["Admitted", "Admitted", "Admitted"]
p_doctor_index = [-1, -1, -1] # -1 means no doctor

d_names = ["Dr. House", "Dr. Strange"]
# d_patients is not even tracked explicitly! We have to scan p_doctor_index to find a doctor's patients.

def assign_doctor_legacy(p_idx, d_idx):
    global p_doctor_index
    p_doctor_index[p_idx] = d_idx
    print(f"Assigned {p_names[p_idx]} to {d_names[d_idx]}")

def discharge_legacy(p_idx):
    global p_status, p_doctor_index
    p_status[p_idx] = "Discharged"
    p_doctor_index[p_idx] = -1 # Clear assignment
    print(f"Discharged {p_names[p_idx]}")

def print_report_legacy():
    print("--- Legacy Report ---")
    for i in range(len(d_names)):
        print(f"Doctor: {d_names[i]}")
        # Find patients... heavily inefficient scan
        for p in range(len(p_names)):
            if p_doctor_index[p] == i:
                print(f"  - {p_names[p]} ({p_status[p]})")

# -----------------------------

# TODO: Refactor everything below.

def create_patient(pid, name):
    """
    REQUIRED: Return a dictionary representing a patient.
    Keys: 'id', 'name', 'status', 'doctor_id'
    """
    pass

def create_doctor(did, name):
    """
    REQUIRED: Return a dictionary representing a doctor.
    Keys: 'id', 'name', 'assigned_patients' (list of IDs)
    """
    pass

def assign_doctor(doc, patient):
    """
    REQUIRED: Link the doctor and patient dictionaries.
    (Update patient['doctor_id'] and doc['assigned_patients'])
    """
    pass

def discharge_patient(patient):
    """
    REQUIRED: Set patient status to 'Discharged'.
    """
    pass

def print_report(doctors, patients):
    """
    REQUIRED: Print a report showing each doctor and their assigned patients.
    """
    pass

def main():
    # RUN LEGACY (Already implemented for comparison)
    assign_doctor_legacy(0, 0) # John -> House
    assign_doctor_legacy(1, 1) # Jane -> Strange
    discharge_legacy(0)
    print_report_legacy()

    print("\n--- REFACTORED SYSTEM ---")
    # TODO: Implement your clean solution here
    
    # 1. Create lists of doctors and patients
    # 2. Assign
    # 3. Discharge
    # 4. Report

if __name__ == "__main__":
    main()
