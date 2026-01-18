"""
Lab 4: Electronic Health Record (EHR) Stub - Starter Code
"""

def add_patient(system, mrn, name, status):
    """Add a patient record to the system."""
    # TODO: Implement
    system[mrn] = {"name": name, "status": status}

def get_patient_status(system, mrn):
    """Retrieve status or return 'Not Found'."""
    # TODO: Implement using .get()
    patient = system.get(mrn)
    if patient:
        return patient["status"]
    return "Not Found"

def update_status(system, mrn, new_status):
    """Update existing patient status. Return True if successful."""
    # TODO: Implement
    if mrn in system:
        system[mrn]["status"] = new_status
        return True
    return False

if __name__ == "__main__":
    ehr = {}
    add_patient(ehr, "101", "Alice Doe", "Stable")
    print(f"Alice Status: {get_patient_status(ehr, '101')}")
    
    update_status(ehr, "101", "Critical")
    print(f"Alice New Status: {get_patient_status(ehr, '101')}")
    
    print(f"Non-existent: {get_patient_status(ehr, '999')}")
