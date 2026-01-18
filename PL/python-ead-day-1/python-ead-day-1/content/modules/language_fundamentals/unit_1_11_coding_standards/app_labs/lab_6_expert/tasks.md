# Lab 6: The Pythonic Auditor - Tasks

## Task 1: Module Constants
Define `FORBIDDEN_USERNAMES = ["admin", "root", "guest", "superuser"]`.

## Task 2: Pythonic Logic
In `audit_logins(login_list)`, iterate through the `login_list`. For each name, use the `in` operator to check against `FORBIDDEN_USERNAMES`.

## Task 3: Collection and Return
Append flagged names to a list called `flagged_accounts` and return it.

## Task 4: Professional Formatting
- Add a Module Docstring.
- Add Function Docstrings.
- Ensure all spacing follows PEP 8.
- Use `if __name__ == "__main__":` to print a success message if no accounts are flagged in a clean list.
