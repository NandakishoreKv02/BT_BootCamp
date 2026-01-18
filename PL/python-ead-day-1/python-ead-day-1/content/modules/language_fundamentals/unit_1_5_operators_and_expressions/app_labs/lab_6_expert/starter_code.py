"""
Lab 6: Dynamic Formula Evaluator - Starter Code
"""

def calculate_risk_score(age, sys_bp, has_diabetes):
    """
    Calculate a cardiac risk score.
    
    Args:
        age (int): Patient age.
        sys_bp (int): Systolic blood pressure.
        has_diabetes (bool): Condition status.
        
    Returns:
        float: Risk score rounded to 1 decimal.
    """
    # TODO: Calculate Age Adjustment (floor divide by 10)
    age_adjustment = age // 10
    # TODO: Calculate Vital Factor ( (sys_bp - 120) * 0.5 )
    vital_factor = (sys_bp - 120) * 0.5
    # TODO: Calculate Lab Factor (2.0 if True, 0.0 if False)
    lab_factor = 2.0 if has_diabetes else 0.0
    
    return round(age_adjustment + vital_factor + lab_factor, 1)

if __name__ == "__main__":
    # 65//10 = 6, (140-120)*0.5 = 10, True = 2.0 -> Score 18.0
    print(f"Risk: {calculate_risk_score(65, 140, True)}")
