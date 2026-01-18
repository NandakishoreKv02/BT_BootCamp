---
title: "Methods: Instance, Class, and Static"
type: knowledge
module: oop
unit: unit_3_2_methods
order: 2
difficulty: intermediate
tags: [oop, methods, classmethod, staticmethod, behavior]
use_case: hospital_operations
---

# Unit 3.2: Methods

## 1. What
In Object-Oriented Programming, **Methods** are functions that are defined inside a class. While attributes represent the "state" or data of an object, methods represent the "behavior" or actions that the object can perform. They are the mechanisms through which we interact with and manipulate the data encapsulated within an object.

In Python, not all methods are created equal. Depending on what data they need to access, they are categorized into three distinct types:
1.  **Instance Methods**: The most common type. They act on a specific instance (object) of the class and have access to unique instance data via the `self` parameter.
2.  **Class Methods (`@classmethod`)**: These act on the class itself rather than a specific object. They are often used as "factory methods" to create objects in different ways. They receive the class as the first argument (`cls`).
3.  **Static Methods (`@staticmethod`)**: These are essentially regular functions that happen to live inside a class's namespace. They do not have access to either instance data or class data.

### The Problem It Solves
Without methods, objects would be passive data structures (like a dictionary). You would have to write external functions to modify them, which breaks the principle of **Encapsulation**. Methods allow an object to "own" its logic. For example, a `Patient` object shouldn't just *have* a heart rate; it should know how to *update* its heart rate and *notify* a doctor if it exceeds a threshold.

### When to Use This?
Use **Instance Methods** for object-specific actions (e.g., a patient taking medication). Use **Class Methods** for logic that involves the entire class (e.g., tracking the total number of patients admitted). Use **Static Methods** for utility functions that are logically related to the class but don't need its data (e.g., validating a Social Security Number format).

---

## 2. Example

### Example 1: Basic Instance Methods
Instance methods use `self` to access and modify the object's unique attributes.
```python
class Patient:
    def __init__(self, name):
        self.name = name
        self.is_checked_in = False

    def check_in(self):
        """Instance method: Modifies the specific patient's state."""
        self.is_checked_in = True
        return f"{self.name} has been checked in."

# Usage
p1 = Patient("Alice")
print(p1.check_in())
# Output: Alice has been checked in.
```

### Example 2: Class Methods as Factories
Class methods are great for creating objects from different data sources (like a date string vs. individual numbers).
```python
class Appointment:
    def __init__(self, day, month, year):
        self.date = f"{year}-{month:02d}-{day:02d}"

    @classmethod
    def from_string(cls, date_str):
        """Class method: Creates a new instance from a 'DD-MM-YYYY' string."""
        day, month, year = map(int, date_str.split("-"))
        # cls() is equivalent to calling Appointment()
        return cls(day, month, year)

# Usage
apt = Appointment.from_string("15-05-2024")
print(apt.date)
# Output: 2024-05-15
```

### Example 3: Static Methods for Utilities
Static methods perform logic that doesn't require "knowing" about any specific patient or the hospital.
```python
class HealthUtils:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Static method: A pure utility with no dependance on class/instance."""
        return (celsius * 9/5) + 32

# Usage
print(HealthUtils.celsius_to_fahrenheit(37))
# Output: 98.6
```

### Example 4: Return Values and Side Effects (Healthcare Scenario)
This example demonstrates a method that performs a "side effect" (changing state) and returns a value (status).
```python
class Pharmacy:
    def __init__(self):
        self.inventory = {"Insulin": 10, "Aspirin": 50}

    def dispense_medication(self, med_name, quantity):
        """
        Side Effect: Decreases inventory.
        Return Value: Success/Failure status.
        """
        if med_name in self.inventory and self.inventory[med_name] >= quantity:
            self.inventory[med_name] -= quantity # Side effect
            return True # Return value
        return False

# Usage
clinic_pharmacy = Pharmacy()
success = clinic_pharmacy.dispense_medication("Insulin", 2)
print(f"Dispensed: {success}, Stock left: {clinic_pharmacy.inventory['Insulin']}")
# Output: Dispensed: True, Stock left: 8
```

---

## 3. Explanation

### How It Works: The Three Musketeers
When a method is called, Python's runtime environment automatically handles the arguments based on the method type.

1.  **Instance Method (`self`)**: When you call `obj.method()`, Python actually executes `Class.method(obj)`. The object itself is silently passed as the first argument, which we name `self` by convention. This gives the method a handle to the object's specific memory space.
2.  **Class Method (`cls`)**: When you call `obj.classmethod()` or `Class.classmethod()`, Python passes the *class object* itself as the first argument. This allows you to interact with class-level attributes or even create new instances of that exact class (even if inherited).
3.  **Static Method**: No extra arguments are passed. It behaves exactly like a function defined outside a class, but it is grouped under the class's name for organizational purposes.

