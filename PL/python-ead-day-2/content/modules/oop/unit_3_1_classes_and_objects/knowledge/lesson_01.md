---
title: Classes and Objects
type: knowledge
module: oop
unit: unit_3_1_classes_and_objects
order: 1
difficulty: intermediate
tags: [oop, classes, objects, init, self]
use_case: patient_management
---

# Unit 3.1: Classes and Objects

## 1. What
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior. In Python, the foundation of OOP is the **Class**.

A **Class** is essentially a blueprint or a template for creating **Objects**. If you think of a building, the architectural blueprint is the Class, while the actual physical building constructed from that blueprint is the Object (or **Instance**). Classes define the structure and capabilities that every object created from them will possess.

### The Problem It Solves
In procedural programming (the style used in earlier units), data and the functions that manipulate it are kept separate. For example, if you were managing a healthcare system, you might have lists for `patient_names`, `patient_ages`, and `patient_ids`. This "fragmented data" model becomes difficult to maintain as systems grow. If you change the order of one list but not the others, your data is corrupted. 

OOP solves this by **Encapsulation**—bundling data and the methods that operate on that data together into a single unit (the object). This ensures that a `Patient` object always carries its own name, age, and ID together, making the system more reliable and easier to understand.

### When to Use This?
You should use classes and objects whenever you need to model complex, real-world entities that have both state (data) and behavior (actions). It is particularly powerful in large-scale applications where data integrity and modularity are critical, such as hospital management systems, banking platforms, or large-scale eCommerce engines.

### Key Terminology
*   **Class**: The blueprint defining common attributes and behaviors.
*   **Object/Instance**: An individual realization of the class.
*   **__init__**: The constructor method used to initialize an object's state.
*   **self**: A reference to the current instance of the class.
*   **Attributes**: Variables defined within a class (Data).
*   **Methods**: Functions defined within a class (Behavior).

---

## 2. Example

### Example 1: The Simplest Class
This shows the bare minimum syntax to define a class and create an object.
```python
class Robot:
    """A minimal class representing a robot."""
    pass

# Creating an instance (Object)
my_bot = Robot()
print(my_bot) 
# Output: <__main__.Robot object at 0x...>
```

### Example 2: Constructor and Attributes
Using the `__init__` method to give our objects unique data from the start.
```python
class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id  # Instance variable
        self.name = name              # Instance variable

# Creating specific patients
alice = Patient("P101", "Alice Smith")
bob = Patient("P102", "Bob Jones")

print(f"Patient ID: {alice.patient_id}, Name: {alice.name}")
print(f"Patient ID: {bob.patient_id}, Name: {bob.name}")
# Output:
# Patient ID: P101, Name: Alice Smith
# Patient ID: P102, Name: Bob Jones
```

### Example 3: Real-World Healthcare Scenario
A more complete model including clinical data and a simple method.
```python
class MedicalRecord:
    hospital = "City General"  # Class variable (shared)

    def __init__(self, patient_name, blood_group):
        self.patient_name = patient_name
        self.blood_group = blood_group
        self.vitals = []

    def log_vital(self, reading):
        self.vitals.append(reading)
        print(f"Logged {reading} for {self.patient_name}")

# Usage
record = MedicalRecord("John Doe", "A+")
record.log_vital(72)  # Log heart rate
record.log_vital(120) # Log blood pressure
print(f"History for {record.patient_name} at {record.hospital}: {record.vitals}")
# Output:
# Logged 72 for John Doe
# Logged 120 for John Doe
# History for John Doe at City General: [72, 120]
```

### Example 4: Multiple Instances and State Isolation
Demonstrating that changing one object does not affect another.
```python
p1 = MedicalRecord("Alice", "O-")
p2 = MedicalRecord("Bob", "B+")

p1.log_vital(80)
print(f"Alice's Vitals: {p1.vitals}")
print(f"Bob's Vitals: {p2.vitals}")
# Output:
# Logged 80 for Alice
# Alice's Vitals: [80]
# Bob's Vitals: []  <- Bob remains empty!
```

---

## 3. Explanation

### How It Works: From Template to Reality
When you define a class, Python creates a "Type" object in memory. When you "call" the class (e.g., `p1 = Patient()`), Python performs a multi-step orchestration:
1.  **Memory Allocation**: It allocates a block of memory for the new object.
2.  **__init__ Trigger**: It automatically calls the `__init__` function.
3.  **Binding**: It passes the memory address of the new object as the first argument (`self`).
4.  **Assignment**: The code inside `__init__` runs, attaching data directly to that specific memory block using `self.attribute = value`.

