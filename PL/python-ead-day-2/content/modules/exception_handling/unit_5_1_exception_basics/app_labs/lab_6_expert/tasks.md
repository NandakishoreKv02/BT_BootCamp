# Lab 6 Tasks

## Task 1: The Loader
- Implement `load_config(file_path)`.
- Default config: `{"mode": "safe", "retries": 3}`.

## Task 2: File Handling
- Try to `open()` the file.
- `except FileNotFoundError`: Return default config, print "Config missing, using defaults".
- `except PermissionError`: Return default config, print "Permission denied".

## Task 3: JSON Parsing
- Try `json.load()`.
- `except json.JSONDecodeError`: Return default config, print "Config corrupted".

## Task 4: Success
- If file exists and is valid JSON, return the loaded dict.
