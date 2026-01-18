"""
Lab 5: The Extensible Analytics Engine - Starter Code
"""

def create_dataset(label, data_list):
    # TODO: Return dataset dict
    pass

# Calculation Objects (Functions as Objects)
def get_mean(values):
    return sum(values) / len(values) if values else 0

def get_max(values):
    # TODO: Implement
    pass

def analyze_dataset(dataset, calc_func):
    """
    EXTENSIBLE ENGINE:
    This function should be 'Closed for Modification' but 'Open for Extension'.
    You can add 100 new math rules without changing this function.
    """
    # TODO: Implement - call calc_func and return formatted string
    pass

def main():
    print("--- Medical Research Stats ---")
    temps = create_dataset("Patient Temps", [36.5, 37.0, 38.2, 39.1])
    
    # TODO: Analyze temps using get_mean
    # TODO: Analyze temps using get_max
    
    # TODO: Create glucose dataset and analyze it

if __name__ == "__main__":
    main()
