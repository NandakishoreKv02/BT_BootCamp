class DrugInteractionError(Exception):
    pass

def dispense_medication(drug_name, quantity):
    """
    TODO:
    1. Check if quantity is int. If not -> TypeError.
    2. If drug_name is "Incompatible" -> DrugInteractionError.
    3. Return "Dispensed".
    """
    # WRITE CODE HERE
    pass

def process_order(drug, qty):
    """
    TODO:
    1. Try dispense_medication.
    2. Catch TypeError -> "System Error: Bad Input".
    3. Catch DrugInteractionError -> "Medical Alert: Safety Violation".
    """
    # WRITE CODE HERE
    pass

def main():
    print(process_order("Statin", "five")) # System Error
    print(process_order("Incompatible", 10)) # Medical Alert
    print(process_order("Statin", 10)) # Dispensed

if __name__ == "__main__":
    main()
