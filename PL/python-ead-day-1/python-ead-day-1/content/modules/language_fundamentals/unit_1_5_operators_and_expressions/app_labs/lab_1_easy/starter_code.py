"""
Lab 1: Pediatric Dosage Calculator - Starter Code
"""

def calculate_mg_dose(weight_kg, mg_per_kg):
    """
    Calculate the total dose in mg based on patient weight.
    
    Args:
        weight_kg (float): Patient weight.
        mg_per_kg (float): Dosage requirement.
        
    Returns:
        float: Total dose rounded to 1 decimal place.
    """
    if weight_kg <= 0:
        return 0.0
    return round(weight_kg * mg_per_kg, 1)

if __name__ == "__main__":
    print(f"Dose for 15.5kg at 10mg/kg: {calculate_mg_dose(15.5, 10)}")
