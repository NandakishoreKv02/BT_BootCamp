"""
Lab 1: The Patient State Tracker - Starter Code
"""

class PatientState:
    # TODO: Implement __init__ to store pid, hr, and temp
    def __init__(self, pid, hr, temp):
        self.pid = pid
        self.hr = hr
        self.temp = temp

def main():
    print("--- ER State Monitor ---")
    # TODO: Create p1 and p2
    p1 = PatientState(101, 72, 98.6)
    p2 = PatientState(102, 85, 99.1)
    # TODO: Demonstrate independence of instance attributes
    print(f"p1 HR: {p1.hr}, p2 HR: {p2.hr}")
    p1.hr = 100
    print(f"p1 HR: {p1.hr}, p2 HR: {p2.hr}")

if __name__ == "__main__":
    main()
