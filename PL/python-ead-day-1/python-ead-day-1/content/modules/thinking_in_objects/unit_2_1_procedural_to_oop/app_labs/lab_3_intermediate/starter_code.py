"""
Lab 3: Breaking the Triage Monolith - Starter Code
"""

# --- BAD PROCEDURAL CODE ---
total_admitted = 0

def process_patient_monolith(name, age, hr, complaint):
    global total_admitted
    print(f"Processing {name}...")
    
    # Validation logic
    if age < 0:
        print("Invalid age")
        return

    # Priority logic mixed with output
    priority = "Normal"
    if hr > 120 or complaint == "Chest Pain":
        priority = "HIGH"
        print("!! ALERT: HIGH SEVERITY !!")
    
    # Side effects
    total_admitted += 1
    
    # Final Output
    print(f"Wristband: [{name}] - Priority: {priority}")

# ---------------------------

# TODO: Refactor into specialized functions working on a dictionary.

def create_triage_record(name, age, hr, complaint):
    # Returns dict
    pass

def assess_severity(record):
    pass

def print_wristband(record):
    pass

def main():
    print("--- Procedural Run ---")
    process_patient_monolith("John", 45, 130, "Headache")

    print("\n--- Refactored Run ---")
    # TODO: Create record, assess, print

if __name__ == "__main__":
    main()
