"""
Unit 1.5: Operators & Expressions - Exercise Solutions
"""

# ============================================================================
# Exercise 1: Arithmetic Operators - Solution
# ============================================================================

def calculate_tablets(total_mg, mg_per_tablet):
    full_tablets = total_mg // mg_per_tablet
    remaining_mg = total_mg % mg_per_tablet
    return (full_tablets, remaining_mg)


# ============================================================================
# Exercise 2: Comparison Operators - Solution
# ============================================================================

def is_within_range(value, min_val, max_val):
    return min_val <= value <= max_val


# ============================================================================
# Exercise 3: Logical Operators - Solution
# ============================================================================

def check_emergency(heart_rate, spo2, is_conscious):
    hr_alert = (heart_rate < 40) or (heart_rate > 140)
    resp_alert = (spo2 < 90) and (not is_conscious)
    return hr_alert or resp_alert


# ============================================================================
# Exercise 4: Membership & Identity - Solution
# ============================================================================

def validate_blood_type(blood_type, patient_obj):
    ALLOWED = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    is_valid_type = blood_type in ALLOWED
    is_patient_none = patient_obj is None
    return (is_valid_type, is_patient_none)


# ============================================================================
# Exercise 5: Assignment Operators - Solution
# ============================================================================

def apply_dosage_step(current_dose, increment, multiplier):
    current_dose += increment
    current_dose *= multiplier
    return float(current_dose)


# ============================================================================
# Exercise 6: Operator Precedence - Solution
# ============================================================================

def solve_precedence_puzzle(a, b, c):
    # Use parentheses to force addition before multiplication
    return (a + b) * c


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.5 Exercise Solutions...")
    passed = 0
    total = 6
    
    if calculate_tablets(500, 200) == (2, 100): passed += 1
    if is_within_range(37.5, 36.0, 38.0): passed += 1
    if check_emergency(150, 95, True) and check_emergency(70, 85, False): passed += 1
    if validate_blood_type("O+", None) == (True, True): passed += 1
    if apply_dosage_step(10, 5, 2) == 30.0: passed += 1
    if solve_precedence_puzzle(1, 2, 3) == 9: passed += 1

    print(f"Result: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
