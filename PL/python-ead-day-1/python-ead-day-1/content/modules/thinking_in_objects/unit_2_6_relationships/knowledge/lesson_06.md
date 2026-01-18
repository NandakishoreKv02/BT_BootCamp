---
title: "The Web of Interactions: Class Relationships"
type: knowledge
module: thinking_in_objects
unit: unit_2_6_relationships
order: 1
difficulty: intermediate
tags:
  subtopics:
    - inheritance-is-a
    - composition-has-a
    - aggregation
    - dependency-uses
    - modeling-best-practices
---

# Unit 2.6: Relationships Between Classes

## 1. What
Object-Oriented Programming is not just about isolated classes; it’s about how those classes interact. There are three primary ways classes relate to each other:
1.  **Is-a (Inheritance)**: A relationship based on hierarchy and specialized types.
2.  **Has-a (Composition & Aggregation)**: A relationship based on ownership or containment.
3.  **Uses (Dependency)**: A temporary relationship where one object calls another to perform a task.

## 2. Example

### The Clinical "Three-Way" Relationship
1.  **Is-a**: A `Surgeon` **is a** `Doctor`. (Inheritance).
2.  **Has-a**: A `Doctor` **has a** `Laptop`. (Composition).
3.  **Uses**: A `Doctor` **uses a** `PatientDatabase` to lookup names. (Dependency).

```python
class Doctor:
    def __init__(self, name):
        self.name = name
        self.laptop = Laptop() # Has-a (Composition)

    def search_records(self, database): # Uses (Dependency)
        database.query(self.name)

class Surgeon(Doctor): # Is-a (Inheritance)
    pass
```

## 3. Explanation

### A. Is-a Relationship (Inheritance)
In healthcare, we often have general categories and specific sub-types. 
- *Rule*: Only use if you can say "Class B is a type of Class A."
- *Example*: `Inpatient` is-a `Patient`. `EmergencyAdmission` is-a `Admission`.

### B. Has-a Relationship (Ownership)
This is when one object "owns" or contains another.
1.  **Composition (Strong)**: If the owner is destroyed, the part is destroyed.
    - *Example*: A `Human` has a `Heart`. You can't have the heart without the human.
2.  **Aggregation (Weak)**: The part can exist without the owner.
    - *Example*: A `Department` has a `Doctor`. If the department closes, the doctor still exists.

### C. Uses Relationship (Dependency)
A class "uses" another if it receives it as a method argument. The relationship only exists for the duration of that method call.
- *Example*: A `Nurse` uses a `BloodPressureMonitor` to take a reading.

### D. Choosing the Right Relationship
- Use **Inheritance** when classes share a fundamental nature.
- Use **Composition** when one class is made of parts.
- Use **Dependency** when a class needs a tool to do a job.

## 4. Why
Why not just make everything inherit from everything?
1.  **Flexibility**: Inheritance is "Rigid." If you make `Doctor` inherit from `HospitalDatabase`, you can never use that `Doctor` in a different hospital.
2.  **Encapsulation**: Composition keeps classes small and focused.
3.  **Decoupling**: Dependency allows you to swap tools easily. A `Doctor` can use an `SQLDatabase` today and a `CloudDatabase` tomorrow without changing the `Doctor` class code.

## 5. Advantages & Disadvantages

### Advantages
- **Reusability**: You can reuse the `Laptop` class in `Nurse`, `Doctor`, and `Admin`.
- **Maintainability**: Changes to the "Uses" relationship (Dependency) are easy to isolate.
- **Logical Mapping**: The code mirrors the real-world connections in a hospital.

### Disadvantages
- **Complexity**: It can be confusing to track where one object ends and another begins.
- **Over-Inheritance**: One of the most common mistakes is creating deep inheritance trees that are impossible to change.

## 6. Real-World Use Case: Robotic Surgery
An **SurgicalRobot** system:
- **Has-a**: `Arm`, `Camera`, `Laser`. (Composition).
- **Uses**: `PowerGrid`, `DataLogger`. (Dependency).
- **Is-a (Child of)**: `MedicalDevice`. (Inheritance).

## 7. Best Practices
1.  **Favor Composition over Inheritance**: This is a classic OOP mantra. It makes your system "pluggable" and easier to change.
2.  **The "Liskov" Test**: If you use inheritance, the child class should be able to do everything the parent does.
3.  **Keep Dependencies Explicit**: Don't hide a "Uses" relationship inside a method by creating the object there. Pass it in as an argument (Dependency Injection).

## 8. Summary
Modeling relationships is the "Grammar" of software architecture. Use **Inheritance** for identity, **Composition** for structure, and **Dependency** for utility. By choosing the right relationship, you create a system that is as organized and efficient as a world-class surgical theater.
