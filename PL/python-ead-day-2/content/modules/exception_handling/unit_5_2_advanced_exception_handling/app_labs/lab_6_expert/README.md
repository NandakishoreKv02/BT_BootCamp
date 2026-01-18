---
title: "Critical Service Broker - Inspecting Exception Objects"
type: app_lab
module: exception_handling
unit: unit_5_2_advanced_exception_handling
lab_number: 6
difficulty: expert
use_case: dynamic_routing
domain: healthcare
order: 6
duration_hours: 3.0
tags:
  topics: ["exceptions", "inspection", "routing"]
  subtopics:
    - error-codes
    - dynamic-logic
    - exception-args
---

# Lab 6: Critical Service Broker - Inspecting Exception Objects

**Objective**: Create a smart service broker that routes retries based on specific error codes hidden inside exceptions, demonstrating deep inspection of exception objects.

## Generic Information
**Problem Statement**: An API raises `ServiceError(code, message)`.
- If `code == 503`: Retry immediately (Temporary glitch).
- If `code == 404`: Abort (Resource missing).
- If `code == 401`: Refresh token and retry (Auth expired).
You need to catch `ServiceError`, inspect `e.args[0]` (the code), and decide what to do.
**Goals**:
- Implement `route_request(service_func)`.
- Catch `ServiceError`.
- Inspect the error code.
- Return action strings: "Retry", "Abort", "Refresh".

## Use Case: Dynamic Routing
The "TeleHealth" router decides if a failed video call connects should be retried or if the user simply hung up, based on complex vendor error codes.

## Lab Structure
1.  **Custom Exception**: `ServiceError`.
2.  **Broker Logic**: The smarter `try-except`.
3.  **Decision Tree**: Mapping codes to actions.

## Getting Started
Exceptions are just objects. You can access `e.args`, `e.message`, or any custom attributes attached to them.
