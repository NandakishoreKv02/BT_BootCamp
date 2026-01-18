---
title: "The Mechanics of State and Behavior"
type: knowledge
module: thinking_in_objects
unit: unit_2_5_attributes_methods
order: 1
difficulty: intermediate
tags:
  subtopics:
    - instance-vs-class-attributes
    - method-signatures
    - cohesion
    - state-management
---

# Unit 2.5: Attributes and Methods

## 1. What
In OOP, a class is composed of two main parts:
- **Attributes (The Nouns)**: Variables that represent the state or properties of the object.
- **Methods (The Verbs)**: Functions that represent the behavior or actions the object can perform.

Understanding the *scope* of these attributes (Instance vs. Class) and the *relevance* of these methods (Cohesion) is what separates a coder from a software architect.

## 2. Example

### Instance vs. Class Attributes
In a hospital, every **Patient** has a unique `name`. However, all patients share the same **Hospital Name**.

```python
class Patient:
    # CLASS ATTRIBUTE: Shared by all instances
    hospital_name = "City General"
    
    def __init__(self, name):
        # INSTANCE ATTRIBUTE: Unique to this person
        self.patient_name = name

p1 = Patient("Alice")
p2 = Patient("Bob")

print(p1.patient_name) # "Alice"
print(p1.hospital_name) # "City General"
print(p2.hospital_name) # "City General"
```

## 3. Explanation

### A. Attributes: The "State"
1.  **Instance Attributes**: Defined inside `__init__` using `self`. They represent the individual data of that specific object.
2.  **Class Attributes**: Defined directly inside the class but outside any methods. They are shared across all instances. If you change a class attribute, every object sees the change.

### B. Methods: The "Behavior"
A method is just a function that "belongs" to an object.
- **Method Signature**: Includes the name and the parameters (`def prescribe(self, drug, dose):`). A good signature makes the code self-documenting.
- **The `self` Parameter**: The first argument of every instance method. It is a reference to the specific object that called the method.

### C. Cohesion Within a Class
**Cohesion** measures how closely related the members of a class are.
- **High Cohesion (Good)**: All methods and attributes in `class Prescription` are about medications.
- **Low Cohesion (Bad)**: A `class Patient` that also has methods for `calculate_hospital_taxes()` and `repair_mri_machine()`. Low cohesion makes code hard to test and easy to break.

## 4. Why
Why distinguish between Class and Instance attributes?
1.  **Memory Efficiency**: 10,000 Patient objects can share one `hospital_name` string instead of storing 10,000 identical copies.
2.  **Global Constants**: It provides a perfect place to store configuration values (like `MAX_HEART_RATE`) that apply to all instances.

Why care about Method Signatures?
1.  **Contractual Clarity**: In healthcare, a method like `administer_dose(amount)` is a contract. If you change the signature to `administer_dose(amount, unit)`, you must ensure every part of the hospital system is updated to follow the new contract.

## 5. Advantages & Disadvantages

### Advantages
- **Shared Memory**: Class attributes save RAM.
- **Modularity**: High cohesion ensures that a bug in "Billing" doesn't hide inside the "Patient" class.
- **Standardization**: Uniform signatures ensure that different modules can "talk" to each other predictably.

### Disadvantages
- **Class Attribute Danger**: Accidental modification of a class attribute can cause system-wide side effects.
- **Complexity**: New developers often confuse `self.variable` with `ClassName.variable`.

## 6. Real-World Use Case: The Lab Analyzer
Imagine a blood analyzer machine in a lab.
- **Class Attribute**: `FIRMWARE_VERSION = "2.1"`. (All machines run the same version).
- **Instance Attribute**: `current_sample_id = "LAB-99"`. (Each machine processes its own sample).
- **Methods**: `analyze_blood()`, `print_report()`. (These are cohesive actions for an analyzer).

## 7. Best Practices
1.  **Attribute Placement**: If the data is unique, put it in `self`. If it's a constant or shared stat, put it in the class.
2.  **Verb-First Methods**: Method names should be verbs (`take_vitals`, `add_patient`).
3.  **Encapsulate Complex logic**: Don't let users manually change `patient.temp = 105`. Use a method `patient.update_temp(105)` so you can add validation logic later.

## 8. Summary
Attributes are the **Memory** of your system, and methods are the **Brain**. By correctly choosing between Class and Instance scope, and maintaining high cohesion, you build code that is efficient, intuitive, and resistant to the "spaghetti" rot that plagues large clinical systems.
