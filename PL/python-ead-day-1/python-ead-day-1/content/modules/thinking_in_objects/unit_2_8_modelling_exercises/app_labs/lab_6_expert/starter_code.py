"""
Lab 6: The EHR Refactoring Challenge - Starter Code
"""

# LEGACY MESSY CLASS (The God Object)
class LegacyMedicalSystem:
    def __init__(self):
        self.patients = {} # mrn: name
        self.notes = {}    # mrn: notes
        self.invoices = {} # mrn: amt
    
    def do_everything(self, name, mrn, note, amt):
        self.patients[mrn] = name
        self.notes[mrn] = note
        self.invoices[mrn] = amt

# TODO: Refactor the above into PatientRegistry, ClinicalNotebook, and BillingModule

class PatientRegistry:
    pass

class ClinicalNotebook:
    pass

class BillingModule:
    pass

class EHRPlatform:
    # TODO: Coordinate the modules
    pass

def main():
    print("--- EHR Refactoring Solution ---")
    # TODO: Initialize platform and process a patient
    pass

if __name__ == "__main__":
    main()
