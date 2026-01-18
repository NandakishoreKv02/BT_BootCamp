# Lab 2 Tasks

## Task 1: SecurityError
- Define `SecurityError(Exception)`.
- `__init__(self, user, resource)`.
- Create a message: `f"User {user} denied access to {resource}"`.
- Call `super().__init__(message)`.
- Store `self.user` and `self.resource`.

## Task 2: Check Access
- Implement `access_resource(user, resource)`.
- If `user == "guest"`, raise `SecurityError`.

## Task 3: Test Attributes
- Catch the error and verify `e.user == "guest"`.
