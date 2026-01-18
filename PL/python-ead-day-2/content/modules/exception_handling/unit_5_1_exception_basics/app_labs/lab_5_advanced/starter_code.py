def parse_record(raw_string):
    """
    TODO:
    1. Split string by ';'.
    2. For each part, split by ':'.
    3. Convert ID and AGE to int.
    4. Handle ValueError (bad ints) -> "Invalid Number".
    5. Handle IndexError (missing ':') -> "Invalid Format".
    6. Return dict {'id': ..., 'age': ...} on success.
    """
    # WRITE CODE HERE
    pass

def main():
    # Success
    print(parse_record("ID:101;AGE:45"))
    # Bad Format
    print(parse_record("ID101;AGE:45"))
    # Bad Number
    print(parse_record("ID:101;AGE:old"))

if __name__ == "__main__":
    main()
