---
title: "Shielding the State: Access Control & Encapsulation"
type: knowledge
module: thinking_in_objects
unit: unit_2_10_access_control
order: 1
difficulty: intermediate
tags:
  subtopics:
    - access-modifiers
    - name-mangling
    - property-decorator
    - validation
    - data-integrity
---

# Unit 2.10: Access Control & Encapsulation

## 1. What
**Encapsulation** is the bundling of data and the methods that operate on that data into a single unit (the class), while restricting direct access to some of the object's components. 

In clinical systems, encapsulation ensures that a patient's `temperature` cannot be set to 500°C by a coding error. We hide the raw variable and provide a "Controller" (a method) to manage it.

## 2. Example

### Traditional vs. Pythonic Encapsulation
```python
class TemperatureMonitor:
    def __init__(self, temp):
        self._celsius = temp # Protected member

    @property
    def celsius(self):
        """The Getter: Controls how data is read."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """The Setter: Controls how data is written (Validation)."""
        if 30 <= value <= 45: # Clinical safety range
            self._celsius = value
        else:
            print("ERROR: Temperature out of biological range!")

# Usage
monitor = TemperatureMonitor(37.0)
monitor.celsius = 38.5 # SUCCESS: Validation passes
monitor.celsius = 99.0 # FAIL: Blocked by logic in setter
```

## 3. Explanation

### A. Access Modifiers in Python
Python does not have strict `private` or `public` keywords like Java. Instead, it uses **Naming Conventions**:
| Prefix | Access Level | Standard Use |
| :--- | :--- | :--- |
| `name` | **Public** | Accessible from anywhere. Default behavior. |
| `_name` | **Protected** | "Internal use only" signal. Accessible but shouldn't be touched from outside. |
| `__name` | **Private** | Triggers **Name Mangling**. Harder to access from outside, prevents conflicts. |

### B. Name Mangling
When you use `__private_attr`, Python internally renames it to `_ClassName__private_attr`. This prevents accidental modification by subclasses or external scripts.

### C. The `@property` Decorator
This is the "Golden Path" for encapsulation in Python.
- `@property`: Turns a method into a read-only attribute.
- `@attr.setter`: Creates a method that is used whenever a value is assigned to that attribute.
- **Why?** It allows you to add validation logic *after* the class is already in use, without changing how external code accesses the data (`obj.attr = val` stays the same).

## 4. Why
1.  **Data Integrity**: You prevent "Illegal States." An `Age` attribute should never be negative. Encapsulation enforces this rule.
2.  **Ease of Maintenance**: You can change how data is stored internally (e.g., from Celsius to Kelvin) without breaking the code of anyone using your class.
3.  **Security**: Hiding sensitive data identifiers (like `__tax_id`) prevents lazy or careless modifications.

## 5. Advantages & Disadvantages

### Advantages
- **Flexibility**: You can make attributes read-only easily.
- **Validation**: Centralized logic for data checking.
- **Abstraction**: Users of your class only see a clean interface, not the messy math inside.

### Disadvantages
- **Verbosity**: `@property` adds boilerplate code.
- **Execution Overhead**: Accessing a property is slightly slower than a raw variable (though rarely a bottleneck).

## 6. Real-World Use Case: EHR Dosage Safety
In an EHR (Electronic Health Record), a `Prescription` class has a `dose` attribute. By encapsulating it, the setter can automatically cross-reference the dose against the patient's weight before allowing the update.

## 7. Best Practices
1.  **Don't over-encapsulate**: If an attribute doesn't need validation and isn't sensitive, just make it public.
2.  **Use `_` for most internal variables**: It's the standard way to tell teammates "Be careful here."
3.  **Validate in the Setter**: Always raise errors or print warnings in your `@property.setter` if the data is invalid.

## 8. Summary
Encapsulation isn't just about hiding data; it's about **Control**. By using Python's naming conventions and the `@property` decorator, you create clinical software that is safer, cleaner, and more resistant to bugs caused by accidental state corruption.
