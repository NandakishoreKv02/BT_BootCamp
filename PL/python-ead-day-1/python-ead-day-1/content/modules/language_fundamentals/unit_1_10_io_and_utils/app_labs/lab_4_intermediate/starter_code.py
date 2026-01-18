"""
Lab 4: Clinical Protocol Loader - Solution
"""

def load_protocol(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    # Create dummy file for demonstration
    with open("sepsis_steps.txt", "w") as f:
        f.write("Administer Fluids\nStart Antibiotics\nMonitor Vitals\n")
    
    print(load_protocol("sepsis_steps.txt"))
