# Lab 3: Encounter Log Append Utility - Tasks

## Task 1: The Context Manager
Use `with open(filename, "a") as file:` to open the target file for appending.

## Task 2: String Construction
Use an f-string to create the message: `{user_id} accessed {patient_id}\n`.

## Task 3: Writing
Call `file.write(message)`.

## Task 4: Verification
In the `if __name__ == "__main__":` block, call the function twice for the same file and check that the file now contains two lines.
