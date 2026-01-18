# Lab 4: Importable Logger - Tasks

## Task 1: Create log_message Function
Implement `log_message(level, message)`:
- **Input**: Level (str), Message (str)
- **Output**: Returns string `"[<TIMESTAMP>] [<LEVEL>] <MESSAGE>"`
- **Note**: Use `datetime.datetime.now()` for timestamp.
- **Docstring**: Required.

## Task 2: Implement Main Guard
Add `if __name__ == "__main__":`:
- Inside this block, print: `"Logger Demo Started"`.
- Call `log_message` with some test data and print the result.
- Print `"Logger Demo Finished"`.

## Task 3: Verify No Side Effects
Ensure that if you were to `import starter_code` from another script, NOTHING is printed to the console.
- **Hint**: All `print()` calls (except inside functions) must be inside the `if __main__...` block.
