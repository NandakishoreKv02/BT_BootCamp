"""
Lab 1: The Great Variable Cleanup - Starter Code
"""

def refactor_balance_logic(intake_ml, output_ml):
    """
    Refactor the following code to use PEP 8 naming.
    
    BAD CODE:
    v1 = intake_ml
    v2 = output_ml
    b = v1 - v2
    if b < 0:
        s = "DEFICIT"
    else:
        s = "SURPLUS"
    return {"b": b, "s": s}
    """
    fluid_balance = intake_ml - output_ml
    if fluid_balance < 0:
        balance_status = "DEFICIT"
    else:
        balance_status = "SURPLUS"
    return {"balance": fluid_balance, "status": balance_status}

if __name__ == "__main__":
    print(refactor_balance_logic(1000, 500))
