def is_shift_compliant(ward_staff, master_authorized):
    return ward_staff.issubset(master_authorized)

def no_double_shift_violations(morning_shift, night_shift):
    return morning_shift.isdisjoint(night_shift)

def create_fixed_requirements(cert_list):
    return frozenset(cert_list)

def get_senior_staff(shift_data):
    return {staff_id for staff_id in shift_data if staff_id > 5000}

def identify_unauthorized_ids(ward_staff, master_authorized):
    return ward_staff - master_authorized
