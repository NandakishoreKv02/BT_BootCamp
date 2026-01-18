---
title: "Medication Inventory Manager"
type: app_lab
module: language_fundamentals
unit: unit_1_12_hands_on_labs
lab_number: 2
difficulty: easy
use_case: pharmacy_management
domain: healthcare
order: 2
duration_hours: 2
tags:
  topics: ["lists", "dictionaries", "loops", "functions"]
  subtopics: ["inventory-management", "data-structures"]
---

# Lab 2: Medication Inventory Manager

**Module**: Language Fundamentals  
**Objective**: Build a medication inventory system that manages stock levels, tracks medications, and generates reports.  
**Difficulty**: Easy  
**Context**: Healthcare - Pharmacy Operations

## Generic Information
**Problem Statement**: Create a program that maintains a medication inventory, allows adding/removing stock, and generates low-stock alerts.

## Use Case
**Title**: Pharmacy Stock Management  
**Description**: Manage medication inventory with CRUD operations and reporting.

### Requirements
1. Store medications as dictionaries with: name, quantity, reorder_level
2. Add new medications to inventory
3. Update stock quantities (dispense/restock)
4. Generate low-stock report (quantity < reorder_level)
5. Display formatted inventory list

### Functions to Implement
- `create_medication(name, quantity, reorder_level)`: Create medication dict
- `add_to_inventory(inventory, medication)`: Add medication to list
- `find_medication(inventory, name)`: Search by name, return index or -1
- `update_stock(inventory, name, change)`: Modify quantity
- `get_low_stock_items(inventory)`: Return list of medications needing reorder
- `display_inventory(inventory)`: Print formatted table

## Expected Output Example
```
=== MEDICATION INVENTORY ===
Name                 Quantity    Reorder Level
------------------------------------------------
Aspirin              150         50
Ibuprofen            25          30    [LOW STOCK]
Amoxicillin          200         100

Low Stock Alert: 1 medication(s) need reordering
```
