def initialize_registry(visiting_ids):
    return set(visiting_ids)

def check_in_patient(registry, patient_id):
    registry.add(patient_id)
    return registry

def remove_record(registry, patient_id):
    registry.discard(patient_id)
    return registry

def get_unique_count(registry):
    return len(registry)
