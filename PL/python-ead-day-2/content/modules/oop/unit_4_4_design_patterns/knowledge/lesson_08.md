---
title: "Design Patterns: Proven Solutions for OOP"
type: knowledge
module: oop
unit: unit_4_4_design_patterns
order: 8
difficulty: advanced
tags: [oop, architecture, singleton, factory, observer, strategy]
use_case: hospital_management_system
---

# Unit 4.4: Design Patterns

## 1. What
**Design Patterns** are standardized, reusable solutions to commonly occurring problems in software design. They are not specific pieces of code or libraries; rather, they are architectural templates or "blueprints" that show you how to structure your classes and their interactions to solve a specific design challenge.

In Python, these patterns often leverage dynamic features like decorators, first-class functions, and metaclasses to provide elegant solutions.

### The Problem It Solves
When building complex systems like a **Hospital Management System**, developer teams often face the same structural questions: "How do I ensure only one database exists?", "How do I create different report types without messy if/else blocks?", or "How do I notify multiple departments when a patient is admitted?". 

Design patterns provide a **common language** and a **proven architecture** for these problems. This prevents developers from "reinventing the wheel" with buggy, hard-to-maintain house-built solutions.

### When to Use This?
Use **Singleton** when you need exactly one instance of a class (e.g., a Logger). Use **Factory** when you need to create objects but don't know the exact class until runtime. Use **Observer** for one-to-many notification systems (e.g., a Vital Monitor). Use **Strategy** when you have multiple ways to perform a task (e.g., different billing algorithms) and want to swap them easily.

---

## 2. Example

### Example 1: The Singleton (Database Connector)
Ensures only one instance of the connection pool exists throughout the application.
```python
class HospitalDB:
    _instance = None

    def __new__(cls):
        # The magic happens here: we only ever return the first instance created
        if cls._instance is None:
            print("LOG: Creating new Database Connection Pool...")
            cls._instance = super(HospitalDB, cls).__new__(cls)
        return cls._instance

# Usage
db1 = HospitalDB()
db2 = HospitalDB()
print(f"Same instance: {db1 is db2}") 
# Output: Same instance: True
```

### Example 2: The Factory (Medical Report Generator)
De-couples the creation of reports from the code that uses them.
```python
class PDFReport:
    def generate(self): return "Generating PDF Medical Summary..."

class CSVReport:
    def generate(self): return "Generating CSV Data Export..."

class ReportFactory:
    @staticmethod
    def get_report(report_type):
        """Factory logic centralized in one place."""
        formats = {"pdf": PDFReport, "csv": CSVReport}
        return formats.get(report_type.lower(), PDFReport)()

# Usage
my_report = ReportFactory.get_report("csv")
print(my_report.generate())
# Output: Generating CSV Data Export...
```

### Example 3: The Observer (Patient Alerting System)
Allows multiple "subscribers" (Nurse Station, Pager, Logger) to listen to a "Subject" (Patient Monitor).
```python
class PatientMonitor:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def trigger_alert(self, message):
        for observer in self._observers:
            observer.update(message)

class NurseStation:
    def update(self, msg): print(f"Nurse Dashboard: {msg}")

# Usage
monitor = PatientMonitor()
monitor.attach(NurseStation())
monitor.trigger_alert("Vitals Spike: Bed 4")
# Output: Nurse Dashboard: Vitals Spike: Bed 4
```

### Example 4: The Strategy (Insurance Billing)
Swaps calculation algorithms at runtime based on the patient's insurance provider.
```python
class MedicareStrategy:
    def calculate(self, amount): return amount * 0.8  # 80% coverage

class PrivateStrategy:
    def calculate(self, amount): return amount * 0.2  # 20% coverage

class BillingEngine:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, total):
        return f"Patient must pay: ${self.strategy.calculate(total)}"

# Usage
bill = BillingEngine(MedicareStrategy())
print(bill.process(1000))
# Output: Patient must pay: $800.0
```

---

## 3. Explanation

### How It Works: The Orchestration of Objects
Design patterns rely on **composition** and **interfaces** rather than deep inheritance.
- **Singleton** uses the `__new__` magic method to intercept object creation.
- **Factory** uses a mapping (like a dictionary) to hide the `if/else` logic of class selection.
- **Observer** maintains a list of references to other objects and iterates through them to broadcast state changes.
- **Strategy** passes a specialized object to a "Context" class that calls a standard method name (like `.calculate()`) regardless of which strategy is active.

### Creational vs. Behavioral Patterns
1.  **Creational (Singleton, Factory)**: Concerned with the *how* of object creation. They reduce complexity by hiding initialization logic and ensuring correct object lifecycle management.
2.  **Behavioral (Observer, Strategy)**: Concerned with *how* objects interact and distribute responsibility. They reduce "tight coupling" by allowing objects to talk to each other without knowing their exact types.

### Comparison Table: Pattern Quick-Reference
| Pattern | Purpose | Main Benefit | Healthcare Example |
| :--- | :--- | :--- | :--- |
| **Singleton** | Ensure 1 instance | Global state control | Shared Log File |
| **Factory** | Hide creation details | Easy extensibility | Multi-source EHR import |
| **Observer** | Event notification | Decoupled communication | Bedside Alarm System |
| **Strategy** | Interchangeable logic | Runtime flexibility | Dosage Analyzers |

