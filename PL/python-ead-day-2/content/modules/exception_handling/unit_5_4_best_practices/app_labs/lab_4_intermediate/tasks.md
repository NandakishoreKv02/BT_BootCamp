# Lab 4 Tasks

## Task 1: The Failing Op
- View `download_report(filename)`.
- It raises `PermissionError(f"Locked file: {filename}")`.

## Task 2: Implement the Proxy
- Implement `secure_download_handler(filename, log_store)`.
- Try calling `download_report(filename)`.

## Task 3: Split the Output
- Catch `PermissionError`.
- Append the raw error message (with path) to `log_store`.
- Return a user-friendly string: `"Unable to access report. Please try again later."`.
