# Unit 3.3: Properties and Encapsulation - Exercises

## Overview
This unit contains 10 concept-focused exercises that test your understanding of Python properties, encapsulation, and access control. Each exercise builds progressively from basic property usage to advanced validation and computed properties.

**File**: `unit_3_3_properties_and_encapsulation_exercises.py`

---

## Exercise List

### Exercise 1: Basic Property with Getter
**Objective**: Master the `@property` decorator for creating getters

**What You'll Build**: A class with a read-only property that returns a private attribute.

**Requirements**:
- Create a `Container` class
- Use a private attribute `_value` initialized to 100
- Create a property `value` that returns `_value`
- Property should be read-only (no setter)

**Key Concepts**: `@property`, private attributes, getters

---

### Exercise 2: Property with Getter and Setter
**Objective**: Master properties with both getter and setter

**What You'll Build**: A class with a writable property using the setter decorator.

**Requirements**:
- Create a `Counter` class
- Use private attribute `_count` initialized to 0
- Create property `count` with both getter and setter
- Allow reading and writing the count value

**Key Concepts**: `@property`, `@<property>.setter`, read-write properties

---

### Exercise 3: Property with Validation
**Objective**: Master data validation in property setters

**What You'll Build**: A class that validates input values in the setter.

**Requirements**:
- Create a `Score` class
- Property `points` must be between 0 and 100 (inclusive)
- Raise `ValueError` for out-of-range values
- Use private attribute `_points`

**Key Concepts**: Validation, raising exceptions, boundary checking

---

### Exercise 4: Read-Only Property (Computed Value)
**Objective**: Master read-only properties for computed values

**What You'll Build**: A class with a property that computes a value dynamically.

**Requirements**:
- Create a `Rectangle` class with `width` and `height`
- Create read-only property `area` that returns `width * height`
- Area should update automatically when dimensions change
- No setter for `area`

**Key Concepts**: Computed properties, read-only access, dynamic values

---

### Exercise 5: Private Attributes with Name Mangling
**Objective**: Understand Python's name mangling for private attributes

**What You'll Build**: A class using double-underscore private attributes.

**Requirements**:
- Create a `Vault` class
- Use private attribute `__secret` (double underscore)
- Create read-only property `secret` to access it
- Understand that Python mangles `__secret` to `_Vault__secret`

**Key Concepts**: Name mangling, `__attribute`, privacy conventions

---

### Exercise 6: Multiple Properties with Different Access Levels
**Objective**: Master public, protected, and private attribute conventions

**What You'll Build**: A class demonstrating all three access levels.

**Requirements**:
- Create an `Account` class
- Public attribute: `name` (no underscore, direct access)
- Protected attribute: `_balance` (property with getter/setter)
- Private attribute: `__pin` (property with getter only)
- Initialize with: name="User", balance=1000, pin="1234"

**Key Concepts**: Access levels, naming conventions, encapsulation

---

### Exercise 7: Property with Type Validation
**Objective**: Master type checking in property setters

**What You'll Build**: A class that validates the data type of property values.

**Requirements**:
- Create a `Config` class
- Property `timeout` must be an integer
- Raise `TypeError` for non-integer values
- Use private attribute `_timeout` initialized to 30

**Key Concepts**: Type validation, `isinstance()`, `TypeError`

---

### Exercise 8: Property with Complex Validation
**Objective**: Master multiple validation rules in a single setter

**What You'll Build**: A class with both type and range validation.

**Requirements**:
- Create a `User` class
- Property `age` must be:
  * An integer (raise `TypeError` if not)
  * Between 0 and 150 inclusive (raise `ValueError` if not)
- Use private attribute `_age` initialized to 18

**Key Concepts**: Multiple validations, exception types, validation order

---

### Exercise 9: Property with Dependent Values
**Objective**: Master properties that depend on other properties

**What You'll Build**: A temperature converter with dependent properties.

**Requirements**:
- Create a `Temperature` class
- Property `celsius` with getter/setter
- Read-only property `fahrenheit` computed as `(celsius * 9/5) + 32`
- Fahrenheit should update automatically when celsius changes

**Key Concepts**: Dependent properties, computed values, automatic updates

---

### Exercise 10: Property Deleter
**Objective**: Master the `@property.deleter` decorator

**What You'll Build**: A class with a deletable property.

**Requirements**:
- Create a `Cache` class
- Property `data` with getter, setter, and deleter
- Deleter should set `_data` to `None`
- Support `del obj.data` syntax

**Key Concepts**: `@<property>.deleter`, `del` statement, cleanup operations

---

## How to Use These Exercises

1. **Open the exercise file**: `unit_3_3_properties_and_encapsulation_exercises.py`

2. **Read each exercise docstring** to understand:
   - Objective (what you're learning)
   - Requirements (what to implement)
   - Expected behavior

3. **Implement your solution** between the "WRITE CODE HERE" markers

4. **Run the tests**:
   ```bash
   python unit_3_3_properties_and_encapsulation_exercises.py
   ```

5. **Verify all tests pass** - you should see:
   ```
   ✓ Exercise 1 passed
   ✓ Exercise 2 passed
   ...
   All exercises passed! 🎉
   ```

6. **Review test cases** to understand edge cases and expected behavior

---

## Learning Path

The exercises are ordered by difficulty:

**Foundational (1-2)**: Basic property syntax and usage
**Intermediate (3-7)**: Validation, access levels, type checking
**Advanced (8-10)**: Complex validation, dependent properties, deleters

Complete them in order for the best learning experience, or jump to specific topics as needed.

---

## Tips for Success

1. **Read the docstrings carefully** - they contain all requirements
2. **Check the test cases** - they show exactly what's expected
3. **Start simple** - get basic functionality working first
4. **Add validation incrementally** - test after each addition
5. **Use meaningful variable names** - `_value`, `_count`, etc.
6. **Remember the decorators**:
   - `@property` for getters
   - `@<property>.setter` for setters
   - `@<property>.deleter` for deleters

---

## Common Patterns

### Basic Property Pattern
```python
class MyClass:
    def __init__(self):
        self._value = 0
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val
```

### Validation Pattern
```python
@value.setter
def value(self, val):
    if not isinstance(val, int):
        raise TypeError("Must be integer")
    if val < 0:
        raise ValueError("Must be non-negative")
    self._value = val
```

### Read-Only Computed Property
```python
@property
def computed_value(self):
    return self._a + self._b
# No setter - read-only!
```

---

## Next Steps

After completing these exercises:
1. Review the knowledge content for deeper understanding
2. Explore the App Labs for real-world applications
3. Move on to Unit 2.4: Special Methods (Dunder Methods)

Good luck! 🚀
