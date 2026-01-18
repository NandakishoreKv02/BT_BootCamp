def update_patient_status(manager_dict, patient_id, status):
    manager_dict[patient_id] = status
    return manager_dict

def record_vitals(history_list, timestamp, heart_rate):
    history_list.append((timestamp, heart_rate))
    return history_list

def register_visit(registry_set, patient_id):
    registry_set.add(patient_id)
    return registry_set

def lock_config(device_ids_list):
    return frozenset(device_ids_list)

def batch_status_check(manager_dict, target_ids):
    return [manager_dict.get(pid, "Unknown") for pid in target_ids]
