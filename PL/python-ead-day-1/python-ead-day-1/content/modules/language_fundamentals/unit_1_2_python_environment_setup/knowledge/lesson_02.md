---
title: "Python Environment Setup: Professional Development Configuration"
type: knowledge
module: language_fundamentals
unit: unit_1_2_python_environment_setup
order: 2
difficulty: beginner
tags:
  subtopics:
    - python-installation
    - repl
    - virtual-environments
    - ides-editors
    - development-workflow
---

# Unit 1.2: Python Environment Setup

## 1. What
Setting up a proper Python development environment is the foundation of professional software development. This involves:
- **Installing Python**: Getting the Python interpreter on your system.
- **REPL (Read-Eval-Print Loop)**: An interactive shell for testing code snippets.
- **Virtual Environments**: Isolated spaces for project dependencies.
- **IDEs/Editors**: Tools that make writing and debugging code efficient.

A properly configured environment prevents the infamous "works on my machine" problem and ensures your code is reproducible across different systems.

---

## 2. Example

### Installing Python (Windows)
```bash
# Download from python.org and run the installer
# IMPORTANT: Check "Add Python to PATH" during installation

# Verify installation
python --version
# Output: Python 3.11.5 (or your installed version)

# Check pip (Python's package installer)
pip --version
# Output: pip 23.2.1 from C:\Python311\lib\site-packages\pip (python 3.11)
```

### Using the REPL
```python
# Launch REPL by typing 'python' in terminal
>>> 2 + 2
4
>>> name = "Healthcare System"
>>> print(f"Welcome to {name}")
Welcome to Healthcare System
>>> exit()  # or Ctrl+D (Unix) / Ctrl+Z (Windows)
```

### Creating a Virtual Environment
```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Your prompt should now show (venv)
(venv) $ pip install requests
# Package installs ONLY in this virtual environment

# Deactivate when done
deactivate
```

### Running a Python Script
```python
# File: hello_patient.py
def greet_patient(name):
    return f"Hello, {name}! Welcome to our clinic."

if __name__ == "__main__":
    print(greet_patient("Dr. Smith"))
```

```bash
# Run the script
python hello_patient.py
# Output: Hello, Dr. Smith! Welcome to our clinic.
```

---

## 3. Explanation

### Why Virtual Environments?
Imagine you have two projects:
- **Project A** needs `Django 3.2`
- **Project B** needs `Django 4.1`

Without virtual environments, you can only have ONE version of Django installed globally. Virtual environments solve this by creating isolated Python installations for each project.

### How Virtual Environments Work
When you create a virtual environment:
1. Python copies itself into a new directory (e.g., `venv/`).
2. It creates a separate `site-packages` folder for this environment's libraries.
3. When activated, your shell uses THIS Python instead of the system Python.

### REPL vs Scripts
- **REPL**: Great for quick experiments, testing syntax, or exploring libraries.
- **Scripts**: For actual programs that need to be saved, versioned, and run repeatedly.

### IDE Features That Matter
- **Syntax Highlighting**: Colors code for readability.
- **IntelliSense/Autocomplete**: Suggests code as you type.
- **Debugging**: Step through code line-by-line to find bugs.
- **Integrated Terminal**: Run code without leaving the editor.

---

## 4. Why

### Why Proper Setup Matters in Healthcare
In healthcare software:
- **Reproducibility**: A bug in production must be reproducible in development. Virtual environments ensure everyone uses the same package versions.
- **Security**: Outdated packages have vulnerabilities. A clean environment makes it easier to audit and update dependencies.
- **Compliance**: HIPAA and FDA regulations require documented software environments. `requirements.txt` provides this documentation.

### Why Not Just Use Global Python?
- **Dependency Hell**: Different projects need different package versions.
- **System Breakage**: Installing packages globally can break OS tools that rely on Python.
- **Collaboration**: Your teammate's global environment is different from yours.

---

## 5. Advantages & Disadvantages

### Advantages
- **Isolation**: Each project has its own dependencies.
- **Reproducibility**: `requirements.txt` ensures everyone has the same setup.
- **Safety**: Mistakes in one project don't affect others.
- **Flexibility**: Test new packages without risking your main environment.

### Disadvantages
- **Disk Space**: Each virtual environment duplicates Python (typically 20-50 MB).
- **Activation Step**: You must remember to activate the environment before working.
- **Learning Curve**: Beginners often forget to activate or get confused about which Python is running.

---

## 6. Real-World Use Cases

### Case 1: Hospital EMR System
A hospital's Electronic Medical Records system uses:
- `Django 4.0` for the web framework
- `psycopg2` for PostgreSQL database
- `celery` for background tasks

The development team uses virtual environments to ensure all developers and the production server use identical package versions, preventing "it works on my machine" bugs.

### Case 2: Data Science Team
A healthcare analytics team has multiple projects:
- **Project 1**: Uses `pandas 1.5` and `scikit-learn 1.2`
- **Project 2**: Uses `pandas 2.0` and `tensorflow 2.12`

Virtual environments allow both projects to coexist on the same machine without conflicts.

### Case 3: Open Source Contribution
When contributing to an open-source medical imaging library, you create a virtual environment to match the project's exact dependencies, ensuring your changes work in the project's context.

---

## 7. Best Practices

### Best Practice 1: Always Use Virtual Environments
**When to apply**: For every Python project, no matter how small.
**Why**: Prevents dependency conflicts and makes projects portable.
```bash
# Start every project with:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Best Practice 2: Use `requirements.txt`
**When to apply**: As soon as you install your first package.
**Why**: Documents dependencies for teammates and deployment.
```bash
# Save current packages
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

### Best Practice 3: Add `venv/` to `.gitignore`
**When to apply**: Immediately when creating a Git repository.
**Why**: Virtual environments are large and machine-specific.
```bash
# .gitignore
venv/
__pycache__/
*.pyc
```

### Best Practice 4: Use Descriptive Environment Names
**When to apply**: When managing multiple environments.
**Why**: Clarity prevents activation mistakes.
```bash
# Instead of just 'venv', use:
python -m venv patient-portal-env
python -m venv analytics-dashboard-env
```

---

## 8. Top 3 Mistakes

### Mistake 1: Installing Packages Without Activating Virtual Environment
#### What's the Problem?
Running `pip install package` without activating your virtual environment installs the package globally.

#### Impact
- Pollutes global Python installation
- Package won't be available when you activate the virtual environment
- Can cause version conflicts

#### Correct Approach
```bash
# ALWAYS activate first
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# THEN install
pip install requests
```

### Mistake 2: Committing Virtual Environment to Git
#### What's the Problem?
Adding the `venv/` folder to version control.

#### Impact
- Massive repository size (100+ MB)
- Breaks on different operating systems (Windows venv won't work on Linux)
- Merge conflicts in binary files

#### Correct Approach
```bash
# Add to .gitignore
echo "venv/" >> .gitignore

# Use requirements.txt instead
pip freeze > requirements.txt
git add requirements.txt
```

### Mistake 3: Using System Python for Projects
#### What's the Problem?
Running `python` without creating a virtual environment first.

#### Impact
- Dependency conflicts between projects
- Risk of breaking system tools
- Difficult to reproduce environment on other machines

#### Correct Approach
```bash
# For EVERY new project:
mkdir my_healthcare_app
cd my_healthcare_app
python -m venv venv
source venv/bin/activate
pip install django
```
