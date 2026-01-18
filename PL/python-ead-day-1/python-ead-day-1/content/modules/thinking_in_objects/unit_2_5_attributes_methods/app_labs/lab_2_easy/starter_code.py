"""
Lab 2: The Hospital Census Tracker - Starter Code
"""

class Admission:
    # TODO: Define Class Attribute 'total_patients'
    total_patients = 0
    
    def __init__(self, name):
        # TODO: Store name and increment the shared total
        self.name = name
        Admission.total_patients += 1

def main():
    print("--- Hospital Census ---")
    # TODO: Create several admissions and print the global total
    Admission("Patient1")
    Admission("Patient2")
    Admission("Patient3")
    print(f"Total patients: {Admission.total_patients}")
    Admission("Patient4")
    Admission("Patient5")
    print(f"Total patients: {Admission.total_patients}")

if __name__ == "__main__":
    main()
