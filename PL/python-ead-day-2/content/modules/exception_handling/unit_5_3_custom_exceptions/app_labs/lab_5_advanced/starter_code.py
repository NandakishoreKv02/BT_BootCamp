class RecordImportError(Exception):
    """
    TODO:
    Implement __init__ to accept message, row_idx, and field.
    """
    pass

def validate_age(age_val, row_idx):
    """
    TODO:
    Raise RecordImportError if age < 0 or age > 150.
    """
    # WRITE CODE HERE
    pass

def import_records(age_list):
    """
    TODO:
    1. Loop through age_list.
    2. Try validate_age.
    3. If success, increment count.
    4. If RecordImportError caught, add formatted msg to error list.
    5. Return (count, error_list).
    """
    # WRITE CODE HERE
    pass

def main():
    ages = [25, -1, 300, 45]
    print(import_records(ages))
    # Expected: (2, ["Row 1: age - Age cannot be negative", "Row 2: age - Age out of range"])

if __name__ == "__main__":
    main()
