# Unit 1.3: Python Program Structure - Learning Outcomes

## Overview
In this unit, you will learn the fundamental structure and organization of Python programs. You'll understand how Python uses indentation to define code blocks, how to document your code effectively with comments and docstrings, and the critical distinction between modules and scripts. This knowledge is essential for writing clean, maintainable, and professional Python code.

**Estimated Time**: 8-10 hours
- Knowledge: 90 min
- Exercises: 3 hours
- App Labs: 4-6 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Python Script Structure
- [ ] **Organize** a Python script with proper structure (imports, constants, functions, main execution).
- [ ] **Apply** the standard Python file structure conventions used in professional projects.
- [ ] **Identify** the components of a well-structured Python program.

### Indentation & Code Blocks
- [ ] **Utilize** consistent indentation (4 spaces) to define code blocks in Python.
- [ ] **Explain** why Python uses indentation instead of braces or keywords.
- [ ] **Debug** indentation errors (`IndentationError`, `TabError`).
- [ ] **Configure** your editor to use spaces instead of tabs.

### Comments & Docstrings
- [ ] **Write** single-line and multi-line comments to explain complex logic.
- [ ] **Create** docstrings for modules, classes, and functions following PEP 257 conventions.
- [ ] **Distinguish** between comments (for developers) and docstrings (for users/documentation).
- [ ] **Generate** documentation from docstrings using tools like `help()`.

### `__main__` and Script Execution
- [ ] **Implement** the `if __name__ == "__main__":` pattern to make scripts importable.
- [ ] **Explain** the purpose and behavior of the `__name__` variable.
- [ ] **Design** scripts that can be both run directly and imported as modules.
- [ ] **Understand** the execution flow when a Python file is run vs imported.

### Python Modules vs Scripts
- [ ] **Differentiate** between a Python module (importable) and a script (executable).
- [ ] **Create** reusable modules that can be imported by other programs.
- [ ] **Organize** code into logical modules for better maintainability.
- [ ] **Apply** best practices for module design in healthcare applications.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct use of indentation with no mixing of tabs and spaces.
- Proper docstrings for all functions following PEP 257.
- Successful implementation of `__main__` guard in scripts.
- Ability to create both importable modules and executable scripts.

### App Labs (Pass: 80% or higher)
- **Structure**: Code follows professional organization patterns.
- **Documentation**: All functions have clear, informative docstrings.
- **Reusability**: Scripts can be both run and imported without side effects.
- **Style**: Consistent indentation and adherence to PEP 8.

---

## Next Steps
1. **Unit 1.4: Variables & Data Types** will introduce Python's type system and how to work with different data types.
2. **Unit 1.5: Operators & Expressions** will teach you how to perform operations and build complex expressions.

---

## Common Pitfalls to Avoid
✅ **Do**: Use 4 spaces for indentation (PEP 8 standard).

❌ **Don't**: Mix tabs and spaces—this causes `TabError` and inconsistent behavior.

✅ **Do**: Write docstrings for all public functions, classes, and modules.

❌ **Don't**: Use comments to explain obvious code—write self-explanatory code instead.

✅ **Do**: Use the `if __name__ == "__main__":` guard for all executable scripts.

❌ **Don't**: Put executable code at the module level without the main guard—it runs on import.

✅ **Do**: Keep modules focused on a single responsibility.

❌ **Don't**: Create "god modules" that try to do everything.

✅ **Do**: Use triple-quoted strings (`"""..."""`) for docstrings, not regular comments.

❌ **Don't**: Forget to document complex algorithms or non-obvious design decisions.
