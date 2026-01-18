def optimize_registry(legacy_list):
    return set(legacy_list)

def is_id_inactive(optimized_collection, target_id):
    return target_id in optimized_collection
