"""
Lab 3: The Pythonic Patient Portal - Starter Code
"""

# TODO: Rename to PatientData
class PatientData:
    def __init__(self, name):
        self.patient_name = name

def is_admitted(patient_name, admission_list):
    """
    Check if a patient name exists in the list.
    """
    # TODO: Refactor this manual loop to use 'in'
    return patient_name in admission_list

if __name__ == "__main__":
    current_list = ["Alice", "Bob", "Charlie"]
    print(f"Is Bob in? {is_admitted('Bob', current_list)}")
