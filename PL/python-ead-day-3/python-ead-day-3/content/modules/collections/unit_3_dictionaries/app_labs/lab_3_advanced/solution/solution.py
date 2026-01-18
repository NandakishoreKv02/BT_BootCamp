"""
Lab 3 (Advanced): Hospital Analytics System
Solution Code

Module: Collections - Unit 3: Dictionaries
"""

def merge_datasets(main_db, archive_db):
    """
    Merge archive_db into main_db, handling conflicts.
    """
    conflicts = []
    
    for doc_id, data in archive_db.items():
        if doc_id in main_db:
            conflicts.append(doc_id)
        else:
            main_db[doc_id] = data
            
    return conflicts


def validate_records(db):
    """
    Check records for required fields ("name", "age", "blood_type").
    Mark missing fields with "status": "incomplete".
    """
    required_keys = {"name", "age", "blood_type"}
    valid_cnt = 0
    invalid_cnt = 0
    
    for doc_id, record in db.items():
        # Check if all required keys are in the record
        # Use set features for efficiency: required_keys.issubset(record.keys())
        if required_keys.issubset(record.keys()):
            record["status"] = record.get("status", "active")
            valid_cnt += 1
        else:
            record["status"] = "incomplete"
            invalid_cnt += 1
            
    return (valid_cnt, invalid_cnt)


def search_patients(db, criteria):
    """
    Search patients by multiple criteria.
    """
    matches = []
    
    for doc_id, record in db.items():
        # Skip incomplete records typically, but prompt didn't strictly say safe assumption implies searching active data
        # Let's search all for thoroughness unless filtered
        
        match = True
        
        # Check blood type
        if "blood_type" in criteria:
            if record.get("blood_type") != criteria["blood_type"]:
                match = False
                
        # Check min age
        if match and "min_age" in criteria:
            if record.get("age", 0) < criteria["min_age"]:
                match = False
                
        # Check max age
        if match and "max_age" in criteria:
            if record.get("age", 999) > criteria["max_age"]: # 999 safe default
                match = False
                
        # Check string contains (case-insensitive)
        if match and "name_contains" in criteria:
            name = record.get("name", "").lower()
            query = criteria["name_contains"].lower()
            if query not in name:
                match = False
                
        if match:
            matches.append(doc_id)
            
    return matches


def get_blood_type_distribution(db):
    """
    Count active patients by blood type.
    """
    stats = {}
    
    for record in db.values():
        if record.get("status") == "incomplete":
            continue
            
        b_type = record.get("blood_type", "Unknown")
        stats[b_type] = stats.get(b_type, 0) + 1
        
    return stats
