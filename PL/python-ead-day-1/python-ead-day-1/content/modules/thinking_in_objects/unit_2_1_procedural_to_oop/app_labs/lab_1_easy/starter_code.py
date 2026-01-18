"""
Lab 1: The Global Bed Manager - Starter Code
"""

# --- BAD PROCEDURAL CODE STARTS HERE ---
# Problem: We can only track ONE unit's beds.

total_beds = 10
occupied_beds = 0
ward_name = "General"

def admit_legacy():
    global occupied_beds
    if occupied_beds < total_beds:
        occupied_beds += 1
    else:
        print(f"{ward_name} is full!")

def discharge_legacy():
    global occupied_beds
    if occupied_beds > 0:
        occupied_beds -= 1

# --- BAD PROCEDURAL CODE ENDS HERE ---

# TODO: Define make_ward(name, capacity) -> returns dict

# TODO: Define admit_patient(ward) -> modifies dict

# TODO: Define discharge_patient(ward) -> modifies dict

def main():
    print("--- Legacy Global System ---")
    admit_legacy()
    print(f"Beds: {occupied_beds}/{total_beds}")

    print("\n--- New Modular System ---")
    # TODO: Create 'icu' and 'general' wards
    # TODO: Admit patients to both
    # TODO: Verify they are independent

if __name__ == "__main__":
    main()
