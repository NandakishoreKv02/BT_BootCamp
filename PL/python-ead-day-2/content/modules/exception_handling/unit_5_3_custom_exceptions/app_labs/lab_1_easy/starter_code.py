class PatientNotFound(Exception):
    """Raised when a patient ID is not found in the database."""
    pass

def get_patient(db, patient_id):
    """
    TODO:
    1. Check if patient_id in db.
    2. If not, raise PatientNotFound with a message.
    3. Else return db[patient_id].
    """
    # WRITE CODE HERE
    pass

def main():
    db = {"101": "Alice"}
    try:
        print(get_patient(db, "102"))
    except PatientNotFound as e:
        print(f"Caught: {e}")

if __name__ == "__main__":
    main()
