# Exercises: Introduction to Python

### Exercise 1: The Zen of Python
1.  Open your terminal or a Python REPL.
2.  Type `import this`.
3.  Read the aphorisms. Which principle do you think is most important for medical software development? Why?

"Explicit is better than implicit."
In healthcare systems, ambiguity can lead to serious errors (wrong diagnosis, wrong dosage, wrong patient data). Explicit code:
1. Is easier to review and audit
2. Reduces misunderstandings among developers and doctors
3. Improves patient safety
Clear and readable logic is critical when lives depend on the software.
---

### Exercise 2: Language Comparison
Research and compare Python with Java for a simple "Hello Patient" application.
1.  How many lines of code are required in Python? - 1 line
2.  How many lines are required in Java (including class and main method)? 5-6 lines
3.  Which one is easier for a non-programmer to read? -Python
    
    No boilerplate code
    Almost reads like plain English
    Faster to understand and maintain
---

### Exercise 3: Ecosystem Matchmaking
Match the following Python tools to their respective domains:
- **Tools**: Django, pandas, TensorFlow, FastAPI, NumPy, requests
- **Domains**: 
    - AI & Machine Learning -TensorFlow
    - Data Analysis -Pandas
    - Large Web Frameworks -Django
    - High-performance APIs -FastAPI
    - Mathematical Computing -Numpy
    - Web Scraping/API Interaction -requests

---

### Exercise 4: Version Check
1.  Run `python --version` in your terminal.
2.  What version are you running? 
    Python 3.12.10
3.  Is it Python 3? 
    Yes
4.  Why is it important to ensure you aren't using Python 2.x for modern healthcare applications?
    
    
    Python 2 is officially discontinued
    No security updates ❌
    Incompatible with modern libraries ❌
    Unsafe for handling sensitive medical data ❌
---

### Exercise 5: Indentation Logic
Observe the code below. Why will it fail?
```python
def check_temperature(temp):
print("Checking value...")
    if temp > 37.5:
        return "Fever"
    return "Normal"
```
*Hint: Look closely at the indentation of the print statement.*
Python uses indentation to define code blocks.
The print statement is not indented, so Python throws an IndentationError.