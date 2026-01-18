# Exercises: Python Environment Setup

### Exercise 1: Python Installation Verification
1. Open your terminal/command prompt.
2. Run `python --version` and note the output. 
3. Run `pip --version` and note the output.
4. **Questions**:
   - What version of Python is installed on your system?
      Python 3.12.10
   - Is it Python 3.10 or higher? If not, upgrade to the latest version.
      Its higher
   - What is the path to your pip installation?
      pip 25.0.1 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0\Lib\site-packages\pip (python 3.12)
---

### Exercise 2: REPL Exploration ''' Read–Eval–Print Loop.'''
1. Launch the Python REPL by typing `python` in your terminal.
2. Execute the following commands and observe the output:
   ```python
   >>> import this
   >>> 5 + 3
   >>> name = "Patient Portal"
   >>> print(f"Welcome to {name}")
   >>> help(print)
   >>> exit()
   ```
3. **Questions**:
   - What does `import this` display?
      It displays The Zen of Python – a set of guiding principles emphasizing readability, simplicity, and clarity.
   - How do you exit the REPL on your operating system?
      exit()
      Ctrl + Z (Windows) + Enter
      Ctrl + D (Linux/macOS)
   - What information does `help(print)` provide?
      Description of the print() function
      Parameters like sep, end, file, flush
      Usage examples
---

### Exercise 3: Creating Your First Virtual Environment
1. Create a new directory called `healthcare_project`.
2. Navigate into this directory.
3. Create a virtual environment named `venv` using `python -m venv venv`.
4. Activate the virtual environment.
5. Verify activation by running `which python` (macOS/Linux) or `where python` (Windows).
6. **Questions**:
   - What command did you use to activate the virtual environment on your OS?
      Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
      .\venv\Scripts\activate
   - How can you tell if a virtual environment is active?
      The environment name appears at the beginning of your terminal prompt.
   - What happens to your command prompt when the environment is activated?
      The (venv) prefix confirms that the environment is active.
---

### Exercise 4: Package Management with pip
With your virtual environment activated from Exercise 3:
1. Install the `requests` package: `pip install requests`
2. Verify installation: `pip list`
3. Create a `requirements.txt` file: `pip freeze > requirements.txt`
4. Open and examine the `requirements.txt` file.
5. Deactivate the virtual environment.
6. Create a NEW virtual environment called `venv2`.
7. Activate `venv2` and install packages from requirements.txt: `pip install -r requirements.txt`

**Questions**:
- What packages are listed in `requirements.txt`?
- Why are there more packages than just `requests`?
- What's the difference between `pip install` and `pip freeze`?

'''Ans:
requests

Its dependencies:

urllib3

certifi

charset-normalizer

idna

2.Requests depends on other libraries to work
3.Command	Purpose
pip install requests	Installs a package
pip freeze	Lists installed packages

---

### Exercise 5: Running Python Scripts
1. Create a file named `patient_greeting.py` with the following content:
   ```python
   def greet_patient(patient_name, doctor_name):
       return f"Hello {patient_name}, Dr. {doctor_name} will see you shortly."

   if __name__ == "__main__":
       message = greet_patient("John Doe", "Smith")
       print(message)
   ```
2. Run the script from the command line: `python patient_greeting.py`
3. Modify the script to accept command-line arguments (research `sys.argv`).

**Questions**:
- What does `if __name__ == "__main__":` do?
   “Run this code only if this file is executed directly, not when imported.”
- How would you run this script from a different directory?
   python C:\PythonProjects\healthcare_project\patient_greeting.py

- What happens if you try to import this file as a module?
   Function is imported
   Code inside if __name__ == "__main__": ❌ does NOT run
   ✔️ This allows reuse without side effects
---

### Exercise 6: IDE/Editor Configuration
Choose ONE of the following and complete the setup:

#### Option A: Visual Studio Code
1. Download and install VS Code from code.visualstudio.com
2. Install the "Python" extension by Microsoft
3. Open your `healthcare_project` folder in VS Code
4. Configure VS Code to use your virtual environment:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your `venv` folder
5. Create a new file `test.py` and write a simple print statement
6. Run it using the play button or `F5`

#### Option B: PyCharm Community Edition
1. Download and install PyCharm Community from jetbrains.com
2. Open your `healthcare_project` as a new project
3. Configure the Python interpreter to use your virtual environment
4. Create a new Python file and run it

**Questions**:
- What features does your chosen IDE provide that the REPL doesn't?
IDE Feature	Benefit
Syntax highlighting	Easy to read
Auto-complete	Faster coding
Debugger	Step-by-step execution
Breakpoints	Pause code
Integrated terminal	No context switching

- How do you run a Python file from within the IDE?
   Click ▶️ Run
   OR press F5
   OR right-click → Run Python File
- Can you set breakpoints and debug code? Try it!
   YES
---

### Exercise 7: Environment Troubleshooting
Intentionally create and fix these common issues:

1. **Issue 1**: Install a package WITHOUT activating the virtual environment. Then activate and try to import it. What happens?
   ModuleNotFoundError

2. **Issue 2**: Create a file named `requests.py` in your project directory, then try to `import requests`. What error do you get? Why?
   AttributeError or ImportError
   Why?
   Python imports local file first, not pip package.

3. **Issue 3**: Try to run a script from the wrong directory. How do you fix the path issue?

**Document your findings**: Write a short paragraph explaining each issue and how you resolved it.

Issue 1 occurred because the package was installed globally instead of inside the virtual environment, causing import errors. Activating the virtual environment before installation resolved the issue.

Issue 2 happened due to filename shadowing, where a local file had the same name as an installed package. Renaming the file fixed the import conflict.

Issue 3 was caused by running the script from the wrong directory. Navigating to the correct directory or using an absolute path resolved the problem.
---

### Exercise 8: Cross-Platform Compatibility
Research and document:
1. How do you activate a virtual environment on:
   - Windows (Command Prompt)
   - Windows (PowerShell)
   - macOS/Linux (Bash/Zsh)

   Windows (CMD)
   venv\Scripts\activate

   Windows (PowerShell)
   venv\Scripts\Activate.ps1

   macOS / Linux
   source venv/bin/activate

2. What are the differences in path separators between Windows and Unix-like systems?

OS	Separator
Windows	\
Linux/macOS	/

3. How would you write a script that works on all platforms?

import os
os.path.join("folder", "file.txt")

---

### Bonus Challenge: Automated Setup Script
Create a script called `setup_project.sh` (or `setup_project.bat` for Windows) that:
1. Creates a virtual environment
2. Activates it
3. Installs packages from `requirements.txt`
4. Prints a success message

python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo Project setup completed successfully!


This is a common practice in professional projects to streamline onboarding.
