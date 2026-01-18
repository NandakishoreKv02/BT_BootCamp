# Lab 2 Tasks

## Task 1: Create the Logger "Constructor"
Define `make_logger(service_name)`:
- Returns a dictionary representing the Logger.
- Store the `service_name` (e.g., "Pharmacy", "ICU").
- Initialize an empty list called `log_history` to track events.

## Task 2: Implement Standardized Logging
Define `log_event(logger, message)`:
- Accept a logger dictionary and a message string.
- Format the output as: `"[SERVICE_NAME]: MESSAGE"`.
- Append the message to the `log_history` for that specific logger.
- Print the formatted string to the console.

## Task 3: Multi-Service Simulation
In the `main()` function:
1. Create `pharmacy_logger = make_logger("Pharmacy")`.
2. Create `admission_logger = make_logger("Admissions")`.
3. Log standard events (e.g., "Administered Aspirin", "Admitted John Doe") to both.
4. Verify that although they use the same function, they maintain separate identities and history.
