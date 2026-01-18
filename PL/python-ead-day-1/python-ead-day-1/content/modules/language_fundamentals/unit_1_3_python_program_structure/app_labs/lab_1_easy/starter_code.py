"""
Healthcare patient data formatting module.

This module provides functions for formatting patient records.
"""

def format_patient_id(patient_id):
    """
    Format a patient ID with leading zeros.
    
    Args:
        patient_id (int): The patient ID number.
    
    Returns:
        str: Formatted string "PAT-XXXXX" with 5 digits.
    """
    return f"PAT-{patient_id:05d}"


def format_patient_record(name, patient_id, age):
    """
    Format a complete patient record.
    
    Args:
        name (str): The patient's name.
        patient_id (int): The patient ID number.
        age (int): The patient's age.
    
    Returns:
        str: Formatted patient record string.
    """
    formatted_id = format_patient_id(patient_id)
    return f"Patient: {name} ({formatted_id}), Age: {age}"


if __name__ == "__main__":
    print(format_patient_record("John Doe", 42, 35))
    print(format_patient_record("Jane Smith", 123, 28))