### The `self` Parameter
The most critical concept in Python OOP is `self`. It is not a keyword (you could technically name it something else, though you shouldn't), but a naming convention. It represents the specific object being modified. Without `self`, a method wouldn't know which patient's record it is supposed to update.

### Instance vs. Class Variables
*   **Instance Variables**: Defined inside `__init__` with the prefix `self.`. These are **unique** to every object. If you have 1,000 patients, you have 1,000 unique `name` variables.
*   **Class Variables**: Defined directly inside the class body but outside any method. These are **shared** by all objects. If you change a class variable, it changes for every instance simultaneously (unless an instance has overridden it).

### Comparison Table: Variables
| Aspect | Instance Variable | Class Variable |
|--------|-------------------|----------------|
| **Source** | `self.name = ...` | `hospital = '...'` |
| **Location** | Inside `__init__` | Top of class body |
| **Storage** | Unique per object | Single copy shared by all |
| **Use Case** | Names, IDs, Vitals | Hospital Name, Tax Rates |
| **Access** | `object.name` | `Class.variable` or `object.variable` |

### Visual Representation (ASCII Diagram)
```text
  [ CLASS: Patient ] 
  (The Blueprint)
  ├── Class Variable: hospital = "General"
  ├── Method: __init__(self, name)
  └── Method: display_info(self)

        |
        | (Instantiation)
        V

  [ OBJECT: p1 ]               [ OBJECT: p2 ]
  (Distinct Memory)            (Distinct Memory)
  ├── self.name = "Alice"      ├── self.name = "Bob"
  └── hospital (points to) ----> [ Shared Hospital Data ]
```

### Performance and Memory
*   **Time Complexity**: Creating an object (instantiation) is generally **O(k)** where k is the number of attributes being initialized. Accessing an attribute is **O(1)**.
*   **Memory**: Each object has its own `__dict__` (a dictionary of its attributes). For thousands of objects, this can be memory-intensive. For extremely high-performance needs, Python offers `__slots__` to save memory, which we will explore in later units.

---

## 4. Why

### 1. Unified Data Modeling
In a healthcare application, a "Patient" is not just a string; it is a complex entity with history, insurance, and vitals. Classes allow us to model this complexity as a single unit. This prevents "sync issues" where a patient's name is updated in one list but their clinical data is left behind in another.

### 2. Code Reusability and Modularity
Once you define a `Patient` class, you can reuse it across different modules—billing, pharmacy, and triage. You don't need to rewrite the logic for how a patient is initialized or how their vitals are calculated. This modularity makes the codebase easier to test and debug because issues can be isolated to a specific class.

### 3. Maintainability (The "Single Source of Truth")
If the hospital changes its policy on how patient IDs are formatted, you only update the `__init__` method in the `Patient` class. Every part of the application that creates patients will immediately follow the new rule. In a procedural system, you might have to find and update every function that handles IDs.

### 4. Data Safety through Encapsulation
By using classes, you can control how data is accessed and modified. In future units, we will see how we can "hide" data (Private Attributes) so that it can't be accidentally deleted. Even at this basic level, keeping data inside objects prevents global variable clutter, which is a common source of bugs in large Python scripts.

---

## 5. Advantages & Disadvantages

### Advantages

#### 1. Real-World Mapping
Classes allow developers to think in terms of objects they can touch and see. Mapping a "Banking Transaction" to a `Transaction` class is much more intuitive than mapping it to a set of parallel arrays.

#### 2. Scalability
OOP projects are significantly easier to scale. When you need to add a "Newborn" specialty to your healthcare system, you can build upon your existing `Patient` logic rather than starting over.

#### 3. Collaboration
In a team, one developer can work on the `Doctor` class while another works on the `Appointment` class. As long as they agree on how the classes interact, they won't step on each other's toes.

### Disadvantages

#### 1. Learning Curve
For beginners, concepts like `self`, constructors, and class vs. instance data can be overwhelming. It requires a shift in thinking from "Step 1, Step 2, Step 3" (procedural) to "How do these entities interact?" (object-oriented).

#### 2. Overhead for Small Scripts
If you are writing a 20-line script to rename files in a folder, creating a `FileRenamer` class is likely overkill. Procedural programming is often faster and cleaner for simple, linear tasks.

#### 3. Memory Footprint
Because every object in Python carries its own dictionary of attributes, object-oriented code typically uses more RAM than equivalent code using simple lists or tuples. This rarely matters for business apps but is critical for high-perf systems.

---

## 6. Real-World Use Cases

### Domain 1: Healthcare
**Problem**: Tracking patient triage status across multiple departments without losing data integrity.
**Solution**: Use a `Patient` class to encapsulate demographics and a `VitalsHistory` object within it.
```python
class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority # 1: Critical, 3: Stable
        self.admitted = False

    def admit(self):
        self.admitted = True
        print(f"Patient {self.name} is now admitted.")

# Scenario: ER Triage
triage_list = [Patient("James", 1), Patient("Sarah", 3)]
for p in triage_list:
    if p.priority == 1:
        p.admit()
```

### Domain 2: eCommerce
**Problem**: Managing a shopping cart where items need to be added, removed, and totals calculated dynamically.
**Solution**: A `CartItem` class to store product details and a `ShoppingCart` class to manage the collection.
```python
class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price

# Every item in the cart is a Product instance
p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 25)

shopping_cart = [p1, p2]
total = sum(item.price for item in shopping_cart)
print(f"Total: ${total}")
```

### Domain 3: Banking
**Problem**: Ensuring that every transaction is logged with a timestamp and account reference and cannot be easily forged.
**Solution**: Use an `Account` class to manage balances and a `Transaction` class for every movement of money.
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"New balance for {self.owner}: {self.balance}")

