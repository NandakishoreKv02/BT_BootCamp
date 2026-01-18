"""
Lab 1: The Abstract Device Blueprint - Starter Code
"""
# TODO: Import ABC module

class MedicalDevice: # TODO: Inherit correctly
    # TODO: Implement @abstractmethod operate()
    
    def get_status(self):
        return "System Ready"

def main():
    print("--- Hardware Security Check ---")
    # TODO: Test that MedicalDevice cannot be instantiated
    pass

if __name__ == "__main__":
    main()
