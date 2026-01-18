"""
Lab 3: Breaking the God Object - Starter Code
"""

# LEGACY GOD OBJECT (Do not use this in your final solution)
class HospitalApp:
    def __init__(self, p_name, bed_num, days):
        self.p_name = p_name
        self.bed_num = bed_num
        self.days = days
        self.bill = 0
    
    def calculate_bill(self): return self.days * 100
    def get_summary(self): return f"{self.p_name} @ Bed {self.bed_num}"

# TODO: Refactor the above into THREE separate classes

class Patient:
    pass

class Ward:
    pass

class BillingEngine:
    pass

def main():
    # TODO: Demonstrate the refactored workflow
    pass

if __name__ == "__main__":
    main()
