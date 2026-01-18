---
title: "Fluid Balance Monitor"
type: app_lab
module: language_fundamentals
unit: unit_1_5_operators_and_expressions
lab_number: 5
difficulty: advanced
use_case: patient_stats
domain: healthcare
order: 5
duration_hours: 1
tags:
  topics: ["compound-expressions", "precedence"]
  subtopics: ["fluids", "balance"]
---

# Lab 5: Fluid Balance Monitor

**Module**: Language Fundamentals  
**Objective**: Calculate a patient's net fluid balance using a complex expression involving addition, subtraction, and potentially division/multiplication for scaling.  
**Difficulty**: Advanced  
**Context**: Healthcare - Intensive Care Unit (ICU)

## Generic Information
**Problem Statement**: Monitoring fluid "Ins" (IV fluids, oral intake) and "Outs" (Urine output, drainage) is critical for ICU patients. You need to calculate the "Net Balance" over a 24-hour period.

**Simplified Formula**:
`Net Balance = (IV_Intake (mL) + Oral_Intake (mL)) - (Urine_Output (mL) + Drainage (mL))`



🟦 4. Drainage (mL)
This includes all fluid drained from the body, such as:

Chest tube drainage
Surgical drain (e.g., Jackson-Pratt drain)
Nasogastric (NG) aspirate
Vomit (if measured)
Diarrhea (if measured)



## Use Case
**Title**: ICU Intake/Output Calculation  
**Description**: Calculate the 24-hour fluid status.

### Rules
- `calculate_fluid_status(iv, oral, urine, drainage, scale_factor=1.0)`
- Total Intake = `(iv + oral)`
- Total Output = `(urine + drainage)`
- Final Result = `(Total Intake - Total Output) * scale_factor`
- All inputs are `ints` or `floats`.
- Scale factor is used to convert units if needed (e.g., to Liters).

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
