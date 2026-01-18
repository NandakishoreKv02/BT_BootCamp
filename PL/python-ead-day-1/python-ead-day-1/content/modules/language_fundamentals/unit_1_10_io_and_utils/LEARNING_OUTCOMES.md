# Unit 1.10: Input, Output & Basic Utilities - Learning Outcomes

## Overview
A program that can't interact with the world is a closed box. This unit focuses on making your Python applications interactive and persistent. You will learn to collect data from users, format professional clinical reports, and save data to files so it isn't lost when the program ends.

**Estimated Time**: 14-16 hours
- Knowledge: 2 hours
- Exercises: 4-6 hours
- App Labs: 8 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### User Interaction
- [ ] **Collect** user data using the `input()` function and understand the necessity of type casting (e.g., `int(input())`).
- [ ] **Implement** interactive command-line loops for clinical data entry.

### Advanced Output Formatting
- [ ] **Master** f-strings for complex output (alignment, padding, and decimal precision).
- [ ] **Utilize** `print()` arguments like `sep` and `end` for custom formatting.

### File Operations (Basic)
- [ ] **Open** and **Close** text files safely using the `with` statement (context managers).
- [ ] **Write** clinical logs and patient notes to external `.txt` files.
- [ ] **Read** data from files to load patient history or reference ranges.

### Command-line Awareness
- [ ] **Identify** the purpose of command-line arguments and how they differ from interactive input.
- [ ] **Implement** basic usage of `sys.argv` for simple script configuration.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct numeric conversion of interactive user input.
- Successful generation of a multi-line formatted report using f-strings with padding.
- Error-free writing and reading of a string to/from a local file.

### App Labs (Pass: 80% or higher)
- **Interactivity**: Building a triage script that asks questions and processes answers in real-time.
- **Persistence**: Ensuring patient encounter notes are saved to a unique file.
- **Report Quality**: Producing a "Shift Summary" report that is readable, aligned, and professional.
- **Safety**: Using `try/except` alongside file operations to handle "File Not Found" errors.

---

## Next Steps
1. **Module 1 Final Capstone**: You will now combine all skills from Module 1 into a comprehensive Patient Management System.
2. **Module 2: Intermediate Python**: You will deep dive into libraries like `pandas` and `matplotlib` for advanced data processing.

---

## Common Pitfalls to Avoid
✅ **Do**: Use `with open(...)` to ensure files are closed even if an error occurs.

❌ **Don't**: Manually call `.close()` if you can use a context manager; it's easy to forget.

✅ **Do**: Remember that `input()` *always* returns a string.

❌ **Don't**: Try to do math on `input()` without converting it to a numeric type first.

✅ **Do**: Use f-strings (`f"..."`)—they are the modern standard for Python formatting.

❌ **Don't**: Use old-style `%` formatting or `.format()` unless you are working on very old legacy code.

✅ **Do**: Use relative paths for files within your project directory for better portability.

❌ **Don't**: Hardcode absolute paths (like `C:\Users\Name\...`) which will break on other computers.
