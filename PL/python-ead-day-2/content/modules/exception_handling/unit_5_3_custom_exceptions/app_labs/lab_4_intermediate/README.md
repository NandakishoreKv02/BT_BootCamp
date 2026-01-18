---
title: "Pharmacy System - Validation Patterns"
type: app_lab
module: exception_handling
unit: unit_5_3_custom_exceptions
lab_number: 4
difficulty: intermediate
use_case: hybrid_exceptions
domain: healthcare
order: 4
duration_hours: 1.5
tags:
  topics: ["exceptions", "custom-vs-builtin", "validation"]
  subtopics:
    - business-logic-errors
    - input-validation
---

# Lab 4: Pharmacy System - Validation Patterns

**Objective**: Differentiate between system-level errors (input types) and business-logic errors (medical contraindications) by using both built-in and custom exceptions.

## Generic Information
**Problem Statement**: Not every error needs a custom class. If a user passes a string where a number belongs, use `TypeError`. But if a user tries to prescribe a drug with a lethal interaction, using `ValueError` is too vague. You need a semantic `DrugInteractionError`.
**Goals**:
- Implement `dispense_medication(drug_name, quantity)`.
- Use `TypeError` if quantity is not an integer.
- Use a custom `DrugInteractionError` if the drug is forbidden.

## Use Case: Hybrid Exceptions
The "e-Script" system needs to validate prescriptions. It should throw standard errors for data-type issues but specific medical errors for safety violations.

## Lab Structure
1.  **Custom Class**: `DrugInteractionError`.
2.  **Logic**: Validating both the type of the quantity and the safety of the drug.
3.  **Handler**: Distinguishing between these two types of errors to show different UI messages.

## Getting Started
"Fail Early": Check the input type first (`isinstance`), then check the business rules.
