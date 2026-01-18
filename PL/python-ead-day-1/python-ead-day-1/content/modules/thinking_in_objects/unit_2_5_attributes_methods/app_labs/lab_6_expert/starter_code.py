"""
Lab 6: The Clinical Data Aggregator - Starter Code
"""

class PatientMetric:
    # TODO: Define class attributes for sum and count
    all_hr_sum = 0
    total_patients = 0
    
    # TODO: Implement __init__, record_heart_rate, and get_average_bpm
    def __init__(self, name):
        self.name = name
        self.reading = 0
        PatientMetric.total_patients += 1
    
    def record_heart_rate(self, bpm):
        self.reading = bpm
        PatientMetric.all_hr_sum += bpm
    
    @staticmethod
    def get_average_bpm():
        if PatientMetric.total_patients == 0:
            return 0
        return PatientMetric.all_hr_sum / PatientMetric.total_patients

def main():
    print("--- Population Health Aggregator ---")
    # TODO: Demonstrate aggregation across multiple objects
    bob = PatientMetric("Bob")
    alice = PatientMetric("Alice")
    bob.record_heart_rate(80)
    alice.record_heart_rate(100)
    print(f"Average BPM: {PatientMetric.get_average_bpm()}")
    charlie = PatientMetric("Charlie")
    charlie.record_heart_rate(60)
    print(f"Average BPM: {PatientMetric.get_average_bpm()}")

if __name__ == "__main__":
    main()
