# Python Development Training Program - Day 2

Welcome to Day 2 of the Python Development Training Program! Today's focus is on **Module 5: Exception Handling**, where you will learn how to build robust, fault-tolerant applications by mastering Python's error management mechanisms.

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [How to Use This Repository](#how-to-use-this-repository)
- [Learning Path (Day 2)](#learning-path-day-2)
- [Support](#support)

---

## 🚀 Getting Started

### Prerequisites
- **Git** installed on your machine
- **Python** (v3.8 or higher) installed
- A code editor (VS Code recommended)

### Step 1: Clone the Repository (If not already done)

```bash
git clone https://github.com/SA-BTD-Dec-2026/python-ead.git
cd python-ead
```

### Step 2: Checkout the Day-2 Branch

```bash
git checkout day-2
```

---

## 📁 Repository Structure

```
python-ead/
├── content/                    # All learning materials
│   └── modules/               # Course modules
│       └── exception_handling/ # Module 5: Exception Handling
│           ├── unit_5_1_exception_basics/
│           ├── unit_5_2_advanced_exception_handling/
│           ├── unit_5_3_custom_exceptions/
│           └── unit_5_4_best_practices/
└── README.md                  # This file
```

### Inside Each Unit

Each unit is organized into three types of learning materials:

```
unit_5_x_topic_name/
├── knowledge/              # 📚 Theory and Concepts
│   └── lessons/           # Detailed markdown lessons
├── exercises/             # ✏️ Practice Exercises
│   └── *.py              # Quick coding practice with test runners
└── app_labs/              # 🔬 Hands-on Labs (Healthcare Context)
    ├── lab_1_easy/
    ├── lab_2_easy/
    ├── lab_3_intermediate/
    ├── lab_4_intermediate/
    ├── lab_5_advanced/
    └── lab_6_expert/
```

---

## 📖 How to Use This Repository

### 1. **📚 Knowledge (Theory Lessons)**
**Location**: `content/modules/exception_handling/{unit_name}/knowledge/`
Read the lessons thoroughly before starting exercises. All examples are tailored for healthcare scenarios (e.g., patient data processing).

### 2. **✏️ Exercises (Quick Practice)**
**Location**: `content/modules/exception_handling/{unit_name}/exercises/`
Open the `.py` file and implement the functions. Run the file directly to check your progress:
```bash
python unit_5_1_exception_basics_exercises.py
```

### 3. **🔬 App Labs (Hands-on Projects)**
**Location**: `content/modules/exception_handling/{unit_name}/app_labs/`
Each lab folder contains:
- `README.md`: Problem statement and healthcare context.
- `tasks.md`: Checklist of implementation steps.
- `starter_code.py`: Your workspace.
- `tests.py`: Automated tests. Run with `python tests.py`.

---

## 🎯 Learning Path (Day 2)

Today you will progress through [Module 5: Exception Handling]:

1. **Unit 5.1: Exception Basics**
   - Understanding exceptions and errors
   - Common built-in exceptions
   - The try-except block
   - Catching multiple exceptions
   - Exception hierarchy
   - The else clause
2. **Unit 5.2: Advanced Exception Handling**
   - The finally clause
   - Nested try-except blocks
   - Catching exception objects
   - Re-raising exceptions
   - Exception chaining
   - Context managers for cleanup
3. **Unit 5.3: Custom Exceptions**
   - Creating custom exception classes
   - When to create custom exceptions
   - Exception naming conventions
   - Adding attributes to exceptions
   - Organizing exception hierarchies
4. **Unit 5.4: Best Practices**
   - EAFP vs LBYL programming
   - Specific vs general exception handling
   - Logging exceptions
   - Error messages for users
   - Defensive programming techniques
   - Performance considerations

---

## 🆘 Support

If you encounter any issues:
- Review the **Knowledge** materials in the unit folder.
- Check the **README.md** in the specific lab folder.
- Reach out to your instructor or teaching assistant.
- Collaborate with your fellow trainees!

---

**Robust code starts with safe errors. Happy Coding! 🎓**