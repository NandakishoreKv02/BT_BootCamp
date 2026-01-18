# Lab 6: Critical Dosage Auditor - Tasks

## Task 1: The Calculation
In `calculate_concentration`, identify the line of code that could fail (division) and place it in a `try` block.

## Task 2: Specific Error Handling
Implement an `except` block that catches both `ZeroDivisionError` and `TypeError` on the same line.
- Print: `AUDIT: Calculation Failed`.
- Return `0.0`.

## Task 3: The Success Path
Implement an `else` block. 
- Print: `AUDIT: Calculation Successful`.
- Return the calculated concentration.

## Task 4: The Mandatory Log
Implement a `finally` block. 
- Print: `AUDIT: Transaction Completed`.
- *Wait!* If you return in `else` and `except`, will `finally` run? (Yes, Python guarantees it).