# Banking Scenario
acc = BankAccount("Emily", 5000)
acc.deposit(1000)
```

---

## 7. Best Practices

### Best Practice 1: Use PascalCase for Class Names
**When to apply**: Every time you define a class.
**Why**: Following PEP 8 standards (`PascalCase` for classes, `snake_case` for functions) makes it immediately obvious which parts of your code are blueprints and which are actions.

### Best Practice 2: Initialize All Attributes in `__init__`
**When to apply**: During class design.
**Why**: Avoid creating attributes "on the fly" outside the constructor. If an attribute doesn't have a value yet, initialize it to `None` or an empty list. This prevents `AttributeError` and makes your code self-documenting.

### Best Practice 3: Always Use `self` for Instance Access
**When to apply**: Inside any instance method.
**Why**: Even if it seems redundant, referring to attributes via `self.attribute` is mandatory for clarity and correctness. It distinguishes instance data from local variables within the method.

### Best Practice 4: Document Your Classes
**When to apply**: At the top of every class definition.
**Why**: Use docstrings to explain what the class represents and what its primary attributes are. This is essential for maintainability in team environments.

### Best Practice 5: Keep Classes Focused (SRP)
**When to apply**: Architectural planning.
**Why**: Follow the Single Responsibility Principle. A `Patient` class should manage patient data, not generate a PDF billing report. Create a separate `ReportGenerator` class for that.

---

## 8. Top 3 Mistakes

### Mistake 1: Forgetting the `self` Parameter in Methods

#### What's the Problem?
Defining a method without `self` as the first parameter, or forgetting to use `self.` to access variables.

#### Why It Happens
Coming from languages where the "this" context is implicit, or simply a typo.

#### Impact
Python will raise a `TypeError` when you call the method because it automatically tries to pass the instance as the first argument, but the method isn't set up to receive it.

#### Incorrect Approach
```python
class Patient:
    def __init__(self, name):
        self.name = name

    def say_name(): # ERROR: Missing self argument
        print(name)  # ERROR: NameError (no local name)
```

#### Correct Approach
```python
class Patient:
    def __init__(self, name):
        self.name = name

    def say_name(self): 
        print(self.name)
```

---

### Mistake 2: Using Mutable Defaults as Class Variables

#### What's the Problem?
Defining a list or dictionary at the class level intending for it to be unique to each instance.

#### Why It Happens
Misunderstanding the difference between class-level and instance-level storage.

#### Impact
**Data Leakage.** Every instance of the class will share the *exact same list*. If Patient A gets an allergy, Patient B suddenly has it too.

#### Incorrect Approach
```python
class Patient:
    allergies = []  # Shared by ALL patients!

p1 = Patient()
p1.allergies.append("Peanuts")
p2 = Patient()
print(p2.allergies) # Output: ["Peanuts"] - DANGEROUS!
```

#### Correct Approach
```python
class Patient:
    def __init__(self):
        self.allergies = [] # Unique to this specific patient
```

---

### Mistake 3: Identity Confusion (`is` vs `==`)

#### What's the Problem?
Assuming that two objects are "the same" just because they contain the same data.

#### Why It Happens
Generalizing behavior from strings or integers to custom objects without understanding memory references.

#### Impact
Logic errors in `if` statements or search algorithms. Your code might think a record is missing when it's actually there under a different memory reference.

#### Incorrect Approach
```python
p1 = Patient("ID-01")
p2 = Patient("ID-01")

if p1 is p2: # This is FALSE!
    print("Match")
```

#### Correct Approach
Always compare specific attributes (like IDs) unless you have implemented custom equality logic (which we will cover in Unit 2.4).
```python
if p1.patient_id == p2.patient_id:
    print("Same patient data")
```

#### Lesson Learned
`is` checks memory address (Identity). `==` checks data (Equality). Custom objects are unique by identity unless told otherwise.
