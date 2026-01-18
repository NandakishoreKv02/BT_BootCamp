# Unit 1.3: Python Program Structure - Exercises

## Overview
These exercises will help you master Python's program structure, including indentation, comments, docstrings, and the `__main__` guard pattern.

## Instructions
1. Open `unit_1_3_python_program_structure_exercises.py`
2. Complete each exercise by replacing the TODO comments with working code
3. Run the file to test your solutions: `python unit_1_3_python_program_structure_exercises.py`
4. Compare your solutions with `solutions/unit_1_3_python_program_structure_exercises.py`

## Exercise List

### Exercise 1: Fix Indentation Errors ⭐
**Difficulty**: Easy  
**Objective**: Fix indentation errors in a function that checks vital signs.

**Skills Practiced**:
- Proper indentation levels
- Nested if statements
- Debugging `IndentationError`

---

### Exercise 2: Add Proper Docstring ⭐
**Difficulty**: Easy  
**Objective**: Write a comprehensive docstring following PEP 257 conventions.

**Skills Practiced**:
- Docstring format
- Args and Returns sections
- Example usage

---

### Exercise 3: Implement `__main__` Guard ⭐⭐
**Difficulty**: Medium  
**Objective**: Add a `__main__` guard to make a script importable.

**Skills Practiced**:
- Understanding `__name__` variable
- Script vs module behavior
- Testing code in main block

---

### Exercise 4: Create a Reusable Module Function ⭐⭐
**Difficulty**: Medium  
**Objective**: Format patient IDs with leading zeros.

**Skills Practiced**:
- String formatting with f-strings
- Creating reusable functions
- Writing clear docstrings

---

### Exercise 5: Add Comments and Docstrings ⭐⭐
**Difficulty**: Medium  
**Objective**: Improve documentation for an age calculation function.

**Skills Practiced**:
- Inline comments for complex logic
- Comprehensive docstrings
- Distinguishing when to use comments vs docstrings

---

### Exercise 6: Nested Indentation ⭐⭐⭐
**Difficulty**: Hard  
**Objective**: Implement complex nested logic for vital signs assessment.

**Skills Practiced**:
- Multiple indentation levels
- Nested if-elif-else statements
- Logical flow control

---

### Exercise 7: Module Structure ⭐⭐⭐
**Difficulty**: Hard  
**Objective**: Reorganize messy code into proper module structure.

**Skills Practiced**:
- Module docstrings
- Import organization
- Constant definitions
- Function organization
- Main guard placement

---

### Exercise 8: Docstring Formats ⭐⭐⭐
**Difficulty**: Hard  
**Objective**: Write a comprehensive docstring for BMI calculation.

**Skills Practiced**:
- Complete docstring format
- Args with types
- Returns with type
- Raises section
- Example usage

---

### Exercise 9: Script vs Module ⭐⭐
**Difficulty**: Medium  
**Objective**: Make code behave differently when run vs imported.

**Skills Practiced**:
- `__main__` guard usage
- Script/module dual behavior
- Testing importable code

---

### Exercise 10: Complete Program Structure ⭐⭐⭐⭐
**Difficulty**: Expert  
**Objective**: Create a complete, professional patient registration system.

**Skills Practiced**:
- Full module structure
- Multiple functions with docstrings
- Constants and validation
- Main function pattern
- Professional code organization

---

## Running the Tests

```bash
# Run the starter file (will show failures)
python unit_1_3_python_program_structure_exercises.py

# Run the solutions (should all pass)
python solutions/unit_1_3_python_program_structure_exercises.py
```

## Tips for Success

1. **Indentation**: Always use 4 spaces, never tabs
2. **Docstrings**: Use triple quotes `"""..."""` for all docstrings
3. **Comments**: Use `#` for inline comments explaining complex logic
4. **Main Guard**: Always use `if __name__ == "__main__":` for executable code
5. **Testing**: Test your code both by running it and by importing it

## Common Errors and Solutions

### `IndentationError`
**Problem**: Mixed tabs and spaces or incorrect indentation level  
**Solution**: Configure your editor to use 4 spaces and check indentation carefully

### `TabError`
**Problem**: Mixing tabs and spaces  
**Solution**: Convert all tabs to spaces in your editor settings

### Code Runs on Import
**Problem**: Missing `__main__` guard  
**Solution**: Wrap executable code in `if __name__ == "__main__":`

### No Help Text
**Problem**: Missing or incorrect docstring  
**Solution**: Add triple-quoted docstring immediately after function definition

## Additional Resources

- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Real Python - Documenting Python Code](https://realpython.com/documenting-python-code/)
