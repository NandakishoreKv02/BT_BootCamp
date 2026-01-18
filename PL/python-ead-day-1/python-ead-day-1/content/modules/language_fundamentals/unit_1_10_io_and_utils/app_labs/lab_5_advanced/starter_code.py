"""
Lab 5: Patient Electronic Archive - Solution
"""

def write_record_to_disk(mrn, name, diagnosis):
    filename = f"{mrn}.txt"
    with open(filename, "w") as file:
        file.write(f"MRN: {mrn}\n")
        file.write(f"NAME: {name}\n")
        file.write(f"DIAGNOSIS: {diagnosis}\n")

def archive_patient():
    print("--- NEW PATIENT ARCHIVE ---")
    mrn = input("MRN: ")
    name = input("Full Name: ")
    diag = input("Diagnosis: ")
    
    write_record_to_disk(mrn, name, diag)
    print(f"Success. Record {mrn}.txt created.")

if __name__ == "__main__":
    # archive_patient()
    pass
