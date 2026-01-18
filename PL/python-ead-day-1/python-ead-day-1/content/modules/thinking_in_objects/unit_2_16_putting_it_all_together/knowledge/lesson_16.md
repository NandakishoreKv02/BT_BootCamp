---
title: "The Architect's Mindset: Putting It All Together"
type: knowledge
module: thinking_in_objects
unit: unit_2_16_putting_it_all_together
order: 1
difficulty: advanced
tags:
  subtopics:
    - system-design
    - refactoring
    - anti-patterns
    - software-architecture
    - capstone
---

# Unit 2.16: Putting It All Together

## 1. The Design Lifecycle
Writing "Class syntax" is easy. Designing a system is hard. This unit bridges the gap by walking through the full lifecycle of a feature.

### Step 1: Requirements Analysis (The "What")
Example: *"We need a system for the Organ Transplant Center. It tracks Donors and Recipients. A match is made based on Blood Type and Urgency. When matched, an Organ is 'Reserved'."*

### Step 2: Noun/Verb Extraction (The "Who" and "How")
- **Nouns (Classes)**: `Donor`, `Recipient`, `Organ`, `TransplantCenter`.
- **Verbs (Methods)**: `register_donor()`, `find_match()`, `reserve_organ()`.

### Step 3: Relationship Mapping
- A `TransplantCenter` *has-many* `Donors` (Aggregation).
- A `Recipient` *needs-a* `Organ` (Dependency).
- An `Organ` *belongs-to* a `Donor` (Composition).

## 2. Refactoring: From Script to System
Many developers start with procedural scripts. Refactoring to OOP makes the code scalable.

### Procedural Mess (The "Before")
```python
donors = []
recipients = []

def add_donor(name, type):
    donors.append({"name": name, "type": type})

def match():
    # ... nested loops ...
    pass
```

### OOP Architecture (The "After")
```python
class Donor:
    def __init__(self, name, blood_type):
        self.name = name
        self.organs = []

class TransplantCenter:
    def match_organ(self, recipient):
        # ... logic inside the center ...
        pass
```

## 3. Common OOP Anti-Patterns
Avoiding bad habits is as important as learning good ones.

### A. The "God Object"
A class that knows too much and does too much.
- **Symptom**: `HospitalSystem` class with 50 methods for billing, staffing, parking, and surgery.
- **Fix**: Apply SRP. Split into `BillingService`, `StaffManager`, etc.

### B. The "Data Clump"
Passing the same 3-4 arguments together everywhere.
- **Symptom**: `schedule_surgery(patient_name, patient_age, patient_id)`
- **Fix**: Abstraction. Pass a `Patient` object instead.

### C. "Poltergeists" (Useless Classes)
Classes with no state and only one method that just calls another class.
- **Symptom**: `NameValidatorManagerController`.
- **Fix**: Just put the validation method where it belongs or make it a static utility.

## 4. The Industry Checklist
Before you say "I'm done," check your code against this list:
1.  **Encapsulation**: Are internal variables private (`_`)?
2.  **Type Hints**: Do functions verify inputs (`def add(self, p: Patient) -> bool:`)?
3.  **Docstrings**: Does every class and complex method have a description?
4.  **Testing**: Can you write a test case without setting up 50 global variables?

## 5. Real-World Use Case: The Vaccination Campaign
Imagine managing a city-wide Flu Shot campaign.
- **Objects**: `Citizen`, `Clinic`, `VaccineBatch`.
- **Statics**: `VaccinationCenter.TOTAL_VACCINATED`.
- **Inheritance**: `FluVaccine` vs `CovidVaccine` inheriting from `Vaccine`.
- **Abstraction**: `Clinic` doesn't know how `Vaccine` works, it just calls `vaccine.administer()`.

## 6. Conclusion
You now have the tools to think in objects. You can see the world not as a list of instructions, but as a network of interacting entities. This is the foundation of all modern software engineering.
