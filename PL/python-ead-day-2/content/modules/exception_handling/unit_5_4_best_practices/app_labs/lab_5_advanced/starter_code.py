def validate_prescription(data):
    """
    Returns a list of error messages.
    Checks:
    1. 'dose' exists and is > 0.
    2. 'drug' exists and is not empty.
    """
    errors = []
    # WRITE VALIDATION LOGIC HERE
    return errors

def calculate_schedule(dose, frequency):
    """Core logic that could still fail with ZeroDivisionError"""
    return dose / frequency

def secure_scheduler(data):
    """
    TODO:
    1. Run validate_prescription.
    2. If errors, return {"status": "rejected", "errors": errors}.
    3. Try calculate_schedule(data['dose'], data['freq']).
    4. Catch ZeroDivisionError -> return {"status": "rejected", "errors": ["Frequency cannot be zero"]}.
    5. Return {"status": "success", "data": result}.
    """
    # WRITE WRAPPER LOGIC HERE
    pass

def main():
    bad_data = {"dose": -5, "drug": "", "freq": 1}
    print(secure_scheduler(bad_data))
    
    zero_val = {"dose": 10, "drug": "Statin", "freq": 0}
    print(secure_scheduler(zero_val))

if __name__ == "__main__":
    main()
