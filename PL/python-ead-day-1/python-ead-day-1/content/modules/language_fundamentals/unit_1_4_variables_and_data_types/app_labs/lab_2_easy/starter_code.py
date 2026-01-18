"""
Lab 2: BMI Calculator - Starter Code
"""

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index.

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: BMI rounded to 2 decimal places.
    """
    if height_m <= 0:
        return 0.0
    return round(weight_kg / (height_m ** 2), 2)

if __name__ == "__main__":
    print(f"BMI (70kg, 1.75m): {calculate_bmi(70, 1.75)}")
