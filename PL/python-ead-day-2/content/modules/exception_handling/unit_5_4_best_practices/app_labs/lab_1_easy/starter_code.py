def get_contact_info_legacy(data, key):
    """LBYL Style (Legacy)"""
    if key in data:
        return data[key]
    else:
        return "Contact info not provided"

def get_contact_info_pythonic(data, key):
    """
    TODO: Refactor the above logic to EAFP style.
    Use try-except KeyError.
    """
    # WRITE CODE HERE
    pass

def main():
    patient_data = {"phone": "555-0101"}
    print(get_contact_info_pythonic(patient_data, "phone"))
    print(get_contact_info_pythonic(patient_data, "email"))

if __name__ == "__main__":
    main()
