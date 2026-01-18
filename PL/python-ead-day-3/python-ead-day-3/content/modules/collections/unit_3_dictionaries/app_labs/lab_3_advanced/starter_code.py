"""
Lab 3 (Advanced): Hospital Analytics System
Starter Code

Module: Collections - Unit 3: Dictionaries
"""

def merge_datasets(main_db, archive_db):
    """
    Merge archive_db into main_db, handling conflicts.
    
    Args:
        main_db (dict): The primary database
        archive_db (dict): The legacy database to merge in
        
    Returns:
        list: List of IDs that existed in both (conflicts)
    """
    # TODO: Iterate through archive_db
    # TODO: If key in main_db, record conflict
    # TODO: If key NOT in main_db, add to main_db
    pass


def validate_records(db):
    """
    Check records for required fields ("name", "age", "blood_type").
    Mark missing fields with "status": "incomplete".
    
    Args:
        db (dict): The patient database
        
    Returns:
        tuple: (count_active, count_incomplete)
    """
    # TODO: Iterate through all records
    # TODO: Check for required keys
    # TODO: Update "status" field
    # TODO: Count and return stats
    pass


def search_patients(db, criteria):
    """
    Search patients by multiple criteria.
    
    Supported keys in criteria:
        - "blood_type": Exact string match
        - "min_age": Age >= value
        - "max_age": Age <= value
        - "name_contains": Substring match (case-insensitive)
        
    Args:
        db (dict): The database
        criteria (dict): Filter rules
        
    Returns:
        list: List of matching Patient IDs
    """
    # TODO: Loop through each patient
    # TODO: detailed check against all criteria
    # TODO: Return matching IDs
    pass


def get_blood_type_distribution(db):
    """
    Count active patients by blood type.
    
    Args:
        db (dict): The database
        
    Returns:
        dict: { "A+": 10, "O-": 5, ... }
    """
    # TODO: Aggregate counts
    # TODO: Ignore "incomplete" records
    pass


# ============================================================================
# Manual Testing Section
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Lab 3 (Advanced): Analytics Engine")
    print("=" * 80)
    
    # 1. Setup Data
    current_data = {
        101: {"name": "Alice", "age": 30, "blood_type": "A+"},
        102: {"name": "Bob", "age": 45, "blood_type": "O-"}
    }
    
    archive_data = {
        102: {"name": "Bob Duplicate", "age": 45, "blood_type": "O-"}, # Conflict
        103: {"name": "Charlie", "age": 25} # Missing blood_type (Invalid)
    }
    
    # 2. Merge
    print("\n[Task 1] Merging Datasets...")
    conflicts = merge_datasets(current_data, archive_data)
    print(f"Conflicts: {conflicts}")
    print(f"Merged Keys: {list(current_data.keys())}")
    
    # 3. Validate
    print("\n[Task 2] Validating Schema...")
    valid, invalid = validate_records(current_data)
    print(f"Valid: {valid}, Invalid: {invalid}")
    print(f"Patient 103 Status: {current_data[103].get('status')}")
    
    # 4. Search
    print("\n[Task 3] Searching (Age > 20)...")
    results = search_patients(current_data, {"min_age": 20})
    print(f"Found IDs: {results}")
    
    # 5. Stats
    print("\n[Task 4] Stats...")
    stats = get_blood_type_distribution(current_data)
    print(f"Blood Types: {stats}")
    
    print("\n" + "=" * 80)
    print("Run tests.py to verify complex logic!")
    print("=" * 80)
