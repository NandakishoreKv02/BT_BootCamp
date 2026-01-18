---
title: "Inheritance: Code Reuse and Hierarchies"
type: knowledge
module: oop
unit: unit_4_1_inheritance
order: 5
difficulty: intermediate
tags: [oop, inheritance, mro, super, abc]
use_case: hospital_staff_management
---

# Unit 4.1: Inheritance

## 1. What
**Inheritance** is a fundamental principle of Object-Oriented Programming that allows a new class (the **subclass** or child) to acquire the properties and behaviors of an existing class (the **superclass** or parent). It establishes an **"Is-A"** relationship between objects.

In Python, inheritance is not just about copying code; it's about creating a logical hierarchy where specialized objects can leverage general logic defined higher up in the tree.

### The Problem It Solves
Without inheritance, you would have to duplicate code across similar classes. For example, in a hospital system, both `Doctor` and `Nurse` have a name, an employee ID, and a payroll record. Instead of defining these attributes twice, you define them once in a `HospitalStaff` class and let both `Doctor` and `Nurse` inherit from it. This prevents **code duplication** and ensures that a change to the general staff logic (e.g., how IDs are formatted) automatically applies to all types of staff.

### When to Use This?
Use inheritance when you have a clear **"Is-A"** relationship. A `Surgeon` **is a** `Doctor`. An `Ambulance` **is a** `Vehicle`. Do not use inheritance just to "steal" a few methods from another class (use composition for that). Use **Single Inheritance** for simple parent-child relationships, and **Multiple Inheritance** when an object logically fulfills multiple roles (e.g., a `ManagingDoctor` who is both a `Doctor` and an `Admin`).

---

## 2. Example

### Example 1: Basic Single Inheritance
The subclass uses `super()` to initialize parent attributes and adds its own specialization.
```python
class HospitalStaff:
    def __init__(self, name, employee_id):
        self.name = name
        self.id = employee_id

    def get_details(self):
        return f"ID: {self.id} | Name: {self.name}"

class Doctor(HospitalStaff):
    def __init__(self, name, employee_id, specialty):
        # super() calls the parent class constructor
        super().__init__(name, employee_id)
        self.specialty = specialty

    def get_details(self):
        # Override parent method and extend it
        base_info = super().get_details()
        return f"{base_info} | Specialty: {self.specialty}"

# Usage
doc = Doctor("Dr. Strange", "DOC-001", "Neurosurgery")
print(doc.get_details())
# Output: ID: DOC-001 | Name: Dr. Strange | Specialty: Neurosurgery
```

### Example 2: Multiple Inheritance and Mixins
Mixins are classes designed to provide additional functionality to other classes via multiple inheritance.
```python
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class ValidatorMixin:
    def is_valid_email(self, email):
        return "@" in email

class PatientRecord(LoggerMixin, ValidatorMixin):
    def save_record(self, email):
        if self.is_valid_email(email):
            self.log(f"Saving record for {email}")
            return True
        return False

# Usage
patient = PatientRecord()
patient.save_record("alice@hospital.com")
# Output: [LOG]: Saving record for alice@hospital.com
```

### Example 3: Abstract Base Classes (ABCs)
ABCs define a "contract" that all subclasses must follow, but cannot be instantiated themselves.
```python
from abc import ABC, abstractmethod

class MedicalDevice(ABC):
    @abstractmethod
    def take_reading(self):
        """All devices must implement this method."""
        pass

class Thermometer(MedicalDevice):
    def take_reading(self):
        return 98.6

# Usage
# device = MedicalDevice() # This would raise a TypeError
therm = Thermometer()
print(therm.take_reading())
# Output: 98.6
```

---

## 3. Explanation

### How It Works: The `super()` Proxy
The `super()` function returns a proxy object that allows you to call methods of the parent class. While it is most commonly used in `__init__`, it can be used in any method to "extend" rather than completely "replace" data. It ensures that the parent's state is properly set up before the child adds its own specific logic.

### Method Resolution Order (MRO)
In multiple inheritance, Python needs to know which parent's method to call if both define the same name. It uses an algorithm called **C3 Linearization** to create an **MRO**—a deterministic list of classes to search.
- You can view any class's MRO by calling `ClassName.mro()` or `help(ClassName)`.
- Python searches from left to right in the inheritance list, then goes up the tree (Depth-First, Left-to-Right).

### Comparison Table: Inheritance vs. Composition
| Feature | Inheritance (Is-A) | Composition (Has-A) |
| :--- | :--- | :--- |
| **Relationship** | Class B is a specialized version of Class A. | Class B contains an instance of Class A. |
| **Coupling** | High (Tight) | Low (Loose) |
| **Flexibility** | Static (Fixed at design time) | Dynamic (Can change at runtime) |
| **Code Reuse** | Automatic for all public methods. | Manual delegation to the contained object. |
| **Best For** | Hierarchies (Doctor -> Surgeon) | Components (Monitor has a Battery) |

### The Diamond Problem
This occurs in multiple inheritance when two parent classes inherit from a single base class, and the child class inherits from both. Python's MRO handles this by ensuring each class in the hierarchy is visited exactly once, preventing duplicate initialization of the root base class.

---

## 4. Why

### 1. Code Reusability
Inheritance allows you to write common logic (like "Calculating Payroll" or "Updating Address") once in a base class and have it available across dozens of specialized subclasses without rewriting a single line of code.

