---
title: "The High-Speed Stream - Performance Best Practices"
type: app_lab
module: exception_handling
unit: unit_5_4_best_practices
lab_number: 6
difficulty: expert
use_case: performance_optimization
domain: healthcare
order: 6
duration_hours: 3.0
tags:
  topics: ["exceptions", "performance", "tight-loops"]
  subtopics:
    - overhead
    - optimization
    - stream-processing
---

# Lab 6: The High-Speed Stream - Performance Best Practices

**Objective**: Optimize a high-frequency data stream by choosing between EAFP and LBYL based on expected error rates.

## Generic Information
**Problem Statement**: Exceptions are "expensive" in Python. Creating the traceback object takes time. In a tight loop (e.g., processing 1,000,000 sensor readings), if you expect many failures (e.g., 50% are noise), using `try-except` will slow down your code by 2x-5x compared to an `if` check.
**Goals**:
- Implement both EAFP and LBYL versions of a filter.
- Understand the "Tipping Point": EAFP is faster when errors are rare (Happy Path), LBYL is faster when errors are frequent.

## Use Case: Performance Optimization
An "ECG-Analyzer" processes waveform samples. If a sample is `None` or out-of-range, it should be skipped. Since sensor noise is common, we must optimize the loop.

## Lab Structure
1.  **Stream Processor**: Processing a list of 100,000 items.
2.  **EAFP implementation**: Using `try-except`.
3.  **LBYL implementation**: Using `if`.

## Getting Started
In Python, `try` itself is practically free. It's the `except` block that is expensive.
