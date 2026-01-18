"""
Lab 1 (Easy): Hospital Registry - Part 1
Starter Code
"""

def initialize_registry(visiting_ids):
    """
    Convert a list of visit logs to a set of unique IDs.
    """
    # TODO: Implement this
    pass


def check_in_patient(registry, patient_id):
    """
    Add a new patient_id to the registry.
    """
    # TODO: Implement this
    pass


def remove_record(registry, patient_id):
    """
    Safely remove a patient_id from the registry.
    """
    # TODO: Implement this
    pass


def get_unique_count(registry):
    """
    Return the total number of unique patients in the registry.
    """
    # TODO: Implement this
    pass


if __name__ == "__main__":
    # Test your implementation manually here
    my_registry = initialize_registry([101, 102, 101, 105])
    print(f"Initial: {my_registry}") # Should be {101, 102, 105}
    
    check_in_patient(my_registry, 110)
    print(f"After check-in: {my_registry}")
    
    remove_record(my_registry, 102)
    print(f"After removal: {my_registry}")
    
    print(f"Total count: {get_unique_count(my_registry)}")
