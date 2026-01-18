---
title: "I/O & Utilities: Interacting with the World"
type: knowledge
module: language_fundamentals
unit: unit_1_10_io_and_utils
order: 10
difficulty: beginner
tags:
  subtopics:
    - input
    - f-strings
    - file-io
    - context-managers
---

# Unit 1.10: Input, Output & Basic Utilities

## 1. What
**Input/Output (I/O)** refers to the communication between a computer program and its external world (users, files, other programs). 

In healthcare, I/O is everywhere:
- **Input**: A clinician entering a patient's temperature.
- **Output**: A formatted PDF lab report.
- **Utilities**: Saving an encrypted log file of every time a record was accessed.

---

## 2. Example

### Example 1: Collecting and Processing Input
```python
# input() always returns a string!
age_str = input("Enter patient age: ")
age_int = int(age_str) # Type casting is required for math
print(f"Patient will be {age_int + 1} next year.")
```

### Example 2: Professional Formatting (f-strings)
```python
name = "Jane Doe"
bmi = 22.4567
# :.2f limits to 2 decimal places
# :>20 aligns right with 20 spaces of padding
print(f"Patient: {name:>20}")
print(f"BMI:     {bmi:.2f}")
```

### Example 3: Basic File Writing (Persistence)
```python
# 'w' mode overwrites, 'a' mode appends
with open("encounter_notes.txt", "w") as file:
    file.write("Encounter Date: 2023-10-27\n")
    file.write("Patient reported mild headache.\n")
# File is automatically closed when the block ends
```

### Example 4: Basic File Reading
```python
with open("encounter_notes.txt", "r") as file:
    content = file.read()
    print("Record loaded:")
    print(content)
```

---

## 3. Explanation

### The `input()` function
- Stops the program and waits for the user to type something.
- **Critical Note**: Even if the user types `10`, Python receives `"10"` (a string). You must convert it using `int()` or `float()` to do math.

### The `print()` function
- Displays information to the console.
- **`sep` argument**: Sets the character between multiple items (default is space).
- **`end` argument**: Sets the character at the end of the line (default is `\n` or newline).

### File Context Managers (`with`)
- Using `with open(...)` is the standard "Best Practice."
- It manages the lifecycle of the file. If your program crashes inside the `with` block, Python still ensures the file is closed and saved correctly.

### Modes for `open()`
- `'r'`: Read (default). Errors if file doesn't exist.
- `'w'`: Write. Overwrites existing content. Creates file if missing.
- `'a'`: Append. Adds to the end of existing content.

---

## 4. Why

### Persistence
Without file I/O, all data is lost the moment the program closes. To built an EHR, you *must* save data to disk.

### Professionalism
Standard `print("Total:", cost)` is okay for debugging, but `print(f"Total: ${cost:10.2f}")` is what makes medical software look reliable and trustworthy.

### User Autonomy
Interactive input allows clinical staff to perform different calculations (different dosages, different patients) without a developer having to change the code.

---

## 5. Advantages & Disadvantages

### Advantages
- **Flexibility**: Programs can handle different data sets every time they run.
- **Auditability**: File logs create a "paper trail" for medical actions.
- **Communication**: Clean output allows humans to make better clinical decisions.

### Disadvantages
- **Erroneous Input**: Users might type "ten" instead of "10", causing a crash.
- **File System Errors**: Permissions, full disks, or missing files can cause runtime exceptions.
- **Security**: Improperly formatted output could leak sensitive PII (Personally Identifiable Information).

---

## 6. Real-World Use Cases

### Case 1: Triage Intake CLI
A simple command-line script for emergency room greeting staff.
```python
name = input("Patient Name: ")
reason = input("Reason for visit: ")
with open("triage_queue.txt", "a") as log:
    log.write(f"{name} | {reason}\n")
```

### Case 2: Lab Summary Generator
Formatting a table of results for a clinician.
```python
print(f"{'TEST':<15} | {'RESULT':<10} | {'STATUS':<10}")
print("-" * 40)
print(f"{'Glucose':<15} | {95:<10} | {'NORMAL':<10}")
```

---

## 7. Best Practices

### Best Practice 1: Input Validation
Always wrap `input()` in a `try/except` if you plan to convert it to a number.
```python
try:
    temp = float(input("Enter temperature: "))
except ValueError:
    print("Error: Please enter a numeric value.")
```

### Best Practice 2: Use Descriptive File Names
Use naming conventions that include dates or Patient IDs to keep the file system organized.

### Best Practice 3: Strip Whitespace
User input often has accidental spaces. Use `.strip()` to clean it.
```python
choice = input("Enter (Y/N): ").strip().upper()
```

---

## 8. Top 3 Mistakes

### Error 1: Forgetting to Convert Input
```python
val = input("Value: ")
result = val * 2 # If input was 5, result is "55", not 10!
```

### Error 2: "File Not Found" Crashes
Trying to read a file that hasn't been created yet. Always use a `try/except FileNotFoundError` for reading operations.

### Error 3: Hardcoding File Paths
```python
# Bad: Won't work on anyone else's computer
open("C:\\Users\\Bob\\Desktop\\data.txt") 

# Good: Works anywhere within the project folder
open("data.txt") 
```
