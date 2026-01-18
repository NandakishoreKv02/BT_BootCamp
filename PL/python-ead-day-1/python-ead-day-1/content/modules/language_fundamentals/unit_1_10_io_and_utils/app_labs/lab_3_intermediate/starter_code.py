"""
Lab 3: Encounter Log Append Utility - Solution
"""

def log_access(filename, user_id, patient_id):
    with open(filename, "a") as file:
        file.write(f"{user_id} accessed {patient_id}\n")

if __name__ == "__main__":
    log_access("audit.txt", "Dr_Smith", "P_99")
    log_access("audit.txt", "Nurse_Jones", "P_99")
