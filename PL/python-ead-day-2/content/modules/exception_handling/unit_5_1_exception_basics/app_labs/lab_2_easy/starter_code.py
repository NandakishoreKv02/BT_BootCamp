def get_record_field(database, record_id, field_name):
    """
    TODO:
    1. Try to access database[record_id][field_name].
    2. Catch KeyError and return "Data Not Found".
    """
    # WRITE CODE HERE
    pass

def main():
    db = {
        "101": {"name": "Alice", "diagnosis": "Flu"},
        "102": {"name": "Bob"}
    }
    
    # Success
    print(get_record_field(db, "101", "name"))
    # Fail: Bad ID
    print(get_record_field(db, "999", "name"))
    # Fail: Bad Field
    print(get_record_field(db, "102", "diagnosis"))

if __name__ == "__main__":
    main()
