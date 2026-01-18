# Lab 4: Clinical Protocol Loader - Tasks

## Task 1: The Trap
Wrap the entire file reading logic in a `try...except FileNotFoundError:` block.

## Task 2: Reading
Use `with open(filename, "r") as file:` to open the file.

## Task 3: Processing Lines
Read the lines and use a list comprehension or a loop to `.strip()` each one.

## Task 4: Return
Return the cleaned list on success, or `[]` on failure.
