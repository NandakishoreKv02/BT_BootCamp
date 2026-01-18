"""
Lab 4: The Scalable Ward System - Starter Code
"""

# Policy Functions
def general_policy(ward, patient):
    return ward['occupied'] < ward['total']

def icu_policy(ward, patient):
    # TODO: Implement - Only High priority
    pass

def peds_policy(ward, patient):
    # TODO: Implement - Only Age < 18
    pass

# The Engine
def admit_to_ward(ward, patient, policy_map):
    """
    SCALABLE ENGINE: Does not contain any specific logic for ICU or Peds.
    It simply looks up the logic from the map.
    """
    # TODO: Implement the engine
    # 1. Get correct policy from policy_map
    # 2. Check policy performance
    # 3. Update ward if True
    return False

def main():
    print("--- Scalable Admission System ---")
    
    # 1. Setup Policies
    policies = {
        "General": general_policy,
        # TODO: Add others
    }
    
    # 2. Setup Wards
    icu = {"name": "ICU-A", "type": "ICU", "total": 5, "occupied": 0}
    peds = {"name": "Peds-B", "type": "Peds", "total": 10, "occupied": 0}
    
    # 3. Test Cases
    p1 = {"name": "John (High Priority)", "priority": "High", "age": 45}
    p2 = {"name": "Baby Jack (Low Priority)", "priority": "Low", "age": 2}
    
    # TODO: Try admitting multiple patients and print results

if __name__ == "__main__":
    main()
