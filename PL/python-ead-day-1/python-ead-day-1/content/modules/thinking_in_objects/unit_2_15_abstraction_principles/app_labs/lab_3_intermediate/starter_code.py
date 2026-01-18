"""
Lab 3: The SRP Billing Refactor - Starter Code
"""

# THE "GOD CLASS" TO BE REFACTORED:
class PatientBillingOfficer:
    def __init__(self, name, services):
        self.name = name
        self.services = services # List of dicts: {"name": "X", "price": 0}

    def process(self):
        # 1. Calculation
        total = 0
        for s in self.services: total += s["price"]
        
        # 2. Rendering
        return f"Account: {self.name}\nTotal Due: ${total}"

# TODO: Refactor into 3 SRP classes:
class PatientProfile:
    pass

class CostCalculator:
    pass

class StatementRenderer:
    pass

def main():
    print("--- Billing System v2.0 ---")
    # TODO: Coordinate the 3 new classes to produce a statement
    pass

if __name__ == "__main__":
    main()
