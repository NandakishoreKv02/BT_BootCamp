---
title: "The Blueprint and the Reality: Classes and Objects"
type: knowledge
module: thinking_in_objects
unit: unit_2_3_classes_and_objects
order: 1
difficulty: beginner
tags:
  subtopics:
    - class-definition
    - instantiation
    - object-identity
    - state-and-behavior
---

# Unit 2.3: Classes and Objects – Core Concepts

## 1. What
A **Class** is a static blueprint, a template, or a definition. It defines what data an entity will have and what it can do, but it doesn't hold any actual "live" data itself.

An **Object** (or **Instance**) is the dynamic reality. it is a specific "thing" created from the class blueprint that lives in the computer's memory and holds actual data.

## 2. Example

### The Clinical Blueprint (The Class)
Think of a blank **Medical Chart Form**. It has empty spaces for "Name", "Age", and "Diagnosis". It is a template used by every patient in the hospital.
```python
class PatientChart:
    def __init__(self, name, age):
        # Initializing the template with real data
        self.patient_name = name
        self.age = age
        self.diagnosis = "Pending"
```

### The Clinical Reality (The Objects)
When John Doe walks in, we grab a copy of that form and fill it out. Now it's a "Real" object.
```python
# Creating two distinct objects from the same class
patient_a = PatientChart("Alice", 30)
patient_b = PatientChart("Bob", 45)
```

## 3. Explanation

### A. The Trinity of an Object
Every object in Python has three fundamental characteristics:

1.  **Identity**: Where the object lives in memory (its unique address). Use `id(obj)` to see it.
2.  **State**: The data stored inside the object (attributes). E.g., `age = 30`.
3.  **Behavior**: What the object can do (methods). E.g., `update_diagnosis()`.

### B. Blueprint vs. Runtime Reality
| Feature | **Class (Blueprint)** | **Object (Reality)** |
| :--- | :--- | :--- |
| **Exists In** | The code (.py file) | The computer RAM (at runtime) |
| **Data** | Generic (The *type* of data) | Specific (Actual values) |
| **Quantity** | One | Many (Thousands of instances) |
| **Analogy** | Architecture Drawing | The actual House |

## 4. Why
Why not just use dictionaries?
1.  **Strict Structure**: A dictionary can have any keys. A Class *guarantees* that every `Patient` object will have a `name` and `age`.
2.  **Semantic Meaning**: Type-checking. Python knows that a `Patient` object is different from a `Doctor` object, even if they both have names.
3.  **Bundle Logic**: Classes allow you to put the logic (behavior) right next to the data (state) in a clean, professional syntax.

## 5. Advantages & Disadvantages

### Advantages
- **Consistency**: ensures all instances of an entity follow the same rules.
- **Type Safety**: Easier to debug when you know exactly what an object contains.
- **Readability**: `patient.admit()` is clearer than `admit_logic(patient_dict)`.

### Disadvantages
- **Memory Overhead**: Each object instance takes up resources in RAM.
- **Indirection**: For very simple data, a class might be "too much" compared to a simple tuple or list.

## 6. Real-World Use Cases: Medical Hardware
Imagine a **Pulse Oximeter** device.
- **The Class**: The software engineers create a `PulseOximeter` class that defines how to read oxygen levels and how to trigger an alarm.
- **The Objects**: Every bed in the ICU has a physical device. Each device runs an **Instance** of that class. If Bed 1's device detects low oxygen, it triggers its *own* alarm behavior without affecting the device at Bed 2.

## 7. Best Practices
1.  **Naming**: Always use **PascalCase** for classes (`MedicalRecord`) and **snake_case** for objects (`my_record`).
2.  **Initialization**: Always use the `__init__` method to set up the starting state of your object. Don't leave objects in a "half-ready" state.
3.  **Self-Correction**: Use the `self` keyword carefully. It always refers to the *specific instance* you are currently talking to.

## 8. Summary
A class is the **Plan**; an object is the **Action**. Mastering the transition from blueprint to runtime reality is the most important step in becoming a professional software architect. In high-stakes healthcare software, classes provide the "Contracts" that ensure data remains safe and behavior remains predictable.