---

## 4. Why

### 1. Architectural Stability
Patterns are like "stress-tested" blueprints. When you use an Observer pattern for a vital monitoring system, you are using a structure that has successfully handled real-time notifications in thousands of other applications.

### 2. Team Communication
By saying "We are using a Factory for the Billing module", everyone on the team immediately knows where the creation logic lives and how to add a new billing type. It provides a shorthand for complex architectural discussions.

### 3. De-coupling (Flexibility)
Patterns like Strategy allow you to change how a system works (e.g., adding a new insurance provider) without changing the core engine code. This prevents the "Ripple Effect" where one small change breaks ten other unrelated modules.

### 4. Implementation Transparency
They hide "messy" code. Instead of seeing 50 `if/elif` statements in your main logic, you see a clean `ReportFactory.create()`. This makes the high-level business logic much easier to read and audit.

---

## 5. Advantages & Disadvantages

### Advantages

#### 1. Proven Reliability
Patterns solve problems using the collective experience of decades of software engineering. They are inherently more robust than ad-hoc solutions.

#### 2. Scalability
Patterns like the Factory make it trivial to add new features. You simply add a new class and update the registry—you never have to touch existing implementation code.

#### 3. Separation of Concerns
Each pattern forces you to give a single class a single responsibility. This leads to smaller, cleaner files and easier unit testing.

### Disadvantages

#### 1. Over-Engineering
The biggest risk of patterns. Using a Factory for a class that will only ever have one subtype adds unnecessary complexity and "voodoo" to the codebase.

#### 2. Boilerplate Code
Some patterns (especially in languages like Java, though less so in Python) require creating many small classes and interfaces, which can bloat a small project.

#### 3. Learning Curve
Junior developers may find "Strategy-based" or "Singleton-heavy" code harder to follow initially, as the logic is distributed across many files rather than in a linear flow.

---

## 6. Real-World Use Cases

### Domain 1: Healthcare Telemetry
**Problem**: Real-time sensors (Heart, Oxygen, BP) need to notify a central nurses' station, a mobile app, and a medical database simultaneously.
**Solution**: Use the **Observer Pattern**. The sensor is the "Subject", and the station/app/database are "Observers".

### Domain 2: Financial Services (Banking)
**Problem**: A bank supports multiple "Account Types" (Savings, Checking, Investment) each with different interest calculation rules.
**Solution**: Use the **Strategy Pattern**. The `Account` class uses an `InterestStrategy` that can be swapped based on the account type.

### Domain 3: Game Development
**Problem**: Saving a game state requires a single `SaveManager` to handle file I/O safely to prevent data corruption from multiple write attempts.
**Solution**: Use the **Singleton Pattern** to ensure only one file-locking manager exists.

---

## 7. Best Practices

### Best Practice 1: Don't Pattern-Hunt
**When to apply**: Always.
**Why**: Don't search for a way to use a pattern. Start with the problem. If the problem naturally fits a pattern, apply it. "Pattern-first" development leads to architecture that is impossible to maintain.

### Best Practice 2: Simplify with Python Features
**When to apply**: When implementing patterns in Python.
**Why**: Python allows you to pass classes as arguments or use dictionaries of classes. This often eliminates the need for the complex "Parallel Hierarchies" seen in static languages like C++.

### Best Practice 3: Document the Pattern Name
**When to apply**: In class docstrings or module headers.
**Why**: Explicitly state: "This class implements the Strategy pattern for dosage logic." This saves subsequent developers hours of reverse-engineering your intent.

### Best Practice 4: Avoid Singleton for Testable Code
**When to apply**: For logic that doesn't *strictly* need to be a unique physical resource.
**Why**: Singletons are global state, which is hard to "reset" between unit tests. Use "Dependency Injection" (passing an object into a constructor) where possible instead.

---

## 8. Top 3 Mistakes

### Mistake 1: The "I Guess I'll Use Design Patterns" Phase

#### What's the Problem?
Applying complex patterns to small, simple scripts that don't need them.

#### Impact
"Architecture Bloat." You end up with 15 files for a script that could have been 50 lines. This makes the code harder to read and significantly slower to develop.

#### Correct Approach
Apply patterns only when you see a clear need for extensibility or when complexity starts making the code unmanageable.

---

### Mistake 2: Hard-coding in Factories

#### What's the Problem?
Writing long `if/else` or `switch` blocks inside a Factory method.

#### Impact
Every time you add a new "Product" (like a new report format), you have to modify the Factory code. This violates the **Open/Closed Principle**.

#### Correct Approach
Use a Registry (a dictionary mapping strings to class objects).
```python
# GOOD: Dynamic registry
registry = {"pdf": PDFReport, "csv": CSVReport}
return registry[type]()
```

---

### Mistake 3: Memory Leaks in Observers

#### What's the Problem?
Attaching observers to a subject but never detaching them when the observer is no longer needed.

#### Impact
Even if you delete the observer object in your main code, the `Subject` still holds a reference to it in its `_observers` list. This prevents the Python Garbage Collector from cleaning up the memory, leading to a "Memory Leak" that can crash long-running hospital servers.

#### Correct Approach
Always implement a `detach()` method and ensure it is called, or use `weakref` to store observers so they don't count towards reference totals.
