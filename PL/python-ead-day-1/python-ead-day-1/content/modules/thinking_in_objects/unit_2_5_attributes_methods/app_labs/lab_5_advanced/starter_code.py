"""
Lab 5: The Equipment Maintenance Hub - Starter Code
"""

class Ventilator:
    # TODO: Define service_threshold
    service_threshold = 1000
    
    # TODO: Implement __init__, log_usage, and check_status
    def __init__(self, serial_no):
        self.serial_no = serial_no
        self.hours_run = 0
    
    def log_usage(self, hours):
        self.hours_run += hours
    
    def check_status(self):
        return self.hours_run >= Ventilator.service_threshold

def main():
    print("--- BioMed Maintenance Hub ---")
    # TODO: Create devices, log hours, and change the global threshold
    v1 = Ventilator("SN001")
    v2 = Ventilator("SN002")
    v1.log_usage(900)
    print(f"Status before threshold change: {v1.check_status()}")
    Ventilator.service_threshold = 800
    print(f"Status after threshold change: {v1.check_status()}")

if __name__ == "__main__":
    main()
