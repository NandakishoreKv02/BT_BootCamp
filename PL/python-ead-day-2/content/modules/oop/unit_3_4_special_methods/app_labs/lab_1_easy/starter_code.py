"""
Starter Code - Reset
"""
'Lab 1: Solution - String Representations'

class Patient:
    """Represents a patient in the medical record system."""

    def __init__(self, patient_id: str, name: str, dob: str, blood_type: str, admission_date: str):
        # TODO: Implement logic
        pass

    def __str__(self) -> str:
        """User-friendly string representation."""
        # TODO: Implement logic
        pass

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    patient = Patient('P001', 'Alice Smith', '1990-05-15', 'O+', '2024-01-10')
    print(patient)
    print(repr(patient))