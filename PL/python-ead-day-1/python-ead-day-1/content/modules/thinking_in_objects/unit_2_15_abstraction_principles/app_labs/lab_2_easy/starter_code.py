"""
Lab 2: Enforcing the Scanning Protocol - Starter Code
"""
from abc import ABC, abstractmethod

class MedicalDevice(ABC):
    @abstractmethod
    def operate(self):
        pass
    
    def get_status(self):
        return "System Ready"

# TODO: Implement InfusionPump
class InfusionPump:
    pass

# TODO: Implement HeartMonitor
class HeartMonitor:
    pass

def main():
    print("--- Diagnostic Tool Launch ---")
    # TODO: Demonstrate both devices
    pass

if __name__ == "__main__":
    main()
