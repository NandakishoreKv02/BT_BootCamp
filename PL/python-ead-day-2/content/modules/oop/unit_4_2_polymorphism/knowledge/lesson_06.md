---
title: Polymorphism
type: knowledge
module: oop
unit: unit_4_2_polymorphism
order: 2
difficulty: intermediate
tags:
  subtopics:
    - duck-typing
    - method-overriding
    - operator-overloading
    - polymorphism
    - abstract-base-classes
---

# Unit 4.2: Polymorphism

## 1. What

**Polymorphism** (from Greek "many forms") is the ability of different objects to respond to the same method call in a way specific to their type. In Python, this is primarily achieved through **Duck Typing** ("If it walks like a duck and quacks like a duck, it's a duck") and inheritance-based method overriding.

### What Problem Does It Solve?
It removes the need for type checking (e.g., `if isinstance(obj, TypeA): ...`). Instead of writing separate logic for each type, you write generic code that works with *any* object that implements the required interface.

### When Would You Use This?
- **Generic Collections**: Iterating over a list of mixed objects (e.g., Doctors, Nurses, Admins) and initializing a common action (e.g., `calculate_pay()`).
- **Flexible APIs**: Creating functions that accept any object behaving like a file (has `.read()`) or a list (has `__len__`).
- **Operator Overloading**: Defining how `+`, `-`, or `==` behave for your custom classes.

### Key Terminology
| Term | Meaning |
|------|---------|
| Duck Typing | Checking for behavior (methods/attrs) rather than inheritance type. |
| Method Overriding | Subclasses providing a specific implementation of a parent method. |
| Operator Overloading | Customizing built-in operators like `+` using dunder methods like `__add__`. |
| Interface | A shared set of methods that different classes implement. |

---

## 2. Example

### Example 1: Duck Typing (No Inheritance)

```python
class PDFExporter:
    def export(self, data):
        print(f"Exporting {data} to PDF...")

class CSVExporter:
    def export(self, data):
        print(f"Exporting {data} to CSV...")

def perform_export(exporter, data):
    # Does not care about the class type, only that it has .export()
    exporter.export(data)

perform_export(PDFExporter(), "Report") # Output: Exporting Report to PDF...
perform_export(CSVExporter(), "Report") # Output: Exporting Report to CSV...
```

### Example 2: Polymorphism via Inheritance (Method Overriding)

```python
class Notification:
    def send(self, message):
        raise NotImplementedError("Subclasses must implement send()")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

notifications = [EmailNotification(), SMSNotification()]

for note in notifications:
    note.send("Alert!")  
    # Output: 
    # Sending Email: Alert!
    # Sending SMS: Alert!
```

### Example 3: Operator Overloading

```python
class MonetaryAmount:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies do not match")
        return MonetaryAmount(self.amount + other.amount, self.currency)

    def __str__(self):
        return f"{self.amount} {self.currency}"

m1 = MonetaryAmount(100, "USD")
m2 = MonetaryAmount(50, "USD")
total = m1 + m2  # Invokes __add__
print(total)     # Output: 150 USD
```

### Example 4: Interface-like Programming with ABC

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"Charged ${amount} via Stripe")

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Charged ${amount} via PayPal")

def checkout(gateway: PaymentGateway, amount: float):
    gateway.process_payment(amount)

checkout(Stripe(), 99.99)
```

---

## 3. Explanation

### How It Works using Duck Typing
Python determines if a method invocation is valid at **runtime**.
1. Code calls `obj.method()`.
2. Python checks if `obj` has an attribute named `method`.
3. If yes, it attempts to call it.
4. If no, `AttributeError` is raised.
Strict inheritance hierarchies are not required; only the method signature matters.

### Method Resolution in Inheritance
When accessing a method `obj.method()` where `obj` is an instance of a subclass:
1. Python checks the instance namespace.
2. It checks the class namespace.
3. It walks up the MRO (Method Resolution Order) looking for the method.
4. The first implementation found is used (enabling overriding).

### Operator Overloading Mechanism
When you write `a + b`:
1. Python translates this to `a.__add__(b)`.
2. If `a` doesn't implement `__add__` (or returns `NotImplemented`), Python tries `b.__radd__(a)` (reverse add).
3. If neither works, `TypeError` is raised.

### Visual Representation

**Polymorphism in Action**
```text
           [Interface: send()]
              ^        ^
              |        |
    [EmailSender]    [SMSSender]
    send() {...}     send() {...}

       Code: object.send()
             /       \
      Is it Email?   Is it SMS?
      Run Email logic Run SMS logic
