"""
Lab 6: Automated Billing Generator - Starter Code
"""

def calculate_bill(procedures):
    """
    Calculate final hospital bill with surcharges and discounts.
    
    Args:
        procedures (list): List of dicts.
        
    Returns:
        float: Final total rounded to 2 decimals.
    """
    total = 0.0
    
    # TODO: Implement complex billing logic
    for procedure in procedures:
        if procedure["status"] == "Cancelled":
            continue
        
        total += procedure["cost"]
        if procedure["is_emergency"]:
            total += procedure["cost"] * 0.2
    
    if total > 500:
        total *= 0.9
    
    return round(total, 2)

if __name__ == "__main__":
    ex_data = [
        {"service": "Lab", "cost": 100, "is_emergency": False, "status": "Done"},
        {"service": "X-Ray", "cost": 200, "is_emergency": True, "status": "Done"},
        {"service": "Admin", "cost": 50, "is_emergency": False, "status": "Cancelled"},
    ]
    # Expected: 100 + (200 + 40) = 340.0
    print(f"Final Bill: {calculate_bill(ex_data)}")
