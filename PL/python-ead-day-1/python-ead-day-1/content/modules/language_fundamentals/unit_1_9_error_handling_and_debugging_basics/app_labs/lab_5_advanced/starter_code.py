"""
Lab 5: Multi-Level Data Deep Diver - Starter Code
"""

def extract_weight(data):
    """
    Safely extract nested weight and handle multi-type errors.
    """
    # TODO: Implement multi-exception try/except
    return None

if __name__ == "__main__":
    test_data = {"patient": {"observations": {"weight": "80.0"}}}
    print(f"Success: {extract_weight(test_data)}")
    
    missing = {"patient": {}}
    print(f"Missing: {extract_weight(missing)}")
