def download_report(filename):
    """Simulates a secure file access error"""
    raise PermissionError(f"OS_BLOCK: Access denied to C:/MED_DATA/REPORTS/{filename}")

def secure_download_handler(filename, log_store):
    """
    TODO:
    1. Try calling download_report(filename).
    2. Catch PermissionError as e.
    3. Append str(e) to log_store.
    4. Return "Unable to access report. Please try again later."
    """
    # WRITE CODE HERE
    pass

def main():
    system_logs = []
    user_msg = secure_download_handler("PATIENT_001.pdf", system_logs)
    print(f"To User: {user_msg}")
    print(f"In Developer Logs: {system_logs}")

if __name__ == "__main__":
    main()
