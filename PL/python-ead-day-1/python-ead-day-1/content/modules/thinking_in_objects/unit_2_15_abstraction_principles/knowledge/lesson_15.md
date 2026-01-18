---
title: "The Invisible Architecture: Abstraction & Design Principles"
type: knowledge
module: thinking_in_objects
unit: unit_2_15_abstraction_principles
order: 1
difficulty: advanced
tags:
  subtopics:
    - abstraction
    - abstract-base-classes
    - abc-module
    - srp
    - clean-design
---

# Unit 2.15: Abstraction & Design Principles

## 1. What
**Abstraction** is the process of hiding implementation details and showing only the functionality to the user. It helps reduce programming complexity and effort.

In Python, we use **Abstract Base Classes (ABCs)** via the `abc` module to define "Blueprints" or "Contracts." An abstract class can have methods that have no implementation (abstract methods). Any class that inherits from this abstract class **MUST** implement these methods to be instantiated.

**Single Responsibility Principle (SRP)** is a design principle stating that every class should have responsibility over a single part of the functionality provided by the software.

## 2. Example

### The Abstract Diagnostic Scanner
You shouldn't be able to buy a generic "Medical Scanner." You buy an "MRI" or a "CT." The `Scanner` class is abstract.

```python
from abc import ABC, abstractmethod

class MedicalScanner(ABC):
    """The Abstract Blueprint (Implementation hidden)"""
    
    @abstractmethod
    def scan(self, patient_id):
        """Forces all child classes to have this method."""
        pass

    def power_on(self):
        """Concrete method: All scanners power on the same way."""
        print("System booting...")

class MRIScanner(MedicalScanner):
    """The Concrete Implementation"""
    
    def scan(self, patient_id):
        return f"MRI: High-resolution soft tissue data for {patient_id}."

class XRayScanner(MedicalScanner):
    """Another Concrete Implementation"""
    
    def scan(self, patient_id):
        return f"X-Ray: Bone density image for {patient_id}."

# Usage
# m = MedicalScanner() # ERROR: Cannot instantiate abstract class
mri = MRIScanner()
print(mri.scan("P-101")) # Output: MRI: ...
```

## 3. Explanation

### A. The `abc` Module
Python doesn't have a built-in `abstract` keyword like Java. We inherit from the `ABC` class and use the `@abstractmethod` decorator to indicate which methods are required "contracts."

### B. Encapsulation vs Abstraction
- **Encapsulation**: Hiding *data* (Unit 2.10) to protect it from outside interference.
- **Abstraction**: Hiding *complexity* (Unit 2.15) to make the system easier to use. You know *what* the `scan()` method does, but you don't care *how* the magnets or rays produce the image.

### C. Single Responsibility Principle (SRP)
A common mistake is creating a `Patient` class that manages vitals, calculates invoices, and sends emails.
- **Bad Design**: One class does everything (The "God Object").
- **Good Design**: `Patient` manages data, `BillingEngine` calculates costs, `Notifier` sends emails.

## 4. Why
1.  **Consistency**: Ensures every programmer on the team follows the same rules for a diagnostic tool.
2.  **Modularization**: SRP makes code easier to test. It's easier to verify a billing calculator if it's not buried inside a patient record class.
3.  **Scalability**: You can add new scanners (Ultrasound, PET) easily because the "Blueprint" is already defined.

## 5. Summary Table

| Principle | Core Idea | Clinical Example |
| :--- | :--- | :--- |
| **Abstraction** | Hide details, show intent. | "Power on Hospital" (Don't care about the generator logic). |
| **ABC** | Enforce method implementation. | All `TreatmentPlan` subclasses MUST have a `calculate_cost()`. |
| **SRP** | One class = One job. | `PatientRecord` handles medical data; `EmailService` handles comms. |

## 6. Real-World Use Case: Reporting System
A hospital generator creates `PDFReport`, `CSVReport`, and `HTMLReport`. Every report inherits from an abstract `Report` class with an abstract `generate()` method. The main dashboard doesn't need to know how to draw a PDF; it just calls `.generate()` on whatever report object it has.

## 7. Best Practices
1.  **Rule of One**: If a class does more than one thing, split it.
2.  **Interface over Implementation**: Program to the "Abstract" type, not the specific "Concrete" type.
3.  **Meaningful Abstraction**: Don't abstract for the sake of it. If you only ever have one way to do something, you might not need an ABC yet.

## 8. Conclusion
Abstraction and Design Principles move us from "Writing Code" to "Architecting Systems." By defining clear contracts and keeping responsibilities focused, we create medical software that is robust, predictable, and safe for clinical use.
