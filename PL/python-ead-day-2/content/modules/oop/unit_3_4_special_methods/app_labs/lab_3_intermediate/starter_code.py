"""
Starter Code - Reset
"""
'Lab 3: Solution - Priority Queue'
from functools import total_ordering

@total_ordering
class TriagePatient:

    def __init__(self, patient_id: str, name: str, urgency: int):
        # TODO: Implement logic
        pass

    def __eq__(self, other):
        # TODO: Implement logic
        pass

    def __lt__(self, other):
        # TODO: Implement logic
        pass

    def __repr__(self):
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    patients = [TriagePatient('P001', 'Alice', 3), TriagePatient('P002', 'Bob', 1), TriagePatient('P003', 'Carol', 2)]
    for p in sorted(patients):
        print(p)