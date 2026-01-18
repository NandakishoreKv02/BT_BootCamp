---
title: "The Pythonic Blueprint: Representing Classes"
type: knowledge
module: thinking_in_objects
unit: unit_2_9_representing_classes
order: 1
difficulty: easy
tags:
  subtopics:
    - syntax
    - pep-8
    - constructor
    - instantiation
    - self-keyword
---

# Unit 2.9: Representing Classes in Python

## 1. What
Representing a class in Python involves using specific syntax to define a "Blueprint." While the concepts of OOP are universal, Python has a unique set of "Grammar" rules (PEP 8) and special methods (like `__init__`) that dictate how these blueprints are built and used.

### Core Syntax Components
1.  **Class Header**: `class ClassName:`
2.  **Constructor**: `def __init__(self, ...):`
3.  **Self**: The reference to the current object.
4.  **Instantiation**: The act of creating an object from the class.

## 2. Example

### A PEP-8 Compliant Medical Class
```python
# PascalCase for classes
class BloodPressureReading:
    # Constructor sets the starting state
    def __init__(self, systolic, diastolic):
        # self.attribute (snake_case)
        self.systolic = systolic
        self.diastolic = diastolic

    # Instance method
    def is_hypertensive(self):
        return self.systolic >= 140 or self.diastolic >= 90

# Creating an object (Instantiation)
patient_reading = BloodPressureReading(120, 80)

# Invoking a method
print(patient_reading.is_hypertensive()) # Outputs: False
```

## 3. Explanation

### A. Naming Conventions (PEP 8)
- **Classes**: Use **PascalCase** (or CapWords). Examples: `PatientProfile`, `EmergencyAdmission`.
- **Methods & Attributes**: Use **snake_case**. Examples: `calculate_bmi()`, `patient_id`.
- **Private Attributes**: Start with an underscore (covered in 2.10). Example: `_internal_id`.

### B. The `__init__` Method (The Constructor)
This is a "Magic Method" that Python calls automatically the moment you create a new object. Its primary job is **Initialization**—setting up the object's initial data so it's ready to use.

### C. The `self` Parameter
`self` represents the instance itself.
- Inside the class, `self.name` means "the name attribute of *this specific* object."
- You MUST include `self` as the first argument in every instance method, but you DO NOT pass it when calling the method from outside.

### D. Instantiation vs. Definition
- **Definition**: Writing the code for the class (Creating the blueprint).
- **Instantiation**: Running `p = Patient()` (Building the house from the blueprint).

## 4. Why
Why follow these strict rules?
1.  **Readability**: If everyone uses PascalCase for classes, other developers can instantly identify what is a class and what is a variable just by looking at the case.
2.  **Automation**: Python's `__init__` ensures no object is ever created in an "empty" or "corrupt" state.
3.  **Consistency**: Following PEP 8 makes your code "Pythonic" and professionally acceptable.

## 5. Advantages & Disadvantages

### Advantages
- **Clarity**: Snake_case is scientifically easier to read than camelCase for long method names.
- **Implicit Reference**: Using `self` makes it explicitly clear whether you are working with a local variable or an object attribute.

### Disadvantages
- **Verbosity**: Having to type `self` everywhere can feel repetitive compared to languages like Java or C#.
- **Boilerplate**: You have to write out the assignments (`self.x = x`) manually in the constructor.

## 6. Real-World Use Case: The Patient Vitals Monitor
When a patient is admitted to a ward, the system **instantiates** a `VitalsMonitor` object.
- The `__init__` sets the `alert_thresholds`.
- The methods (like `update_heart_rate`) are **invoked** every few seconds.
- Following PEP 8 ensures that the code can be maintained by any Python developer in the hospital's IT department.

## 7. Best Practices
1.  **Keep `__init__` Simple**: Don't put complex logic (like database calls) in a constructor. Just assign values.
2.  **Always use `self`**: Even if a method doesn't use any attributes yet, if it belongs to the instance, include `self`.
3.  **Document with Docstrings**: Immediately after the class header, add a string describing what the class is for.
```python
class Surgeon:
    """Represents a surgical specialist in the hospital network."""
    pass
```

## 8. Summary
Representing classes correctly is the foundation of professional Python development. By adhering to **PEP 8**, mastering the **constructor**, and understanding **instance scope** via `self`, you turn abstract concepts into standard, high-quality clinical software components.