```

---

## 4. Why

### 1. Flexible and Extensible Code
You can add new types to your system without changing the code that uses them. For example, adding a `SlackNotification` class requires zero changes to the `perform_notification()` function.

### 2. Cleaner Interfaces
Instead of writing functions with long chains of `if type(x) == TypeA elif type(x) == TypeB`, you rely on the objects themselves to handle the behavior. This satisfies the **Open/Closed Principle** (open for extension, closed for modification).

### 3. Pythonic Consistency
Python's core is built on polymorphism. `len()` works on strings, lists, dicts, and custom objects because they all implement `__len__`. `for` loops work on anything with `__iter__`. Adopting this style makes your classes integrate seamlessly with the language.

### 4. Simplified Maintenance
Logic is encapsulated within the specific class rather than scattered in global manager functions. If `Email` logic changes, you only edit `EmailNotification`.

---

## 5. Advantages & Disadvantages

### Advantages

#### 1. Interchangeability
- **Description**: Objects can be swapped easily if they share an interface.
- **Benefit**: Makes mocking objects for unit testing extremely easy.

#### 2. Reduction of Conditional Logic
- **Description**: Replaces large `switch` or `if/else` blocks based on types.
- **Benefit**: Code becomes more readable and less prone to errors when adding new types.

#### 3. Uniform Interface
- **Description**: Different complex implementations are hidden behind a simple, common method name (e.g., `.save()`).
- **Benefit**: Reduces cognitive load for developers using the API.

### Disadvantages

#### 1. Runtime Errors (Duck Typing)
- **Description**: Since checks happen at runtime, passing an object missing the required method causes a crash mid-execution.
- **Workaround**: Use Abstract Base Classes (ABCs) or Type Hinting (`Protocol` from `typing`) to enforce interfaces.

#### 2. Code Navigation Difficulty
- **Description**: When clicking "Go to Definition" on a polymorphic call (e.g., `exporter.export()`), IDEs may not know which specific implementation is being called.
- **Workaround**: Use type hints to help IDEs resolve references.

#### 3. Hidden Complexity
- **Description**: Operator overloading can be confusing if behavior isn't intuitive (e.g., using `+` to subtract).
- **Workaround**: overload operators only when the semantic meaning is obvious (like adding vectors or currencies).

---

## 6. Real-World Use Cases

### Healthcare: Medical Imaging Processing
**Problem**: A system needs to process images from MRI, CT, and X-Ray machines, which all output different raw formats but need standard processing steps.
**Solution**: Polymorphic `ImageProcessor` interface.
```python
class MRIProcessor:
    def process(self, raw_data):
        return self._reconstruct_3d(raw_data)

class XRayProcessor:
    def process(self, raw_data):
        return self._enhance_contrast(raw_data)

def analyze_scan(processor, data):
    image = processor.process(data)
    # Generic analysis logic...
```

### eCommerce: Shipping Calculators
**Problem**: Different carriers (FedEx, UPS, USPS) have different rate calculation APIs.
**Solution**: Common `calculate_shipping` method.
```python
class FedEx:
    def calculate_rate(self, weight):
        return 5.0 + (weight * 0.5)

class UPS:
    def calculate_rate(self, weight):
        return 4.5 + (weight * 0.6)

def get_best_rate(carriers, weight):
    return min(c.calculate_rate(weight) for c in carriers)
```

### Banking: Transaction Processing
**Problem**: Processing deposits, withdrawals, and transfers requires different validation and database updates, but the banking core wants to just "execute transaction".
**Solution**: Polymorphic `Transaction` classes.
```python
class Deposit:
    def execute(self, account):
        account.balance += self.amount

class Withdrawal:
    def execute(self, account):
        if account.balance >= self.amount:
            account.balance -= self.amount

# The transaction log runner just calls .execute() on everything
for txn in daily_transactions:
    txn.execute(target_account)
```

---

## 7. Best Practices

### Best Practice 1: Use Abstract Base Classes (ABCs) for Strict Interfaces
**When to apply**: When building large systems where missing a method implementation would be catastrophic.
**Why**: Catches missing methods at instantiation time rather than runtime.

### Good Practice
```python
from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render(self): 
        pass 
        # Forces subclasses to implement this
```

### Best Practice 2: Follow the Liskov Substitution Principle (LSP)
**When to apply**: When overriding methods in subclasses.
**Why**: Subclasses should be interchangeable with their base class without breaking the application. They should accept the same arguments and return the same types.

### Best Practice 3: Use Type Hints with Protocols
**When to apply**: When using Duck Typing but wanting IDE support and static checking.
**Why**: Defines the expected behavior explicitly.

### Good Practice
```python
from typing import Protocol

class Exportable(Protocol):
    def export(self) -> None: ...

def run_export(obj: Exportable):
    obj.export()
```

---

## 8. Top 3 Mistakes

### Mistake 1: Relying on `type()` or `isinstance()` Checks
**What's the Problem?** Manually checking types destroys the flexibility of polymorphism.
**Correct Approach**: Just call the method. If you need safety, use `try/except AttributeError` or ABCs.

### Incorrect Approach
```python
def play_media(file):
    if isinstance(file, MP3):
        file.play_audio()
    elif isinstance(file, MP4):
        file.play_video()
```
### Correct Approach
```python
def play_media(file):
    # Both classes should simply have a .play() method
    file.play() 
```

### Mistake 2: Violating Method Signatures in Overrides
**What's the Problem?** Changing the arguments or return type in a subclass method.
**Impact**: Code expecting the parent class interface breaks when given the subclass.

### Incorrect Approach
```python
class Parent:
    def save(self, data): ...

class Child(Parent):
    def save(self, data, filename): ... # Breaks compatibility!
```

### Mistake 3: Overloading Operators Counter-Intuitively
**What's the Problem?** Defining `__sub__` ( - ) to perform addition, or using operators for actions that don't map to math/logic.
**Impact**: Confuses other developers and makes code unreadable.

### Lesson Learned
Only use operator overloading when the operation has a natural, widely understood meaning for that data type (e.g., adding two time durations).
