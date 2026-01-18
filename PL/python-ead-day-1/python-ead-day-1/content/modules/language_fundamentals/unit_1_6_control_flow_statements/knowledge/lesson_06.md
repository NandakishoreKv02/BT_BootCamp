---
title: "Control Flow: The Decision-Making Core"
type: knowledge
module: language_fundamentals
unit: unit_1_6_control_flow_statements
order: 6
difficulty: beginner
tags:
  subtopics:
    - if-elif-else
    - for-loops
    - while-loops
    - range
    - break-continue
---

# Unit 1.6: Control Flow Statements

## 1. What
**Control Flow** refers to the order in which a program's code executes. By default, code runs line-by-line from top to bottom. Control flow statements allow you to change this path by:
- **Conditionals**: Executing code only if a condition is met (`if`).
- **Loops**: Repeating code multiple times (`for`, `while`).
- **Interrupts**: Stopping or skipping parts of a loop (`break`, `continue`).

In healthcare, control flow allows systems to automate triage, monitor patient vitals continuously, and process large batches of lab results efficiently.

---

## 2. Example

### Example 1: Basic Conditionals (Triage)
```python
temperature = 38.5

if temperature >= 39.0:
    status = "High Fever"
elif temperature >= 38.0:
    status = "Fever"
else:
    status = "Normal"

print(f"Patient Status: {status}")
```

### Example 2: For Loop with Range (Dose Scheduling)
```python
# Schedule 3 doses
for dose_num in range(1, 4):
    print(f"Preparing dose #{dose_num}...")
```

### Example 3: While Loop (Polling a Sensor)
```python
import time

reading_count = 0
while reading_count < 5:
    print("Collecting blood pressure reading...")
    reading_count += 1
    time.sleep(1) # Simulation
```

### Example 4: Break and Continue
```python
vitals = [72, 75, 0, 80, 110] # 0 represents a sensor error

for hr in vitals:
    if hr == 0:
        continue # Skip the error reading
    if hr > 100:
        print(f"Warning: Tachycardia detected ({hr} BPM)")
        break # Exit search after first warning
```

---

## 3. Explanation

### If Statement Structure
The `if` statement evaluates a Boolean expression. Optional `elif` (else if) branches handle alternative cases, and the `else` catch-all handles everything else.
- **Indentation is mandatory**: Python uses 4 spaces to define the block of code inside a conditional or loop.

### For vs. While
- **`for` loop**: Used for **definite iteration**. You know exactly how many items you are iterating over (a list, a range, etc.).
- **`while` loop**: Used for **indefinite iteration**. It keeps running as long as a condition is `True`. **Warning**: Always ensure the condition eventually becomes `False` to avoid infinite loops.

### Range Deep Dive
`range(start, stop, step)`
- `range(5)` -> 0, 1, 2, 3, 4 (Stop is exclusive)
- `range(1, 6)` -> 1, 2, 3, 4, 5
- `range(0, 10, 2)` -> 0, 2, 4, 6, 8

---

## 4. Why

### Why Conditionals?
- **Clinical Decision Support**: To categorize a patient's risk based on multiple vitals.
- **Data Validation**: To ensure a patient's age is within a reasonable range before saving a record.

### Why Loops?
- **Efficiency**: Instead of writing `print(patient_1)`, `print(patient_2)`, etc., you write one loop that handles 10,000 patients.
- **Continuous Monitoring**: Systems that monitor SPO2 or Heart Rate often use a `while True` loop to never stop checking for anomalies.

---

## 5. Advantages & Disadvantages

### Advantages
- **Reusability**: Loops let you apply the same logic to many inputs.
- **Logical Branching**: Conditionals make programs "smart" by reacting differently to different data.
- **Readability**: Python's `if/else` syntax is closer to human language than many other languages.

### Disadvantages
- **Nesting Complexity**: Deeply nested `if` statements (pyramid of doom) are hard to read and debug.
- **Infinite Loops**: A bug in a `while` loop condition can crash a system or consume 100% CPU.
- **Performance**: Very large loops can be slow in Python compared to compiled languages like C++.

---

## 6. Real-World Use Cases

### Case 1: Pediatric Weight Triage
```python
weight = 15.0

if weight < 5:
    drug_class = "Neonatal"
elif 5 <= weight < 18:
    drug_class = "Pediatric"
else:
    drug_class = "Standard"
```

### Case 2: Batch Processing Lab Results
```python
results = [{"test": "Glucose", "value": 110}, {"test": "Iron", "value": 50}]

for result in results:
    if result["value"] > 100:
        print(f"High result in {result['test']}")
```

### Case 3: Waiting for Lab Integration
```python
lab_received = False
attempts = 0

while not lab_received and attempts < 10:
    print("Checking lab server...")
    # ... logic to check server ...
    attempts += 1
```

---

## 7. Best Practices

### Best Practice 1: Keep Nesting Shallow
**Why**: Deep nesting (more than 3 levels) makes code impossible to maintain. Use "Guard Clauses" (returning early) to flatten logic.
```python
# Bad
if user_logged_in:
    if has_permission:
        if record_exists:
             # Logic

# Good (Guard Clauses)
if not user_logged_in: return
if not has_permission: return
# Logic
```

### Best Practice 2: Use `range()` for Simple Counters
**Why**: It's more memory-efficient than creating a full list of numbers.

### Best Practice 3: Avoid `break` unless Necessary
**Why**: Overusing `break` can make the loop exit point hard to track. Use it when searching or when an unrecoverable error occurs.

---

## 8. Top 3 Mistakes

### Mistake 1: The Infinite "While"
#### Improper Code
```python
count = 0
while count < 5:
    print("Running...")
    # Missing count += 1!
```
#### Correction
Always update your iterator variable inside the loop.

### Mistake 2: Off-by-One with `range()`
#### Improper Code
```python
# Goal: Print numbers 1 to 10
for i in range(1, 10): 
    # Only prints 1 to 9!
```
#### Correction
The `stop` value is exclusive. Use `range(1, 11)`.

### Mistake 3: Repeating `if` instead of `elif`
#### Improper Code
```python
temp = 40
if temp > 38: print("Fever")
if temp > 39: print("High Fever")
# Output:
# Fever
# High Fever (Both execute!)
```
#### Correction
Use `elif` when conditions are mutually exclusive.