### The Memory Model
In Python, methods are not "copied" for every object. If you have 10,000 `Patient` objects, there is still only **one** copy of the `check_in` method in memory, living inside the `Patient` class object. When you call the method on an instance, Python creates a **bound method**—a temporary wrapper that links the class's function to your specific instance.

### Comparison Table: Method Types
| Feature | Instance Method | Class Method | Static Method |
| :--- | :--- | :--- | :--- |
| **Decorator** | None | `@classmethod` | `@staticmethod` |
| **1st Parameter** | `self` (Instance) | `cls` (Class) | None |
| **Access to Instance?** | Yes | No | No |
| **Access to Class?** | Yes (via `type(self)`) | Yes | No |
| **Main Use Case** | Modifying object state | Factory methods | Utility functions |

### Method Overloading Alternatives
Unlike Java or C++, Python **does not support** traditional method overloading (having two methods with the same name but different parameters). If you define two methods with the same name, the second one will overwrite the first.

To achieve "overloading" in Python, we use:
1.  **Default Arguments**: `def medical_test(self, patient_id, test_type="General"):`
2.  **Variable Arguments (`*args`, `**kwargs`)**: To handle an arbitrary number of inputs.
3.  **Class Methods**: As shown in Example 2, providing different "entry points" for object creation.

### Return Values vs. Side Effects
*   **Side Effect**: An observable change in the state of the system that happens during the execution of a method (e.g., updating a database, printing to console, or modifying `self.attribute`).
*   **Return Value**: The data explicitly sent back to the caller using the `return` keyword.

In good software design, we aim for **Command-Query Separation**. A method should either be a *command* (performs a side effect but returns nothing) OR a *query* (returns data but has no side effects). While Python doesn't enforce this, following it makes code much easier to debug.

---

## 4. Why

### 1. Consistent Interface
Methods provide a controlled way to interact with an object. If you want to change a patient's temperature, you don't just set `p1.temp = 38`. You call `p1.update_temperature(38)`. This method can then include validation logic (e.g., checking if the temperature is physically possible) before applying the change. This ensures the object's data always remains valid.

### 2. Namespace Organization
Static methods allow you to group tools where they belong. A `MathUtils.calculate_bmi()` is much easier to find than a loose `calculate_bmi()` function floating in a 5,000-line codebase. It tells other developers exactly which domain this function serves.

### 3. Factory Flexibility
Class methods are the backbone of flexible object creation. Imagine you are building a healthcare API. Sometimes you get patient data from a JSON object, sometimes from a CSV file, and sometimes from a database query. Instead of making the `__init__` constructor messy with `if/else` logic, you create `@classmethod from_json` and `@classmethod from_db`.

### 4. Code Reusability via `self`
Because instance methods use `self`, they are generic. The same `calculate_dosage()` method works for `Patient A` and `Patient B` without needing extra parameters for their weight or age—the method already "knows" where to find that data within the object it was called on.

### 5. Managing Complexity
By using return values and side effects intentionally, you can create complex workflows. A `Surgery.perform()` method might have the side effect of updating surgeons' schedules and return a boolean indicating success. This allows the calling code to handle the result cleanly: `if surgery.perform(): send_bill()`.

---

## 5. Advantages & Disadvantages

### Advantages

#### 1. Encapsulation of Logic
Logic is kept next to the data it manages. This "togetherness" makes code intuitive.
*Example*: A `Thermostat` object containing the `adjust_temp()` logic rather than having that logic in a central "Controller" script.

#### 2. Polymorphism Support
Different classes can have methods with the same name. You can call `.discharge()` on a `Patient` object and a `Staff` object. Python will automatically call the correct implementation based on the object's type, which simplifies complex systems.

#### 3. Maintenance Ease
If the way you calculate "Healthy Risk" changes, you only update the `calculate_risk()` method inside the `Patient` class. You don't have to search through your entire application for every place a risk calculation happens.

### Disadvantages

#### 1. Overhead for Simple Logic
If a piece of code doesn't need to access or modify any object state, making it a method can add unnecessary syntax (`self`) and complexity. In these cases, a simple stand-alone function might be better.

#### 2. Complexity of `self`/`cls`
Beginners often struggle with the "Magic" handled by Python. Forgetting to include `self` leads to frustrating `TypeError` messages that can be cryptic to those coming from procedural backgrounds.

#### 3. Mutable Side Effect Risks
Methods that modify state (side effects) can be harder to test than "Pure Functions" (which only take inputs and return outputs). If a method changes five different attributes, it's harder to predict the system's state after the call.

---

## 6. Real-World Use Cases

### Domain 1: Healthcare
**Problem**: Calculating medication dosage safely based on varying patient metrics.
**Solution**: Use an instance method to combine weight and age data stored in the object to return a precise dosage.
```python
class Patient:
    def __init__(self, weight_kg, age):
        self.weight = weight_kg
        self.age = age

    def calculate_dosage(self, base_mg):
        """Instance method: Uses internal state to calculate safe dosage."""
        if self.age < 12:
            return (base_mg * self.weight) / 100
        return base_mg
```

