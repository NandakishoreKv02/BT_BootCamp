# Lab 4: Encapsulated Triage Logic - Tasks

## Task 1: Function Setup
Define `get_triage_category(systolic_bp)`.

## Task 2: Guard Clauses (Early Returns)
Order your logic from highest priority to lowest:
1. If `systolic_bp > 180`, return `"CRITICAL"`.
2. If `systolic_bp > 140`, return `"URGENT"`.
3. If `systolic_bp > 120`, return `"ELEVATED"`.

## Task 3: Default Return
At the very end of the function (outside any `if` block), return `"NORMAL"`.

## Task 4: Local Scope
Define a local variable `limit = 180` inside the function and use it for the first check. Verify that you cannot access `limit` in the `if __name__ == "__main__":` block.
