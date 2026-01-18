"""
Lab 1: The Code Cleanup - Starter Code
"""

# --- MESSY PROCEDURAL CODE ---
p_names = []
p_times = []

def add_patient(name, time):
    p_names.append(name)
    p_times.append(time)
    print(f"Checked in {name} at {time}.")

def find_patient(name):
    if name in p_names:
        idx = p_names.index(name)
        return p_times[idx]
    return -1

# TODO: Refactor the above into a clean WaitingRoom class
class WaitingRoom:
    pass

def main():
    print("--- Clinic Queue ---")
    # TODO: Use the class instead of the functions
    pass

if __name__ == "__main__":
    main()
