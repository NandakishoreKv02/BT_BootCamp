"""
Lab 4: The Clean Documentation Cure - Starter Code

Drug concentration calculator for pharmacokinetics.
"""

# TODO: Refactor parameters, spacing, and add docstrings
def calculate_concentration(dose_mg, time_hr, half_life):
    """
    Calculates the remaining drug concentration.
    
    Args:
        dose_mg (float): Initial dose.
        time_hr (float): Time Elapsed.
        half_life (float): Drug half-life.
    
    Returns:
        float: Remaining concentration.
    """
    return dose_mg * (0.5 ** (time_hr / half_life))

if __name__ == "__main__":
    print(calculate_concentration(100, 4, 2))
