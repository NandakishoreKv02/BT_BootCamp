# Lab 6 Tasks

## Task 1: Complex Signature
- Define `DataHarvester`.
- Implement `log_event(self, event_type, severity=1, *args, **kwargs)`.

## Task 2: Data Bundling
- Inside the method:
  - Capture all values into a single response dictionary.
  - Return the dictionary.

## Task 3: Reporting
- Implement a helper method to take the response dictionary and print it in a human-readable "Table" format.

## Task 4: Integration
In `main()`:
1. Create a harvester.
2. Call `log_event` with only the mandatory type.
3. Call `log_event` with all argument types mixed (Type, Severity, 3 Vitals, and 2 Metadata Keywords).
4. Print both results.
