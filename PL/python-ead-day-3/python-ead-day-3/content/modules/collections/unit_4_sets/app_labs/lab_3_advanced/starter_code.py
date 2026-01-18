"""
Lab 3 (Advanced): Staffing Audit
Starter Code
"""

def is_shift_compliant(ward_staff, master_authorized):
    """
    Check if ward_staff is a subset of master_authorized.
    """
    # TODO: Use .issubset()
    pass


def no_double_shift_violations(morning_shift, night_shift):
    """
    Check if morning and night shifts have zero overlap.
    """
    # TODO: Use .isdisjoint()
    pass


def create_fixed_requirements(cert_list):
    """
    Convert list to frozenset.
    """
    # TODO: Use frozenset()
    pass


def get_senior_staff(shift_data):
    """
    Filter IDs > 5000 using set comprehension.
    """
    # TODO: Implement set comprehension
    pass


def identify_unauthorized_ids(ward_staff, master_authorized):
    """
    Find IDs in ward_staff that are not in master_authorized.
    """
    # TODO: Use set difference
    pass


if __name__ == "__main__":
    master = {100, 200, 300, 400, 500}
    current_shift = {100, 300, 999} # 999 is unauthorized
    
    print(f"Is compliant: {is_shift_compliant(current_shift, master)}")
    print(f"Unauthorized: {identify_unauthorized_ids(current_shift, master)}")
    
    am = {100, 200}
    pm = {300, 400}
    print(f"No violations: {no_double_shift_violations(am, pm)}")
    
    staff_ids = [1001, 5005, 2002, 6006, 1001]
    seniors = get_senior_staff(staff_ids)
    print(f"Senior Staff (>5000): {seniors}")
