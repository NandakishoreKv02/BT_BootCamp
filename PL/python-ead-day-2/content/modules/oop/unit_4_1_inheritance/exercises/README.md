# Unit 4.1: Inheritance - Exercises

## Overview

This unit contains 10 progressive exercises covering Python inheritance concepts, including single/multiple inheritance, method overriding, `super()`, and Abstract Base Classes (ABCs).

**File**: `unit_4_1_inheritance_exercises.py`

---

## Exercise List

### Exercise 1: Basic Single Inheritance
**Objective**: Create a subclass that inherits attributes and methods.

**Description**: Create a `Vehicle` class and a `Car` subclass. The `Car` should inherit the `start_engine` method.

**Inputs/Outputs**:
- Input: `Car` instance calling `start_engine()`
- Output: Returns "Engine started"

**Requirements**:
- `Vehicle` has `start_engine()` method.
- `Car` inherits from `Vehicle`.
- `Car` adds `num_wheels` attribute in `__init__`.

**Hints**:
1. **Hint 1**: `class Child(Parent):` syntax.
2. **Hint 2**: Remember to call `super().__init__()` if you define `__init__` in Child.
3. **See Solution**: Check solution file.

---

### Exercise 2: Method Overriding
**Objective**: Customize parent behavior in a subclass.

**Description**: Create a variable discount system where a `VIPCustomer` gets a better discount than a standard `Customer`.

**Inputs/Outputs**:
- `Customer.get_discount()` -> 0.05
- `VIPCustomer.get_discount()` -> 0.10

**Requirements**:
- Base `Customer` class returns 0.05.
- `VIPCustomer` overrides `get_discount` to return 0.10.

**Hints**:
1. **Hint 1**: Define the same method name in the subclass.
2. **Hint 2**: No need to call `super()` if you are completely replacing the logic.
3. **See Solution**: Check solution file.

---

### Exercise 3: Using `super()` for Initialization
**Objective**: Extend parent initialization logic.

**Description**: Create an `Employee` system where a `Manager` initializes both standard employee attributes and a department.

**Inputs/Outputs**:
- `Manager` instance has `name`, `salary`, and `department`.

**Requirements**:
- `Employee.__init__` takes `name` and `salary`.
- `Manager.__init__` takes `name`, `salary`, and `department`.
- Use `super().__init__()` to reuse code.

**Hints**:
1. **Hint 1**: `super().__init__(name, salary)`.
2. **Hint 2**: Assign `self.department` after the super call.
3. **See Solution**: Check solution file.

---

### Exercise 4: Extending Methods with `super()`
**Objective**: Add to parent method logic instead of replacing it.

**Description**: A `Logger` class writes to console. A `FileLogger` subclass should write to console AND a file (simulated).

**Inputs/Outputs**:
- `FileLogger.log("msg")` -> Returns "Logged to console: msg | Logged to file: msg"

**Requirements**:
- `Logger.log` returns "Logged to console: {msg}".
- `FileLogger.log` calls parent, then appends file logging text.

**Hints**:
1. **Hint 1**: Capture the result of `super().log(msg)`.
2. **Hint 2**: Return f"{parent_result} | Logged to file: {msg}".
3. **See Solution**: Check solution file.

---

### Exercise 5: Multiple Inheritance Basics
**Objective**: Inherit from two independent classes.

**Description**: Create a `SmartPhone` that acts as both a `Camera` and a `Phone`.

**Inputs/Outputs**:
- `SmartPhone` has `take_photo()` and `make_call()` methods.

**Requirements**:
- `Camera` has `take_photo()`.
- `Phone` has `make_call()`.
- `SmartPhone` inherits from both.

**Hints**:
1. **Hint 1**: `class Child(Parent1, Parent2):`.
2. **Hint 2**: Instances will have methods from both parents.
3. **See Solution**: Check solution file.

---

### Exercise 6: Method Resolution Order (MRO)
**Objective**: Understand lookup order in diamond inheritance.

**Description**: Create a "Diamond" hierarchy (`A` -> `B`, `A` -> `C`, `D` -> `B, C`) and inspect the MRO.

**Inputs/Outputs**:
- Return the `.mro()` list of class `D`.

**Requirements**:
- Classes A, B(A), C(A), D(B, C).
- Return `D.mro()`.

**Hints**:
1. **Hint 1**: Define the classes structure correctly.
2. **Hint 2**: Call the builtin `.mro()` method on the class `D`.
3. **See Solution**: Check solution file.

---

### Exercise 7: Abstract Base Classes (ABC)
**Objective**: Enforce interface implementation.

**Description**: Define an abstract `Shape` class with an abstract method `area`. Implement `Circle` and `Rectangle`.

**Inputs/Outputs**:
- `Circle(5).area()` -> ~78.5
- `Shape()` -> TypeError

**Requirements**:
- Inherit from `ABC`.
- Use `@abstractmethod` decorator.
- `Circle` and `Rectangle` must implement `area`.

**Hints**:
1. **Hint 1**: `from abc import ABC, abstractmethod`.
2. **Hint 2**: Abstract methods have no body (just `pass`).
3. **See Solution**: Check solution file.

---

### Exercise 8: Abstract Properties
**Objective**: Enforce property implementation.

**Description**: An abstract `Database` class requires a `connection_string` property.

**Inputs/Outputs**:
- Subclass without property -> TypeError on instantiation.

**Requirements**:
- `Database` has `@property` and `@abstractmethod` on `connection_string`.
- `SQLDatabase` implements it.

**Hints**:
1. **Hint 1**: Stack `@property` and `@abstractmethod`.
2. **Hint 2**: Subclass must define a property or attribute with that name.
3. **See Solution**: Check solution file.

---

### Exercise 9: Inheritance vs Composition
**Objective**: Refactor inheritance to composition.

**Description**: You have a `Report` class that currently inherits from `Printer`. Change it so `Report` *has a* `Printer`.

**Inputs/Outputs**:
- `Report.print_report()` uses the internal printer.

**Requirements**:
- `Printer.print(text)` method.
- `Report.__init__` accepts a `printer` instance.
- `Report.print_report` delegates to `printer.print`.

**Hints**:
1. **Hint 1**: "Has-A" relationship.
2. **Hint 2**: Store `self.printer = printer`.
3. **See Solution**: Check solution file.

---

### Exercise 10: Real-World Healthcare Hierarchy
**Objective**: Build a multi-level hierarchy with validation.

**Description**: Create a system for `MedicalStaff` -> `Doctor` -> `Surgeon`. Ensure specialization and proper initialization.

**Inputs/Outputs**:
- `Surgeon` has `id`, `name`, `specialty`, and `board_certified` (bool).
- `Surgeon.operate()` checks certification.

**Requirements**:
- `MedicalStaff`: id, name.
- `Doctor`: adds specialty.
- `Surgeon`: adds board_certified.
- `operate()` function raises error if not certified.

**Hints**:
1. **Hint 1**: Chain `super().__init__` calls 3 levels deep.
2. **Hint 2**: Use `raise RuntimeError` for failed checks.
3. **See Solution**: Check solution file.

---

## How to Use These Exercises

1. Open `unit_4_1_inheritance_exercises.py`
2. Read each exercise's docstring for requirements
3. Implement your solution between the TODO markers
4. Run the file to test: `python unit_4_1_inheritance_exercises.py`
5. All tests should pass when complete.

