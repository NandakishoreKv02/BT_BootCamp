"""
Lab 3: Patient Record Validator - Starter Code
"""

# TODO: Define make_validator()

# TODO: Define add_rule(validator, rule_func)

# TODO: Define run_validation(validator, patient)

# Example Rule Functions
def check_mrn(patient):
    if len(patient.get('mrn', '')) != 6:
        return "MRN must be 6 digits"
    return None

def main():
    print("--- Patient Data Integrity Check ---")
    
    patient = {"name": "John", "mrn": "123", "age": -5}
    
    # TODO: Initialize validator
    # TODO: Add rules
    # TODO: Run and print errors
    
    pass

if __name__ == "__main__":
    main()
