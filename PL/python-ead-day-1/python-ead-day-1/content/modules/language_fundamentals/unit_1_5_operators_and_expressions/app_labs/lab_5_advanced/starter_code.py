"""
Lab 5: Fluid Balance Monitor - Starter Code
"""

def calculate_fluid_status(iv_ml, oral_ml, urine_ml, drainage_ml, scale_factor=1.0):
    """
    Calculate the net fluid balance.
    
    Returns:
        float: Net balance rounded to 2 decimal places.
    """
    # TODO: Implement ((iv + oral) - (urine + drainage)) * scale_factor
    return round(((iv_ml + oral_ml) - (urine_ml + drainage_ml)) * scale_factor, 2)

if __name__ == "__main__":
    # 2000 total in, 1500 total out = 500 balance
    print(f"Balance: {calculate_fluid_status(1200, 800, 1000, 500)}")
