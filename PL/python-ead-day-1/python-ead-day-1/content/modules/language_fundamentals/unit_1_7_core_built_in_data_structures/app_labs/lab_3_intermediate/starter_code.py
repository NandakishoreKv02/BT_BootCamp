"""
Lab 3: Cross-Patient Allergy Tracker - Starter Code
"""

def get_common_allergies(group_a, group_b):
    """
    Find unique allergies that appear in both patient groups.
    
    Args:
        group_a (list): e.g. ["Latex", "Latex", "Penicillin"]
        group_b (list): e.g. ["Penicillin", "Peanuts"]
        
    Returns:
        set: Common allergies.
    """
    # TODO: Convert to sets and find intersection
    set_a = set(group_a)
    set_b = set(group_b)
    return set_a & set_b

if __name__ == "__main__":
    a = ["Latex", "Penicillin", "Latex"]
    b = ["Penicillin", "Peanuts"]
    print(f"Common: {get_common_allergies(a, b)}")
