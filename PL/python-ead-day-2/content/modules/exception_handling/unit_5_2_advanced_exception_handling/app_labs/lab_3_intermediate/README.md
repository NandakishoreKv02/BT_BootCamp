---
title: "API Connector - Exception Chaining"
type: app_lab
module: exception_handling
unit: unit_5_2_advanced_exception_handling
lab_number: 3
difficulty: intermediate
use_case: error_wrapping
domain: healthcare
order: 3
duration_hours: 1.5
tags:
  topics: ["exceptions", "chaining", "raise-from"]
  subtopics:
    - abstraction-layers
    - debugging
---

# Lab 3: API Connector - Exception Chaining

**Objective**: Wrap low-level library exceptions (like connection timeouts) into high-level application exceptions while preserving the original traceback for debugging.

## Generic Information
**Problem Statement**: Your code uses a 3rd party library `FakeRequests` which raises `FakeTimeoutError`. Your main application doesn't want to know about `FakeTimeoutError`; it wants a generic `ServiceUnavailableError`. However, if you just raise the new error, you lose the info about the timeout.
**Goals**:
- Implement `fetch_patient_data()`.
- Simulate a low-level error.
- Catch it and raise a customized high-level error using `raise ... from ...`.

## Use Case: Error Wrapping
The "HospitalPortal" connects to "LegacyBilling". If "LegacyBilling" times out, the portal should report `BillingServiceDown` but keep the `Timeout` details in the logs for the sysadmin.

## Lab Structure
1.  **Low-level Simulation**: A function that fails.
2.  **Chaining Logic**: The wrapper using `raise from`.
3.  **Verification**: Checking `__cause__`.

## Getting Started
Use `raise NewException("msg") from original_exception`. This sets `NewException.__cause__` to `original_exception`.