### 2. Standardized Interfaces
By using Abstract Base Classes (ABCs), you ensure that every `MedicalDevice` in your system has a `.take_reading()` method. This allows you to write generic code that handles *any* device, knowing it follows the standard interface.

### 3. Logical Organization
Inheritance forces you to think about the "ancestry" of your objects. It creates a natural directory structure for your code, making it easier for new developers to understand that a `Cardiologist` will have all the behaviors of a `Doctor`.

### 4. Overriding for Specialization
It allows you to provide a "generic" behavior in the parent (e.g., `process_payment`) and a specific, more optimized behavior in the child (e.g., `process_insurance_payment`) without breaking the calling code.

---

## 5. Advantages & Disadvantages

### Advantages

#### 1. DRY (Don't Repeat Yourself)
Massive reduction in boilerplate code. Updates to shared logic only need to happen in one place (the superclass).

#### 2. Extensibility
New features can be added by creating a new subclass without touching or risking the existing, working parent code. This follows the **Open/Closed Principle**.

#### 3. Simplified Client Code
Code that uses your classes can treat a `Surgeon` as a `Doctor`. This allows for polymorphic collections: a list of `[Doctor(), Surgeon(), Nurse()]` can all be processed by a single `staff.pay()` loop.

### Disadvantages

#### 1. Tight Coupling
A change in the superclass might accidentally break something in a subclass. Subclasses are highly dependent on the internal implementation of their parents.

#### 2. Fragile Base Class Problem
If you change a method signature in a root class, you might have to update hundreds of subclasses. This makes deep inheritance trees (5+ levels) very risky.

#### 3. Misuse for Code "Theft"
Developers often use inheritance just to get access to a helper function, creating messy "God Classes" that don't represent a true "Is-A" relationship.

---

## 6. Real-World Use Cases

### Domain 1: Healthcare
**Problem**: Managing different types of hospital staff with varying pay scales but shared identity data.
**Solution**: Use a `Staff` base class for identity and specific `Doctor`, `Nurse`, and `Admin` subclasses for pay logic.
```python
class Staff:
    def __init__(self, name): self.name = name
    def get_id(self): return "ID-" + self.name

class Nurse(Staff):
    def calculate_pay(self, hours): return hours * 45
```

### Domain 2: eCommerce
**Problem**: Creating a shipping system that handles `Standard`, `Express`, and `International` packages.
**Solution**: An `Order` base class defines `get_total()`, while subclasses override `calculate_shipping()`.
```python
class ExpressOrder(Order):
    def calculate_shipping(self):
        return super().calculate_shipping() + 25.00 # Base + Express fee
```

### Domain 3: Gaming (Software Engines)
**Problem**: Different game entities (Player, Enemy, NPC) share movement logic but have different visual representations.
**Solution**: An `Entity` base class handles `x, y` coordinates and `move()`, while subclasses override `draw()`.

---

## 7. Best Practices

### Best Practice 1: Favor Composition Over Inheritance
**When to apply**: When the relationship is "Has-A" (e.g., a Car has an Engine) or when you only need a small part of another class's functionality.
**Why**: It reduces coupling and makes your code much more flexible and testable.

### Best Practice 2: Keep Hierarchies Shallow
**When to apply**: Always.
**Why**: Aim for a maximum of 3 levels. Deep hierarchies are hard to visualize, prone to MRO confusion, and extremely difficult to refactor.

### Best Practice 3: Follow the Liskov Substitution Principle (LSP)
**When to apply**: In every subclass design.
**Why**: A subclass should always be able to replace its parent without the program crashing. If `Doctor.pay()` expects an integer, `Surgeon.pay()` must not expect a string.

### Best Practice 4: Use `super()` Consistently
**When to apply**: In every overridden method that needs to perform parent logic.
**Why**: It handles multiple inheritance correctly and avoids hard-coding parent class names, making your code "future-proof" against name changes.

---

## 8. Top 3 Mistakes

### Mistake 1: Forgetting `super().__init__()`

#### What's the Problem?
Defining a constructor in the child class but failing to call the parent's constructor.

#### Impact
The attributes defined in the parent class are never created for the child instance. Attempting to access `self.parent_attribute` will raise an `AttributeError`.

#### Incorrect Approach
```python
class Parent:
    def __init__(self): self.data = 10

class Child(Parent):
    def __init__(self): 
        self.new_data = 20 # Parent.__init__ is never called!
```

#### Correct Approach
```python
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.new_data = 20
```

---

### Mistake 2: The "Deep Tree" Nightmare

#### What's the Problem?
Creating a hierarchy like: `Organism -> Animal -> Mammal -> Dog -> Labrador -> ServiceLabrador`.

#### Impact
This makes the code impossible to follow. A bug in `Mammal` could manifest in `ServiceLabrador` in a way that is extremely hard to trace. It also makes moving logic between classes a nightmare.

#### Correct Approach
Use Mixins or Composition to add traits (like `ServiceTrait`) instead of adding levels to the inheritance tree.

---

### Mistake 3: Overriding Without Matching Signatures

#### What's the Problem?
Changing the number or type of arguments in a subclass method that overrides a parent method.

#### Impact
It breaks **Polymorphism**. If a piece of code expects to call `device.read(timeout=10)` and your subclass changes it to `device.read(unit_type)`, the code will crash when given your subclass.

#### Correct Approach
Always maintain the same signature. If you need extra data in the child, use default arguments or `**kwargs`.
