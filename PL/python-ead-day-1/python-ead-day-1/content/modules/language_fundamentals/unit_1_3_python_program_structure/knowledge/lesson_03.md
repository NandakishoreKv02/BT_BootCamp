---
title: "Python Program Structure: Building Well-Organized Code"
type: knowledge
module: language_fundamentals
unit: unit_1_3_python_program_structure
order: 3
difficulty: beginner
tags:
  subtopics:
    - script-structure
    - indentation
    - comments-docstrings
    - main-guard
    - modules-vs-scripts
---

# Unit 1.3: Python Program Structure

## 1. What
Python program structure refers to how code is organized and formatted in a Python file. Unlike languages like C++ or Java that use braces `{}` to define code blocks, Python uses **indentation** (whitespace) to determine the structure of the code. This makes Python code highly readable but requires strict adherence to formatting rules.

Key structural elements include:
- **Indentation**: Defines code blocks (functions, loops, conditionals)
- **Comments**: Explanatory text for developers (`#` for single-line)
- **Docstrings**: Documentation strings for functions/modules (`"""..."""`)
- **`__main__` guard**: Makes scripts importable without executing code
- **Module structure**: Organizing code into reusable components

---

## 2. Example

### Example 1: Basic Script Structure
```python
"""
patient_manager.py
A module for managing patient records in a healthcare system.
"""

# Standard library imports
import datetime

# Constants
MAX_PATIENTS = 1000
DEFAULT_STATUS = "Active"

# Function definitions
def register_patient(name, age):
    """
    Register a new patient in the system.
    
    Args:
        name (str): Patient's full name
        age (int): Patient's age in years
    
    Returns:
        dict: Patient record with ID and timestamp
    """
    patient = {
        "name": name,
        "age": age,
        "status": DEFAULT_STATUS,
        "registered_at": datetime.datetime.now()
    }
    return patient

# Main execution block
if __name__ == "__main__":
    # This code only runs when script is executed directly
    patient = register_patient("John Doe", 45)
    print(f"Registered: {patient['name']}")
```

### Example 2: Indentation Levels
```python
def check_vital_signs(temperature, heart_rate):
    """Check if vital signs are within normal range."""
    # Level 1 indentation (inside function)
    if temperature > 38.0:
        # Level 2 indentation (inside if)
        if heart_rate > 100:
            # Level 3 indentation (nested if)
            return "Critical - High fever and tachycardia"
        else:
            return "Warning - High fever"
    elif heart_rate > 100:
        return "Warning - Tachycardia"
    else:
        return "Normal"
```

### Example 3: Comments vs Docstrings
```python
# This is a comment - explains implementation details for developers
# Comments are ignored by Python and don't appear in help()

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    This is a docstring - it documents the function for users.
    It appears when you call help(calculate_bmi).
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    """
    # Implementation comment: Using standard BMI formula
    bmi = weight / (height ** 2)
    return round(bmi, 2)
```

### Example 4: Module vs Script
```python
# utils.py - A reusable module
def format_patient_id(id_number):
    """Format patient ID with leading zeros."""
    return f"PAT-{id_number:05d}"

# This code only runs when executed directly, not when imported
if __name__ == "__main__":
    # Test the function
    print(format_patient_id(42))  # Output: PAT-00042
```

```python
# main.py - A script that imports the module
from utils import format_patient_id

# When we import utils, the test code doesn't run
# because of the __main__ guard
patient_id = format_patient_id(123)
print(patient_id)  # Output: PAT-00123
```

---

## 3. Explanation

### Why Indentation Matters
Python's creator, Guido van Rossum, chose indentation to enforce readable code. In other languages, you can write:
```java
// Java - braces allow poor formatting
if (condition) { doSomething(); doSomethingElse(); }
```

In Python, this is impossible:
```python
# Python - indentation forces clarity
if condition:
    do_something()
    do_something_else()
```

### How `__name__` Works
Every Python file has a special variable called `__name__`:
- When you **run** a file: `__name__ == "__main__"`
- When you **import** a file: `__name__ == "module_name"`

This allows you to write code that behaves differently based on how it's used.

### Docstring Conventions (PEP 257)
1. **One-line docstrings**: For simple functions
   ```python
   def add(a, b):
       """Return the sum of a and b."""
       return a + b
   ```

2. **Multi-line docstrings**: For complex functions
   ```python
   def process_lab_results(results):
       """
       Process laboratory test results.
       
       This function validates, normalizes, and stores lab results
       in the database. It also triggers alerts for abnormal values.
       
       Args:
           results (dict): Raw lab results from analyzer
       
       Returns:
           bool: True if processing succeeded
       
       Raises:
           ValueError: If results format is invalid
       """
       pass
   ```

---

## 4. Why

### Why Indentation-Based Syntax?
1. **Readability**: Forces consistent formatting across all Python code
2. **Less Clutter**: No need for braces or `end` keywords
3. **Fewer Bugs**: Mismatched braces are a common error in C/Java

### Why Docstrings Matter in Healthcare
In medical software:
- **Regulatory Compliance**: FDA requires documented code
- **Team Collaboration**: New developers must understand critical functions
- **Safety**: Clear documentation prevents misuse of dosage calculators or diagnostic tools
- **Maintenance**: Future developers need to understand complex algorithms

### Why Use `__main__` Guard?
Without it:
```python
# bad_module.py
print("Initializing...")  # This runs on import!

def useful_function():
    return 42
```

