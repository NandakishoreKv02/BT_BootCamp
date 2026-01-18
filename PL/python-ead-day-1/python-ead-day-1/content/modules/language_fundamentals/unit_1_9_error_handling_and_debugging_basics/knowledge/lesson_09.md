---
title: "Error Handling: Building Resilient Systems"
type: knowledge
module: language_fundamentals
unit: unit_1_9_error_handling_and_debugging_basics
order: 9
difficulty: beginner
tags:
  subtopics:
    - try-except
    - exceptions
    - tracebacks
    - debugging
---

# Unit 1.9: Error Handling & Debugging Basics

## 1. What
**Error Handling** is the process of anticipating and responding to errors in your code. In Python, runtime errors are called **Exceptions**.

In healthcare software, error handling is critical. Imagine a script processing a batch of 1,000 lab results. If result #45 has a typo (e.g., "1OO" instead of "100"), you don't want the entire program to crash. You want the program to log the error for that one result and continue processing the remaining 955.

---

## 2. Example

### Example 1: Basic Try/Except
```python
raw_reading = "invalid"

try:
    value = float(raw_reading)
    print(f"Reading: {value}")
except ValueError:
    print("Error: Patient reading was not a valid number.")
```

### Example 2: Handling Missing Data
```python
patient = {"name": "Doe^John"}

try:
    print(patient["mrn"])
except KeyError:
    print("Error: MRN is missing from the record.")
```

### Example 3: Else and Finally
```python
try:
    print("Attempting to connect to LIS database...")
    # imaginary_database.connect()
except ConnectionError:
    print("Failed to connect.")
else:
    print("Connection successful!")
finally:
    print("Closing log entry...") # Always runs
```

---

## 3. Explanation

### Types of Errors
1.  **Syntax Errors**: The "grammatical" errors. Python can't even start the program. (e.g., missing a colon `:`).
2.  **Exceptions (Runtime Errors)**: The program starts, but something goes wrong while running. (e.g., dividing by zero).

### The Try/Except Workflow
- **`try`**: Put the code that might fail here.
- **`except`**: If an error happens in the `try` block, Python jumps here immediately.
- **`else`**: Runs only if the `try` block was successful (no error).
- **`finally`**: Runs no matter what. Used for "cleanup" (like closing files).

### Common Exceptions
- **`ValueError`**: Right type, but wrong value (e.g., `float("abc")`).
- **`TypeError`**: Wrong type (e.g., `5 + "10"`).
- **`ZeroDivisionError`**: Dividing by zero.
- **`IndexError`**: Accessing an index that doesn't exist in a list.
- **`KeyError`**: Accessing a key that doesn't exist in a dictionary.

---

## 4. Why

### Reliability
Proper error handling prevents your app from being "brittle." One piece of bad data shouldn't bring down the whole system.

### User Experience
Users should see friendly messages ("Invalid date format") instead of scary technical tracebacks (`ValueError: could not convert string to float...`).

### Security
Exposing raw tracebacks in a live application can reveal sensitive information about your code structure to unauthorized users.

---

## 5. Advantages & Disadvantages

### Advantages
- **Control**: You decide what happens when things go wrong.
- **Continuity**: Loops can continue even if one iteration fails.
- **Resource Management**: `finally` ensuring files and connections are closed.

### Disadvantages
- **Complexity**: Over-using try/except can make code harder to follow.
- **Performance**: Try blocks have a very small overhead (though negligible in most cases).
- **Masking Bugs**: If you catch "All Errors" (`except Exception:`), you might hide real logic bugs that you *should* have fixed.

---

## 6. Real-World Use Cases

### Case 1: Vital Sign Intake
Handling user input from a bedside monitor that might be poorly formatted.
```python
def process_hr(input_str):
    try:
        return int(input_str)
    except ValueError:
        return 0 # Default safe value
```

### Case 2: Lab Result Aggregator
Running a loop through results and skipping the "broken" ones.
```python
for result in results_list:
    try:
        calculate_average(result)
    except ZeroDivisionError:
        print(f"Skipping empty result set for {result['id']}")
        continue
```

---

## 7. Best Practices

### Best Practice 1: Be Specific
Always name the exception you want to catch.
```python
# Bad - catches EVERY error, including stuff you didn't expect
except: 

# Good - only catches the error you know how to handle
except ValueError: 
```

### Best Practice 2: The "Keep it Small" Rule
Only put the lines of code that *actually* might fail inside the `try` block. Everything else goes before or after.

### Best Practice 3: Log Errors
Instead of just "swallowing" an error, print it or log it so developers can find it later.

---

## 8. Debugging Techniques

### The Traceback
When Python crashes, it prints a **Traceback**.
1.  **Bottom Line**: Tells you the error type and message.
2.  **Top/Middle**: Tells you the file and line number where it happened.

### Print Debugging
The most common technique! Use `print()` to see:
- "Did I reach this line?" (`print("Reached point A")`)
- "What is the value of this variable right now?" (`print(f"Current weight: {w}")`)

### The 4-Step Mindset
1.  **Reproduce**: Can you make the error happen again? 
2.  **Isolate**: Which exact line is failing?
3.  **Fix**: Apply the solution.
4.  **Verify**: Does it work now? Did you break anything else?
