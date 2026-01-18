"""
Lab 5: Hospital Queue Manager - Starter Code
"""

def admit_patients(queue, capacity):
    """
    Manage admissions based on urgency and capacity.
    
    Args:
        queue (list): List of patient dicts.
        capacity (int): Ward capacity for routine patients.
        
    Returns:
        list: Names of admitted patients.
    """
    admitted = []
    current_routine = 0
    
    # TODO: Implement complex admission logic
    absolute_limit = capacity * 2
    
    for patient in queue:
        if len(admitted) == absolute_limit:
            break
        
        if patient["urgent"]:
            admitted.append(patient["name"])
        else:
            if current_routine < capacity:
                admitted.append(patient["name"])
                current_routine += 1
    
    return admitted

if __name__ == "__main__":
    test_queue = [
        {"name": "P1", "urgent": True},
        {"name": "P2", "urgent": False},
        {"name": "P3", "urgent": False},
        {"name": "P4", "urgent": True},
    ]
    print(f"Admitted: {admit_patients(test_queue, 1)}")
