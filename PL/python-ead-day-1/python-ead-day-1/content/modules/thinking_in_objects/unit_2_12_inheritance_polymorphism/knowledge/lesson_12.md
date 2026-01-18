---
title: "The Clinical Family Tree: Inheritance & Polymorphism"
type: knowledge
module: thinking_in_objects
unit: unit_2_12_inheritance_polymorphism
order: 1
difficulty: intermediate
tags:
  subtopics:
    - inheritance
    - method-overriding
    - super-keyword
    - polymorphism
    - code-reuse
---

# Unit 2.12: Inheritance & Polymorphism

## 1. What
**Inheritance** is a mechanism where a new class (Subclass/Child) derives properties and behaviors from an existing class (Base class/Parent). It represents an **"Is-A"** relationship.

**Polymorphism** (from Greek, "Many Forms") is the ability of different objects to respond to the same method name in their own specific way.

In healthcare, we use these to model general concepts (like a `MedicalProfessional`) and then specialize them (like a `Radiologist`).

## 2. Example

### Specializing Clinical Behavior
```python
class MedicalDevice:
    """The Base Class: Represents general device behavior."""
    def __init__(self, serial_id):
        self.serial_id = serial_id

    def run_check(self):
        print(f"Device {self.serial_id}: Basic power check passed.")

class Ventilator(MedicalDevice):
    """The Subclass: Inherits from MedicalDevice."""
    def __init__(self, serial_id, oxygen_cap):
        # super() calls the parent's logic
        super().__init__(serial_id)
        self.oxygen_cap = oxygen_cap

    def run_check(self):
        """Method Overriding: Specialized check for lung support."""
        super().run_check() # Do the general check first
        print(f"Ventilator {self.serial_id}: Pressure valves verified.")

# Usage
monitor = MedicalDevice("M-001")
vent = Ventilator("V-999", 500)

devices = [monitor, vent]

for d in devices:
    # POLYMORPHISM: Each device runs its own version of run_check()
    d.run_check()
```

## 3. Explanation

### A. Inheritance Syntax
In Python, we pass the parent class in parentheses: `class Child(Parent):`. This gives the child access to all public methods and attributes of the parent.

### B. Method Overriding
If a child class defines a method with the exact same name as the parent, the child's version "Wins." This allows subclasses to replace generic behavior with specific logic.

### C. The `super()` Keyword
`super()` is used to access the parent's methods. Its most common use is in `__init__`, ensuring the parent class has a chance to set up its attributes before the child adds its own.

### D. Polymorphism
This allows you to create a list of different objects and call the same method on all of them. The program doesn't need to know the specific type; it just knows the method exists. This is the foundation of **Scalability**.

## 4. Why
1.  **DRY (Don't Repeat Yourself)**: You write shared code (like `name` or `id`) once in a parent class.
2.  **Extensibility**: You can add new device types (Defibrillators, MRI) without changing the code that manages the device list.
3.  **Consistency**: Ensures all "Clinical Tools" follow the same interface (like having a `calibrate` method).

## 5. Advantages & Disadvantages

### Advantages
- **Reusability**: Massive reduction in boilerplate code.
- **Maintainability**: Bug fixes in the parent class automatically propagate to all children.
- **Organization**: Creates a logical taxonomy for complex systems.

### Disadvantages
- **Tight Coupling**: Changes in the parent class can break child classes in unexpected ways.
- **Complexity**: Deep hierarchies can make it hard to track where a method is defined.

## 6. Real-World Use Case: The Insurance Claim System
A hospital handles different claim types: `MedicareClaim`, `PrivateClaim`, and `CorporateClaim`.
All inherit from `BaseClaim`. All have a `process()` method. The high-level Accounting system just iterates through a list of claims and calls `claim.process()`. Polymorphism ensures that `MedicareClaim` calculates taxes differently than `PrivateClaim` without the accounting script needing to know the details.

## 7. Best Practices
1.  **Check for "Is-A"**: Only use inheritance if a child truly "Is-A" parent.
2.  **Favor Composition**: If you just want to use a tool, don't inherit from it—make it an attribute (Unit 2.6).
3.  **Always use `super()`**: Don't call the parent by name (`MedicalDevice.__init__`), use `super().__init__` for better flexibility and compatibility with multiple inheritance.
4.  **Avoid Deep Nesting**: Try to keep your "Family Tree" shallow.

## 8. Summary
Inheritance lets us build specialized clinical entities from general blueprints. Polymorphism lets us treat those diverse entities with a singular, simple interface. Together, they allow us to build software that is as organized and flexible as a real-world hospital registry.
