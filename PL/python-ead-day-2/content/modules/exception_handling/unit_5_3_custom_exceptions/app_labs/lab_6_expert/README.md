---
title: "Health Network Orchestrator - Organizing Hierarchies"
type: app_lab
module: exception_handling
unit: unit_5_3_custom_exceptions
lab_number: 6
difficulty: expert
use_case: complex_orchestration
domain: healthcare
order: 6
duration_hours: 3.0
tags:
  topics: ["exceptions", "hierarchies", "orchestration"]
  subtopics:
    - layered-architecture
    - multi-tier-errors
    - system-integration
---

# Lab 6: Health Network Orchestrator - Organizing Hierarchies

**Objective**: Design and implement a multi-tiered exception hierarchy for a health network platform, ensuring that errors from different sub-systems (Data, Network, Auth) are properly categorized and handled.

## Generic Information
**Problem Statement**: In a distributed health network, an error could come from the database, the network, or the authentication service. Catching purely specific errors results in huge, repetitive code blocks. By organizing these under a single `NetworkPlatformError`, and then further into `DataStackError` and `ConnectivityError`, you can manage complexity effectively.
**Goals**:
- Design a 3-layer hierarchy.
- Implement an orchestrator that initiates multiple service calls.
- Use the hierarchy to handle "System level" vs "Application level" failures.

## Use Case: Complex Orchestration
The "IntegratedCare" platform syncs data between a local clinic and a regional hospital. It must handle various failure points gracefully, ensuring that data is never lost or corrupted.

## Lab Structure
1.  **Hierarchy Design**: Defining the 3 levels of exceptions.
2.  **Service Stubs**: Simulating different points of failure.
3.  **Orchestrator**: Managing call sequences and multi-level catching.

## Getting Started
Follow the pattern: `Base` -> `Sub-System Base` -> `Specific Error`.
Example: `AppError` -> `NetworkError` -> `TimeoutError`.
