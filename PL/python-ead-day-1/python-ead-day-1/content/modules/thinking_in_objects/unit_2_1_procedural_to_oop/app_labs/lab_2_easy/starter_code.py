"""
Lab 2: The Parallel Lab Results - Starter Code
"""

# --- BAD PROCEDURAL CODE ---
pids = ["P001", "P002", "P003"]
tests = ["Glucose", "Cholesterol", "Iron"]
values = [95, 190, 50]

def print_raw_report():
    for i in range(len(pids)):
        print(f"Patient: {pids[i]} | Test: {tests[i]} | Value: {values[i]}")

# ---------------------------

# TODO: Define create_lab_result(pid, test_name, value)

# TODO: Define update_result(result, new_value)

# TODO: Define print_lab_report(results)

def main():
    print("--- Old Procedural Report ---")
    print_raw_report()

    # TODO: Create the new 'results' list using create_lab_result()
    
    # TODO: Update P002's Cholesterol to 180
    
    print("\n--- New Object-Oriented Report ---")
    # TODO: Call print_lab_report()

if __name__ == "__main__":
    main()
