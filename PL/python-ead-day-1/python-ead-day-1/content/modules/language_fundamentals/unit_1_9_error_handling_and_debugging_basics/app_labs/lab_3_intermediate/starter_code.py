"""
Lab 3: Insurance Coverage Lookup - Starter Code
"""

def fetch_provider_id(patient_record):
    """
    Retrieve provider_id with error logging.
    """
    # TODO: Implement try/except
    return ""

if __name__ == "__main__":
    p1 = {"name": "Alice", "provider_id": "PRV_99"}
    p2 = {"name": "Bob"} # Missing provider_id
    
    print(f"Alice: {fetch_provider_id(p1)}")
    print(f"Bob: {fetch_provider_id(p2)}")
