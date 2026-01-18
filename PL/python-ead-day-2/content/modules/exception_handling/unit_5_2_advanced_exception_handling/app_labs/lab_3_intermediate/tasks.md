# Lab 3 Tasks

## Task 1: Define Exceptions
- Define `ConnectionTimeout` (low level).
- Define `ServiceUnavailable` (high level).

## Task 2: The Connector
- Implement `connect_to_service()`.
- Use `try` to simulate a connection (raise `ConnectionTimeout`).

## Task 3: The Chain
- In `except ConnectionTimeout as e`:
- Raise `ServiceUnavailable("Service is down")` FROM `e`.