```python
# main.py
import bad_module  # Prints "Initializing..." unexpectedly!
```

With it:
```python
# good_module.py
def useful_function():
    return 42

if __name__ == "__main__":
    print("Testing...")  # Only runs when executed directly
```

---

## 5. Advantages & Disadvantages

### Advantages
- **Enforced Readability**: All Python code looks similar
- **Less Syntax**: No braces, semicolons, or `end` keywords
- **Self-Documenting**: Docstrings integrate with Python's `help()` system
- **Reusability**: `__main__` guard makes scripts importable

### Disadvantages
- **Whitespace Sensitivity**: Mixing tabs/spaces causes errors
- **Copy-Paste Issues**: Indentation can break when pasting code
- **Editor Dependency**: Need a good editor to manage indentation
- **Learning Curve**: Beginners struggle with indentation errors

---

## 6. Real-World Use Cases

### Case 1: Hospital Medication Module
```python
"""
medication.py
Handles medication dosage calculations and safety checks.
"""

def calculate_dosage(weight_kg, drug_name):
    """
    Calculate appropriate drug dosage based on patient weight.
    
    Critical function - changes require medical review.
    """
    # Dosage database (mg per kg)
    dosages = {
        "paracetamol": 15,
        "ibuprofen": 10
    }
    return weight_kg * dosages.get(drug_name, 0)

if __name__ == "__main__":
    # Safety tests run only during development
    assert calculate_dosage(70, "paracetamol") == 1050
    print("All safety checks passed")
```

### Case 2: Data Analysis Script
```python
"""
analyze_patient_data.py
Generates monthly reports from patient database.
"""

import pandas as pd

def load_patient_data(month):
    """Load patient records for specified month."""
    # Implementation here
    pass

def generate_report(data):
    """Create summary statistics report."""
    # Implementation here
    pass

if __name__ == "__main__":
    # Script execution logic
    data = load_patient_data("2024-01")
    report = generate_report(data)
    print(report)
```

### Case 3: Utility Module
```python
"""
validators.py
Reusable validation functions for healthcare data.
"""

def validate_patient_id(patient_id):
    """
    Validate patient ID format.
    
    Args:
        patient_id (str): ID to validate
    
    Returns:
        bool: True if valid
    
    Example:
        >>> validate_patient_id("PAT-00123")
        True
    """
    return patient_id.startswith("PAT-") and len(patient_id) == 9
```

---

## 7. Best Practices

### Best Practice 1: Use 4 Spaces for Indentation
**When to apply**: Always
**Why**: PEP 8 standard, prevents `TabError`
```python
# Configure your editor:
# VS Code: "editor.tabSize": 4, "editor.insertSpaces": true
# PyCharm: Settings → Editor → Code Style → Python → Tab size: 4
```

### Best Practice 2: Write Docstrings for All Public Functions
**When to apply**: Every function that will be used by others
**Why**: Enables `help()`, generates documentation
```python
def calculate_age(birth_date):
    """
    Calculate patient age from birth date.
    
    Args:
        birth_date (datetime): Patient's date of birth
    
    Returns:
        int: Age in years
    """
    pass
```

### Best Practice 3: Organize Imports Properly
**When to apply**: Every module
**Why**: PEP 8 compliance, readability
```python
# 1. Standard library imports
import os
import sys

# 2. Third-party imports
import pandas as pd
import numpy as np

# 3. Local application imports
from .models import Patient
from .utils import validate_id
```

### Best Practice 4: Use `__main__` Guard
**When to apply**: Any script that might be imported
**Why**: Prevents side effects on import
```python
def main():
    """Main execution function."""
    # Your code here
    pass

if __name__ == "__main__":
    main()
```

---

## 8. Top 3 Mistakes

### Mistake 1: Mixing Tabs and Spaces
#### What's the Problem?
Using both tabs and spaces for indentation in the same file.

#### Impact
Causes `TabError: inconsistent use of tabs and spaces in indentation`


#### Incorrect Approach
```python
def process_data():
    # This line uses 4 spaces
    data = load_data()
	# This line uses a tab - ERROR!
	return data
```

#### Correct Approach
```python
def process_data():
    # All lines use 4 spaces
    data = load_data()
    return data
```

**Fix**: Configure your editor to convert tabs to spaces automatically.

### Mistake 2: Missing Docstrings
#### What's the Problem?
Not documenting functions, especially complex or critical ones.

#### Impact
- Other developers don't understand the function
- `help()` returns no useful information
- Fails code review in professional settings

#### Incorrect Approach
```python
def calc(w, h):
    return w / (h ** 2)
```

#### Correct Approach
```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index.
    
    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters
    
    Returns:
        float: BMI value
    """
    return weight_kg / (height_m ** 2)
```

### Mistake 3: No `__main__` Guard
#### What's the Problem?
Putting executable code at module level without the guard.

#### Impact
Code runs unexpectedly when the module is imported.

#### Incorrect Approach
```python
# utils.py
def helper():
    return 42

# This runs on import!
print("Starting tests...")
result = helper()
print(f"Result: {result}")
```

#### Correct Approach
```python
# utils.py
def helper():
    return 42

if __name__ == "__main__":
    # Only runs when executed directly
    print("Starting tests...")
    result = helper()
    print(f"Result: {result}")
```
