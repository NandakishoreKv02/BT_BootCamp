"""
Lab 3: The Prescription Signature - Starter Code
"""

class Prescription:
    # TODO: Implement __init__ and set_instructions()
    def __init__(self, drug_name):
        self.drug_name = drug_name
        self.dose = 0
        self.unit = ""
        self.freq = ""
    
    def set_instructions(self, dose, unit, frequency):
        self.dose = dose
        self.unit = unit
        self.frequency = frequency
        return f"Take {dose}{unit}, {frequency}."

def main():
    print("--- Pharmacy Labeling ---")
    # TODO: Create rx and set instructions
    rx = Prescription("Insulin")
    label = rx.set_instructions(10, 'units', 'Before meals')
    print(label)

if __name__ == "__main__":
    main()
