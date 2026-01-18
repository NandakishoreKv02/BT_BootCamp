# Unit 1.11: Coding Standards - Exercises

## Overview
These exercises focus on the "professionalism" of your code. You will refactor poorly written snippets into clean, PEP 8-compliant, and Pythonic code suitable for a healthcare engineering team.

## Instructions
1. Open `unit_1_11_coding_standards_exercises.py`.
2. Perform the refactoring requested in each "TODO".
3. Run the file to verify your work:
   ```bash
   python unit_1_11_coding_standards_exercises.py
   ```

## Exercise List

### 1. Variables (snake_case)
Change single-letter or non-standard names into descriptive, lowercase underscores.

### 2. Functions (Verbs + snake_case)
Refactor function names to correctly describe their action using standard casing.

### 3. Constants (Screaming Snake)
Eliminate "Magic Numbers" by defining named constants at the top level.

### 4. Classes (PascalCase)
Ensure object Blueprints follow the capitalized noun convention.

### 5. Pythonic Power
Replace traditional C-style logic (like manual loops for searching) with built-in Python idioms like `in`.

### 6. Script Hygiene
Prevent code from executing automatically during an import by using the `if __name__ == "__main__":` block.
