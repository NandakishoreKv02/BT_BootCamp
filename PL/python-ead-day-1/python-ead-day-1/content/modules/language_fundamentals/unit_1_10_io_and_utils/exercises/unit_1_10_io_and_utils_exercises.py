"""
Unit 1.10: I/O & Basic Utilities - Exercises
Practice with input, output formatting, and file handling.
"""

import os

# ============================================================================
# Exercise 1: Input & Casting
# ============================================================================

def calculate_age_next_year(current_age_input):
    """
    TODO: current_age_input is a string from input().
    Convert it to an integer, add 1, and return the result.
    If conversion fails, return 0.
    """
    # TODO: Implement conversion and increment
    try:
        return int(current_age_input) + 1
    except ValueError:
        return 0


# ============================================================================
# Exercise 2: F-String Padding (Lab Labels)
# ============================================================================

def format_lab_label(test_name, result):
    """
    TODO: Return a string formatted with padding.
    The test_name should be left-aligned in a 15-character field.
    The result should be right-aligned in a 10-character field with 2 decimals.
    Example: "Glucose         |      95.50"
    """
    # TODO: Implement f-string with formatting codes
    return f"{test_name:<15}|{result:>10.2f}"


# ============================================================================
# Exercise 3: File Writing (Shift Notes)
# ============================================================================

def save_note_to_file(filename, note_text):
    """
    TODO: Write the note_text to the specified filename.
    Use the 'with' statement.
    """
    # TODO: Implement 'with open...' to write
    with open(filename, 'w') as f:
        f.write(note_text)


# ============================================================================
# Exercise 4: File Reading (History Loader)
# ============================================================================

def read_first_line(filename):
    """
    TODO: Read the first line of the file and return it.
    Use try/except to handle FileNotFoundError. Return "File Missing" on error.
    """
    # TODO: Implement file read with error handling
    try:
        with open(filename, 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        return "File Missing"


# ============================================================================
# Exercise 5: Command-line Argument Awareness
# ============================================================================

def check_args_count(args_list):
    """
    TODO: args_list is sys.argv (a list of strings).
    Return the number of arguments passed (excluding the script name).
    """
    # TODO: Return count
    return len(args_list) - 1


# ============================================================================
# Exercise 6: Interactive Menu Wrapper
# ============================================================================

def process_menu_choice(choice_str):
    """
    TODO: choice_str is from input().
    - Strip whitespace.
    - Convert to uppercase.
    - If "Q", return "EXITING".
    - Else, return "STAYING".
    """
    # TODO: Implement strip/upper logic
    choice = choice_str.strip().upper()
    if choice == "Q":
        return "EXITING"
    return "STAYING"


# ============================================================================
# Test Runner
# ============================================================================

def test_runner():
    print("Running Unit 1.10 Exercises...")
    passed = 0
    total = 6

    # Test 1
    try:
        if calculate_age_next_year("25") == 26 and calculate_age_next_year("abc") == 0:
            print("PASS: Exercise 1")
            passed += 1
        else:
            print("FAIL: Exercise 1")
    except Exception as e:
        print(f"ERROR: Exercise 1 - {e}")

    # Test 2
    try:
        res = format_lab_label("Sodium", 140.5)
        if "Sodium" in res and "140.50" in res and "|" in res:
            print("PASS: Exercise 2")
            passed += 1
        else:
            print(f"FAIL: Exercise 2 - Got '{res}'")
    except Exception as e:
        print(f"ERROR: Exercise 2 - {e}")

    # Test 3 & 4
    fname = "test_note.txt"
    try:
        save_note_to_file(fname, "Line 1\nLine 2")
        if os.path.exists(fname) and "Line 1" in read_first_line(fname):
            print("PASS: Exercises 3 & 4")
            passed += 2
        else:
            print("FAIL: Exercises 3 or 4")
        if read_first_line("non_existent.txt") == "File Missing":
            passed += 0 # Just verifying the error handler
        else:
            print("FAIL: Exercise 4 (Error Handling)")
            passed -= 1 # Penalty for missing error handler
    except Exception as e:
        print(f"ERROR: Exercise 3/4 - {e}")
    finally:
        if os.path.exists(fname): os.remove(fname)

    # Test 5
    try:
        if check_args_count(["script.py", "arg1", "arg2"]) == 2:
            print("PASS: Exercise 5")
            passed += 1
        else:
            print("FAIL: Exercise 5")
    except Exception as e:
        print(f"ERROR: Exercise 5 - {e}")

    # Test 6
    try:
        if process_menu_choice("  q  ") == "EXITING" and process_menu_choice("c") == "STAYING":
            print("PASS: Exercise 6")
            passed += 1
        else:
            print("FAIL: Exercise 6")
    except Exception as e:
        print(f"ERROR: Exercise 6 - {e}")

    print(f"\nResult: {passed}/{total} tests passed.")

if __name__ == "__main__":
    test_runner()
