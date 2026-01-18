"""
Lab 1: Interactive Triage Intake - Starter Code
"""

def get_screening_status(name, age):
    """
    Logic to determine screening status based on age.
    """
    years_left = 65 - age
    if years_left > 0:
        return f"Patient {name} will be 65 in {years_left} years."
    else:
        return f"Patient {name} is eligible for screening."

def run_triage():
    """
    Main interactive entry point.
    """
    name = input("Patient Name: ")
    age = int(input("Patient Age: "))
    result = get_screening_status(name, age)
    print(result)

if __name__ == "__main__":
    # run_triage()
    pass
