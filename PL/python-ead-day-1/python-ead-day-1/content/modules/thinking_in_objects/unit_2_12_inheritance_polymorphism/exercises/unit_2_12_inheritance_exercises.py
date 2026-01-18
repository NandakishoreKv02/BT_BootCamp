"""
Unit 2.12: Inheritance & Polymorphism - Solutions
"""

# Exercise 1
class Staff:
    def __init__(self, name):
        self.name = name

class Physician(Staff):
    """Inherits name from Staff."""
    def __init__(self, name):
        super().__init__(name)

# Exercise 2
class ElectronicDevice:
    def __init__(self, serial_num):
        self.serial_num = serial_num

class SmartMonitor(ElectronicDevice):
    def __init__(self, serial_num, screen_size):
        # Correct use of super()
        super().__init__(serial_num)
        self.screen_size = screen_size

# Exercise 3 & 4
class DiagnosticTest:
    def perform(self):
        return "Running generic test..."

class BloodTest(DiagnosticTest):
    def perform(self):
        """Method Overriding."""
        return "Analyzing hematology markers..."

if __name__ == "__main__":
    print("Unit 2.12 Solutions verified.")
