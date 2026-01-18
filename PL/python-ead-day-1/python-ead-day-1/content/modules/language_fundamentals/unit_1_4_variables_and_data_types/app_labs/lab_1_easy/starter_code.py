"""
Lab 1: Patient Data Parser - Starter Code
"""

def parse_patient_data(id_str, age_str, weight_str, smoker_str):
    """
    Parse raw strings into correct types.

    Args:
        id_str (str): e.g. " 1001 "
        age_str (str): e.g. "45"
        weight_str (str): e.g. "70.5"
        smoker_str (str): e.g. "Yes" or "No"

    Returns:
        dict: {
            "id": int,
            "age": int,
            "weight": float,
            "is_smoker": bool
        }
    """
    return {
        "id": int(id_str.strip()) if id_str.strip() else 0,
        "age": int(age_str.strip()) if age_str.strip() else 0,
        "weight": float(weight_str.strip()) if weight_str.strip() else 0.0,
        "is_smoker": smoker_str.strip() in ["Yes", "yes", "True", "true"]
    }

if __name__ == "__main__":
    # Test your code
    print(parse_patient_data("123", "30", "70.5", "Yes"))
