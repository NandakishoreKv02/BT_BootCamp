---
title: "The Birth of an Object: Constructors & Lifecycle"
type: knowledge
module: thinking_in_objects
unit: unit_2_11_constructors_lifecycle
order: 1
difficulty: easy
tags:
  subtopics:
    - init-method
    - default-parameters
    - object-lifecycle
    - constructor-best-practices
    - mutable-defaults
---

# Unit 2.11: Constructors & Object Lifecycle

## 1. What
The **Constructor** (`__init__`) is the special method Python executes immediately after an object is created. While the "Creation" happens in the background, the "Initialization" (setting up the initial state) is where you, the developer, take control.

The **Object Lifecycle** represents the journey from instantiation to destruction. Mastering the constructor ensures that every clinical object enters the system in a healthy, valid state.

## 2. Example

### Handling Optional Clinical Data
```python
import datetime

class PatientAdmission:
    """Manages the entry of a patient into the hospital ward."""
    
    def __init__(self, patient_name, dept="General Ward", notes=None):
        # Mandatory field
        self.patient_name = patient_name
        
        # Optional field with Default value
        self.dept = dept
        
        # Optional collection (Best Practice: Use None)
        if notes is None:
            self.notes = []
        else:
            self.notes = notes
            
        self.timestamp = datetime.datetime.now()

# Usage 1: Minimal info
adm1 = PatientAdmission("Alice") 

# Usage 2: Custom info
adm2 = PatientAdmission("Bob", dept="ICU", notes=["History of asthma"])
```

## 3. Explanation

### A. Parameterized Constructors
These are constructors that take arguments. They allow you to pass dynamic data (like a patient's name) directly into the object during creation.
- `p = Patient("John")` -> calls `__init__(self, "John")`.

### B. Default Values & Optional Parameters
Python allows you to set default values in the method signature.
- `def __init__(self, role="Nurse"):`
- If no role is provided, the object defaults to "Nurse".
- This reduces "Boilerplate" code for standard cases.

### C. The Sentinel Pattern (Avoiding Mutable Defaults)
**CRITICAL ERROR**: `def __init__(self, list_attr=[])`.
In Python, default arguments are evaluated only once. If you use a list literal `[]`, every object created will share the **EXACT SAME LIST**.
**The Fix**: Always use `None` as a default and initialize the list inside the `__init__` block.

### D. Creation vs. Initialization
- **`__new__`**: Creates the raw object memory (Implicitly handled by Python).
- **`__init__`**: Initializes the state (Populates the attributes).
- In 99% of cases, you only need to care about `__init__`.

## 4. Why
1.  **Safety**: Ensures an object is never in an "Undefined" state. A `VitalsMonitor` must have a `sensor_id` to function.
2.  **Flexibility**: Allows you to create objects using diverse data sources (minimal vs. comprehensive).
3.  **Readability**: Parameterized constructors make dependencies clear. You know exactly what a class needs just by looking at its `__init__`.

## 5. Advantages & Disadvantages

### Advantages
- **Enforced State**: You can validate data before the object is fully "Born."
- **Code Reuse**: Default parameters allow the same class to handle multiple use cases.

### Disadvantages
- **Constructor Bloat**: If a class has 20 arguments, it becomes hard to manage (Consider the "Builder Pattern" in Module 3).
- **Stealth Errors**: Mistyping a keyword argument can lead to confusing errors if defaults are present.

## 6. Real-World Use Case: The EHR Audit Log
When any action is taken in an EHR, an `AuditEntry` is created.
- The `user_id` is mandatory.
- The `action` is mandatory.
- The `severity` defaults to "INFO".
- The `timestamp` is automatically generated in `__init__`.
This ensures every log entry is consistent without the developer needing to manually set the time every time.

## 7. Best Practices
1.  **Keep it focused**: Only handle state setup. Don't call external APIs or long-running tasks in `__init__`.
2.  **Explicit is better than implicit**: Use keyword arguments when creating objects with more than 3 parameters.
3.  **Validate early**: Check for `None` or invalid types in the constructor to fail fast.

## 8. Summary
The constructor is the gatekeeper of your class. By mastering **parameterization**, **default values**, and avoiding **mutable default traps**, you ensure that your clinical objects are robust, flexible, and cleanly initialized every time they are "Born" into your system.
