"""
Lab 6: Clinical Risk Score Orchestrator - Starter Code
"""

def _calc_age_factor(age):
    # TODO: Implement
    return age // 10

def _calc_vital_factor(hr):
    # TODO: Implement
    return 5 if hr > 100 else 0

def _calc_lab_factor(has_diabetes):
    # TODO: Implement
    return 10 if has_diabetes else 0

def get_total_risk(age, hr, has_diabetes):
    """
    Orchestrate the calculation of the total health risk score.
    """
    # TODO: Call helpers and return sum
    return _calc_age_factor(age) + _calc_vital_factor(hr) + _calc_lab_factor(has_diabetes)

if __name__ == "__main__":
    # Age 70 (7) + HR 110 (5) + Diabetes True (10) = 22
    print(f"Total Risk: {get_total_risk(70, 110, True)}%")
