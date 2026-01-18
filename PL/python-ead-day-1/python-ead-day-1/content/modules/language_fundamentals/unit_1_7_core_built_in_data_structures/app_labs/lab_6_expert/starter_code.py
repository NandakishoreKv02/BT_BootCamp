"""
Lab 6: Hospital Hierarchy Mapper - Starter Code
"""

def register_doctor(registry, dept, doctor, specialty):
    """
    Update a nested registry of departments, doctors, and specialties.
    Structure: {dept: {doctor_name: {specialty_set}}}
    """
    # TODO: Implement nested addition
    if dept not in registry:
        registry[dept] = {}
    if doctor not in registry[dept]:
        registry[dept][doctor] = set()
    registry[dept][doctor].add(specialty)

def get_dept_doctors(registry, dept):
    """Return list of doctor names in a department."""
    # TODO: Implement
    if dept in registry:
        return list(registry[dept].keys())
    return []

def get_unique_specialties_for_dept(registry, dept):
    """Return a set of all unique specialties in a department."""
    # TODO: Implement aggregation
    all_specs = set()
    if dept in registry:
        for doctor_specs in registry[dept].values():
            all_specs |= doctor_specs
    return all_specs

if __name__ == "__main__":
    hosp = {}
    register_doctor(hosp, "ER", "Dr. A", "Trauma")
    register_doctor(hosp, "ER", "Dr. A", "Suture")
    register_doctor(hosp, "ER", "Dr. B", "Trauma")
    
    print(f"ER Doctors: {get_dept_doctors(hosp, 'ER')}")
    print(f"ER Specialties: {get_unique_specialties_for_dept(hosp, 'ER')}")
