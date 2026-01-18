"""
Lab 4: The Electronic Health Record (EHR) - Starter Code
"""

class MedicalChart:
    def __init__(self, chart_id):
        self.chart_id = chart_id

class Doctor:
    def __init__(self, name):
        self.name = name

class Patient:
    # TODO: Implement __init__ with Composition and Aggregation
    pass

def main():
    print("--- EHR Lifecycle management ---")
    # TODO: Create one doctor and two patients
    # TODO: Prove charts are unique (composition) and doctor is shared (aggregation)
    pass

if __name__ == "__main__":
    main()
