# Lab 6 Tasks

## Task 1: The Exception
- Define `class ServiceError(Exception): pass`.

## Task 2: The Broker
- Implement `route_request(func)`.
- Try calling `func()`. If success, return "Success".

## Task 3: Inspection
- Catch `ServiceError` as `e`.
- Access `code = e.args[0]`.
- If 503 -> return "Retry".
- If 404 -> return "Abort".
- If 401 -> return "Refresh".
- Else -> return "Unknown".
