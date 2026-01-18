# Unit 1.2: Python Environment Setup - Learning Outcomes

## Overview
In this unit, you will learn how to properly install Python on your system, configure your development environment, and use essential tools that professional Python developers rely on daily. You'll understand the importance of virtual environments for project isolation and get familiar with popular IDEs and editors. This unit ensures you have a solid foundation for all future Python development work.

**Estimated Time**: 4-5 hours
- Knowledge: 90 min
- Exercises: 2.5-3.5 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Python Installation
- [ ] **Install** Python 3.10+ on Windows, macOS, or Linux using official installers or package managers.
- [ ] **Verify** Python installation by checking the version from the command line.
- [ ] **Configure** the system PATH to ensure Python is accessible from any terminal location.
- [ ] **Distinguish** between system Python and user-installed Python distributions.

### Python Interpreter & REPL
- [ ] **Launch** the Python REPL (Read-Eval-Print Loop) from the command line.
- [ ] **Execute** Python code interactively in the REPL for quick testing and experimentation.
- [ ] **Utilize** REPL features like history navigation, multi-line input, and the `help()` function.
- [ ] **Understand** when to use the REPL versus writing Python scripts.

### Virtual Environments
- [ ] **Explain** why virtual environments are critical for Python project isolation.
- [ ] **Create** a virtual environment using the `venv` module.
- [ ] **Activate** and **deactivate** virtual environments on different operating systems.
- [ ] **Install** packages within a virtual environment using `pip`.
- [ ] **Manage** project dependencies using `requirements.txt` files.
- [ ] **Recognize** the dangers of installing packages globally and how virtual environments prevent conflicts.

### Running Python Programs
- [ ] **Execute** Python scripts from the command line using `python script.py`.
- [ ] **Understand** the difference between running scripts and importing modules.
- [ ] **Use** command-line arguments in Python scripts.
- [ ] **Debug** common execution errors (file not found, syntax errors, import errors).

### IDEs and Editors
- [ ] **Configure** Visual Studio Code for Python development with essential extensions.
- [ ] **Navigate** PyCharm's interface and understand its key features for Python projects.
- [ ] **Compare** lightweight editors (VS Code, Sublime) with full IDEs (PyCharm, Spyder).
- [ ] **Utilize** IDE features like syntax highlighting, code completion, and integrated debugging.
- [ ] **Choose** the appropriate development tool based on project requirements and personal preference.

---

## Assessment Criteria

### Exercises (Pass: All tasks completed successfully)
- Successfully install Python and verify the installation.
- Create and activate a virtual environment, then install at least 3 packages.
- Write and execute a simple Python script from the command line.
- Configure at least one IDE/editor with Python support and run a "Hello, World!" program.

---

## Next Steps
1. **Unit 1.3: Python Program Structure** will teach you how to organize Python code into modules and packages.
2. **Unit 1.4: Variables & Data Types** will introduce Python's type system and how to work with different data types.

---

## Common Pitfalls to Avoid
✅ **Do**: Always use virtual environments for your projects to avoid dependency conflicts.

❌ **Don't**: Install packages globally using `sudo pip install` or admin privileges—this can break system tools.

✅ **Do**: Add your virtual environment folder (e.g., `venv/`) to `.gitignore` to avoid committing it to version control.

❌ **Don't**: Share virtual environments between projects or commit them to Git repositories.

✅ **Do**: Use `python -m pip` instead of just `pip` to ensure you're using the correct Python version's pip.

❌ **Don't**: Mix packages from different Python versions or virtual environments.

✅ **Do**: Keep your IDE/editor updated and learn keyboard shortcuts to improve productivity.

❌ **Don't**: Rely solely on the REPL for complex development—use proper scripts and version control.

✅ **Do**: Document your project dependencies in `requirements.txt` for reproducibility.

❌ **Don't**: Forget to activate your virtual environment before installing packages or running scripts.
