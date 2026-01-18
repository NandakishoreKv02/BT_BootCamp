"""
Lab 5: Patient Profile Generator - Starter Code
"""

# TODO: Define create_patient_record(first_name, last_name, age, city="Unknown")
# TODO: Add docstring
def create_patient_record(first_name, last_name, age, city="Unknown"):
    """
    Create a patient record with formatted name.
    
    Parameters:
        first_name (str): Patient's first name
        last_name (str): Patient's last name
        age (int): Patient's age in years
        city (str): Patient's city (default: "Unknown")
    
    Returns:
        dict: Patient record with full_name, age_years, and location
    """
    formatted_name = f"{last_name.upper()}, {first_name.upper()}"
    return {
        "full_name": formatted_name,
        "age_years": age,
        "location": city
    }

if __name__ == "__main__":
    print(create_patient_record("John", "Doe", 45, "New York"))