### Domain 2: eCommerce
**Problem**: Applying seasonal discounts to a shopping cart without modifying the original product prices.
**Solution**: Use a static method to calculate discounts as a pure calculation service.
```python
class DiscountEngine:
    @staticmethod
    def apply_seasonal_discount(price, season):
        """Static method: Pure calculation utility."""
        if season == "Winter":
            return price * 0.8
        return price
```

### Domain 3: Banking
**Problem**: Creating account objects from legacy paper records (text strings) vs. modern digital data.
**Solution**: Use class methods to handle different data formats for account opening.
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @classmethod
    def from_legacy_data(cls, raw_string):
        """Class method: Factory to handle old record formats."""
        # Assume format: "OWNER_NAME:BALANCE"
        name, bal = raw_string.split(":")
        return cls(name, float(bal))

# Usage
legacy_acc = BankAccount.from_legacy_data("JohnSmith:1500.50")
```

---

## 7. Best Practices

### Best Practice 1: Use `@classmethod` for Alternative Constructors
**When to apply**: Whenever you need more than one way to create an object.
**Why**: It keeps your `__init__` clean and focused on basic assignment.
```python
# GOOD: Explicit factory methods
@classmethod
def from_json(cls, data): ...

@classmethod
def from_csv(cls, row): ...
```

### Best Practice 2: Default to Instance Methods
**When to apply**: Almost always.
**Why**: 90% of OOP logic involves reading or changing an object's state. If you aren't using `self`, ask yourself if this function really belongs in this class.

### Best Practice 3: Prefer Return Values over Side Effects (Where Possible)
**When to apply**: For calculations or data retrieval.
**Why**: It makes testing easier. A function that returns a value is "Pure" and predictable; a method that changes state is "Impure" and its effect depends on what happened before.

### Best Practice 4: Follow Naming Conventions
**When to apply**: Always.
**Why**: 
*   Use `get_...` for queries that return data.
*   Use `set_...` or `update_...` for commands that change state.
*   This makes your API self-documenting.

### Best Practice 5: Document Side Effects
**When to apply**: In the docstring of any method that modifies state.
**Why**: Developers call a method expecting it to do one thing; if it secretly modifies three other attributes or writes to a file, it can cause bugs.

---

## 8. Top 3 Mistakes

### Mistake 1: Forgetting the `self` Parameter

#### What's the Problem?
Defining an instance method but forgetting to put `self` as the first argument in the `def` line.

#### Why It Happens
Muscle memory from writing standard functions or from other languages where the "instance pointer" is hidden.

#### Impact
When you call `p1.check_in()`, Python passes `p1` as an argument. If your definition is `def check_in():`, Python says: *"I gave you one argument (the object), but you said this function takes zero!"* Result: `TypeError`.

#### Incorrect Approach
```python
class Patient:
    def check_in(): # WRONG: Missing self
        print("Done")
```

#### Correct Approach
```python
class Patient:
    def check_in(self): # RIGHT
         print("Done")
```

---

### Mistake 2: Calling Class Methods as Instance Methods (Logically)

#### What's the Problem?
Using an instance method for a task that logically applies to the whole class, or vice versa.

#### Why It Happens
Laziness—it's "easier" to just make everything an instance method since you have to write `self` anyway.

#### Impact
If you use an instance method to track the "Total Patients in Hospital", you have to access an object to get that data. What if you haven't created any patients yet? You can't get the count!

#### Incorrect Approach
```python
class Hospital:
    def __init__(self):
        self.count = 0 
    
    def get_total_count(self): # WRONG: Why do I need a specific hospital instance to see the static count?
        return Hospital.count
```

#### Correct Approach
```python
class Hospital:
    _total_patients = 0

    @classmethod
    def get_total_count(cls): # RIGHT: Accessible even without an instance
        return cls._total_patients
```

---

### Mistake 3: Over-relying on Side Effects

#### What's the Problem?
Creating methods that perform many unrelated changes to an object's state at once.

#### Why It Happens
"Kitchen Sink" coding—trying to make one method do too much work to avoid writing multiple methods.

#### Impact
Extremely difficult debugging. If a `Patient.update_profile()` method updates the name, address, insurance, and medical history all at once, and a bug occurs, you don't know which state change caused the failure.

#### Incorrect Approach
```python
def update_everything(self, name, age, city, blood_type):
    self.name = name
    self.age = age
    self.city = city
    self.blood_type = blood_type
    self.save_to_db()
    self.send_email_notification()
    # TOO MANY SIDE EFFECTS!
```

#### Correct Approach
Break logic into atomic methods. Each method does one thing and does it well.
```python
def update_demographics(self, name, age, city): ...
def update_clinical_data(self, blood_type): ...
def notify_patient(self): ...
```

#### Lesson Learned
Keep methods small, focused, and explicit about what they change.
