"""
Lab 4: The Cohesive Lab Report - Starter Code

TODO: List non-cohesive methods that don't belong here:
1. send_marketing_email
2. calculate_parking_fees
"""

class LabReport:
    # TODO: Implement __init__, add_result, and is_abnormal
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.results = {}
    
    def add_result(self, test_name, value):
        self.results[test_name] = value
    
    def is_abnormal(self):
        return self.results.get("Glucose", 0) > 125

def main():
    print("--- Lab Result System ---")
    # TODO: Create report, add data, and check status
    report = LabReport(505)
    report.add_result("Glucose", 140)
    print(f"Abnormal: {report.is_abnormal()}")

if __name__ == "__main__":
    main()
