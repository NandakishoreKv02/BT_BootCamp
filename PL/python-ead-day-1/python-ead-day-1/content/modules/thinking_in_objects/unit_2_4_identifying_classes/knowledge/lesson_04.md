---
title: "The Art of Modeling: Identifying Classes"
type: knowledge
module: thinking_in_objects
unit: unit_2_4_identifying_classes
order: 1
difficulty: intermediate
tags:
  subtopics:
    - noun-verb-analysis
    - bce-model
    - god-objects
    - cohesion
---

# Unit 2.4: Identifying Classes – Analysis & Modelling

## 1. What
**Object Modeling** is the process of translating informal business requirements into a formal set of software classes. It is the bridge between a doctor saying "I need to track prescriptions" and a developer writing `class Prescription:`.

The goal is to identify classes that are **Stable**, **Highly Cohesive** (they do one thing well), and **Loosely Coupled** (they don't depend too much on others).

## 2. Example

### The Requirement
*"A Nurse needs to register a Patient. The system should calculate the Triage Score based on vitals and assign the patient to a Bed."*

### The Noun-Verb Analysis
- **Nouns (Potential Classes)**: Nurse, Patient, System, Triage Score, Vitals, Bed.
- **Verbs (Potential Methods)**: Register, Calculate, Assign.

### The Refined Model
1.  `Patient` (Entity): Stores the name and MRN.
2.  `Bed` (Entity): Stores availability.
3.  `TriageController` (Control): Contains the logic for the `calculate_score` verb.
4.  `RegistrationUI` (Boundary): Handles the `register` verb (user input).

## 3. Explanation

### A. Noun-Verb Analysis Technique
This is the "First Pass" of modeling. 
1.  **List all Nouns**: These are your "Candidate Classes."
2.  **List all Verbs**: These are your "Candidate Methods."
3.  **Filter**: Some nouns are just attributes (e.g., "Age" is an attribute of `Patient`), and some are outside the system's scope (e.g., "Hospital Building").

### B. BCE Classification (Boundary-Control-Entity)
To prevent messy code, professional architects group classes into three tiers:
1.  **Entity**: The Nouns. Data that persists (e.g., `Patient`, `Medication`). They are the "Heart" of the system.
2.  **Boundary**: The "Skin". How the system talks to the outside world (e.g., `CLI`, `WebPage`, `ScannerInterface`).
3.  **Control**: The "Brain". The logic that connects the Skin to the Heart (e.g., `AdmissionLogic`, `BillingEngine`).

### C. The "God Object" Trap
A **God Object** is a class that "Knows too much" and "Does too much." 
- *Signs*: It has 50 attributes, 100 methods, and is named something vague like `SystemManager` or `App`.
- *Cure*: Decomposition. Break it down into smaller entities and controllers.

## 4. Why
Why not just have one big `Hospital` class?
1.  **Maintenance**: If the `Billing` logic changes, you shouldn't have to risk breaking the `Surgery` code.
2.  **Teamwork**: Five developers can work on five different classes simultaneously. You can't do that with one giant file.
3.  **Stability**: Entities like `Patient` rarely change over 10 years, whereas "Boundaries" (like a mobile vs. web UI) change every year. Separating them keeps the core stable.

## 5. Advantages & Disadvantages

### Advantages
- **Scalability**: New features are added as new classes, not by expanding old ones.
- **Readability**: The code reads like a story about the domain (`Patient` is assigned to `Bed`).
- **Testability**: It's easier to test a small `TriageScore` calculator than a 5,000-line manager.

### Disadvantages
- **Analysis Paralysis**: Spending too much time drawing diagrams instead of writing code.
- **Complexity**: For very small apps, having three classes (BCE) instead of one simple script might feel like "Over-engineering."

## 6. Real-World Use Cases: EHR Architecture
In an **Electronic Health Record (EHR)** system like Epic:
- **Entities**: `Patient`, `Encounter`, `Observation`, `Order`. These are stored in the database.
- **Boundaries**: The `NurseWorkspace`, the `DoctorPortal`, the `HL7Connector`.
- **Controllers**: `DrugInteractionChecker`, `InsuranceValidator`. When a doctor orders a drug (Boundary), the Interaction Checker (Control) looks at the Patient's history (Entity).

## 7. Best Practices
1.  **Single Responsibility**: A class should have one reason to change. (A `Patient` class shouldn't change just because the `Billing` tax rate changed).
2.  **Noun Consistency**: Use the same names that the industry uses. If nurses call it a "Chart," don't name your class `PatientDataContainer`.
3.  **Avoid "Manager" Suffixes**: Names like `DataManager` or `ObjectManager` often indicate a God Object. Try a more specific name like `InventoryController`.

## 8. Summary
Modeling is not about writing code; it's about **mapping reality**. By identifying stable Nouns and grouping them with the BCE pattern, you create a software architecture that can survive for decades. Remember: Nouns are the foundation, Verbs are the mechanics, and God Objects are the enemy.
