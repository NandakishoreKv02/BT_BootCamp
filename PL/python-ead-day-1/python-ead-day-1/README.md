# Python  Development Training Program

Welcome to the Python  Development Training Program! This repository contains all the learning materials, exercises, and labs you'll need throughout the course.

## 📋 Table of Contents
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [How to Use This Repository](#how-to-use-this-repository)
- [Learning Path](#learning-path)
- [Support](#support)

---

## 🚀 Getting Started

### Prerequisites
- **Git** installed on your machine
- **Node.js** (v14 or higher) and **npm** installed
- **Python** (v3.8 or higher) installed
- A code editor (VS Code recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/SA-BTD-Dec-2026/python-ead.git
cd python-ead
```

### Step 2: Checkout the Day-1 Branch

```bash
git checkout day-1
```

### Step 3: Install Dependencies

Navigate to the web application directory and install Node modules:

```bash
cd web-app
npm install
```

### Step 4: Run the Development Server

```bash
npm run dev
```

The application should now be running! Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:3000` or similar).

---

## 📁 Repository Structure

```
python-ead/
├── web-app/                    # Web application for viewing course content
│   ├── package.json
│   └── ...
├── content/                    # All learning materials
│   └── modules/               # Course modules
│       ├── language_fundamentals/
│       ├── oop/
│       └── thinking_in_objects/
└── README.md                  # This file
```

### Inside Each Module

Each module is organized into **units**, and each unit contains three types of learning materials:

```
module_name/
├── unit_x_topic_name/
│   ├── knowledge/              # 📚 Theory and Concepts
│   │   └── lessons/           # Markdown files with detailed explanations
│   ├── exercises/             # ✏️ Practice Exercises
│   │   └── *.py              # Simple coding exercises
│   └── app_labs/              # 🔬 Hands-on Labs
│       ├── lab_1_easy/
│       ├── lab_2_easy/
│       ├── lab_3_intermediate/
│       ├── lab_4_intermediate/
│       ├── lab_5_advanced/
│       └── lab_6_expert/
```

---

## 📖 How to Use This Repository

Each unit contains three types of learning materials. Here's what you'll find and how to use them:

---

### 1. **📚 Knowledge (Theory Lessons)**

**Location**: `content/modules/{module_name}/{unit_name}/knowledge/`

#### What You'll Find:
- **`lesson_XX.md`**: A comprehensive markdown file containing:
  - **What**: Core concept definitions
  - **Example**: Practical code examples
  - **Explanation**: Deep dive into how it works
  - **Why**: Rationale and use cases
  - **Advantages & Disadvantages**: Trade-offs to consider
  - **Real-World Use Cases**: Healthcare-specific applications
  - **Best Practices**: Industry-standard coding patterns
  - **Top 3 Mistakes**: Common pitfalls and how to avoid them

#### How to Use:
1. **Read thoroughly** before attempting exercises or labs
2. **Run the code examples** in your own Python environment to see them in action
3. **Take notes** on key concepts and best practices
4. **Refer back** when you get stuck on exercises or labs

#### Example:
```
knowledge/
└── lesson_05.md  # "Operators & Expressions: The Engine of Logic"
```

---

### 2. **✏️ Exercises (Quick Practice)**

**Location**: `content/modules/{module_name}/{unit_name}/exercises/`

#### What You'll Find:
- **`README.md`**: Overview and instructions for all exercises
- **`unit_X_X_topic_name_exercises.py`**: Python file with 6 exercise functions

#### Structure of Exercise File:
Each exercise file contains:
- **Multiple functions** (typically 6) covering different aspects of the unit
- **Built-in test runner** at the bottom of the file
- **Solutions already implemented** (for reference and self-checking)

#### How to Use:
1. Open the `README.md` to see the list of exercises
2. Open the `.py` file
3. **Try to solve each function yourself first** (you can comment out the solution)
4. Run the file to test your solutions:
   ```bash
   python unit_1_5_operators_and_expressions_exercises.py
   ```
5. Compare your approach with the provided solution
6. Aim for **100% tests passed** before moving to labs

#### Example:
```
exercises/
├── README.md
└── unit_1_5_operators_and_expressions_exercises.py
```

**Sample Output**:
```
Running Unit 1.5 Exercise Solutions...
Result: 6/6 tests passed.
```

---

### 3. **🔬 App Labs (Hands-on Projects)**

**Location**: `content/modules/{module_name}/{unit_name}/app_labs/`

#### Difficulty Levels:
- **lab_1_easy** & **lab_2_easy**: Beginner-friendly, single-concept tasks
- **lab_3_intermediate** & **lab_4_intermediate**: Multi-step problems
- **lab_5_advanced**: Complex logic with edge cases
- **lab_6_expert**: Real-world scenarios with multiple requirements

#### What You'll Find in Each Lab:
Every lab folder contains these **4 important files**:

| File | Purpose | What Trainees Do |
|------|---------|------------------|
| **`README.md`** | Complete lab description with problem statement, use case, rules, and context | **Read first** to understand requirements |
| **`tasks.md`** | Step-by-step breakdown of what needs to be implemented | **Use as a checklist** while coding |
| **`starter_code.py`** | Template with function signatures and TODO comments | **Write your solution here** |
| **`tests.py`** | Automated unit tests using Python's `unittest` framework | **Run to verify** your solution |

#### Lab Workflow (Step-by-Step):

```
┌─────────────────────────────────────────────────────────┐
│  Step 1: Read README.md                                 │
│  → Understand the problem, use case, and rules          │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 2: Review tasks.md                                │
│  → See the breakdown of tasks (Task 1, Task 2, etc.)    │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 3: Open starter_code.py                           │
│  → Implement your logic where you see # TODO comments   │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 4: Run tests.py                                   │
│  → Command: python tests.py                             │
│  → The tests import your functions from starter_code.py │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 5: Debug & Iterate                                │
│  → Fix errors, refine logic, re-run tests               │
│  → Goal: All tests pass (e.g., "OK" or "3/3 passed")    │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 6: Move to Next Lab                               │
│  → Only proceed when all tests pass ✅                  │
└─────────────────────────────────────────────────────────┘
```

#### Example Lab Structure:
```
lab_1_easy/
├── README.md           # "Pediatric Dosage Calculator" - Full description
├── tasks.md            # Task 1: Basic Multiplication, Task 2: Safety Check, etc.
├── starter_code.py     # Your workspace - implement calculate_mg_dose()
└── tests.py            # Automated tests - run with: python tests.py
```

#### How to Run Tests:
```bash
# Navigate to the lab folder
cd content/modules/language_fundamentals/unit_1_5_operators_and_expressions/app_labs/lab_1_easy

# Run the tests
python tests.py
```

#### Expected Test Output:
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

#### Important Notes for Labs:
- ✅ **DO**: Write all your code in `starter_code.py`
- ✅ **DO**: Run `tests.py` frequently to check your progress
- ✅ **DO**: Read error messages carefully - they tell you what's wrong
- ❌ **DON'T**: Modify `tests.py` (unless instructed)
- ❌ **DON'T**: Skip labs - they build on each other
- ❌ **DON'T**: Move forward until all tests pass

---

## 🎯 Learning Path

### Recommended Workflow for Each Unit:

1. **Read Knowledge** → Start with the theory lessons in the `knowledge/` folder
2. **Complete Exercises** → Practice with simple exercises in the `exercises/` folder
3. **Tackle Labs** → Work through labs from easy to expert in the `app_labs/` folder
4. **Review & Reflect** → Go back to knowledge materials if you get stuck

### Available Modules:

1. **Language Fundamentals** - Python basics, syntax, and core concepts
2. **OOP (Object-Oriented Programming)** - Classes, objects, inheritance, and design patterns
3. **Thinking in Objects** - Advanced OOP concepts and real-world applications

---

## 🆘 Support

If you encounter any issues:
- Review the knowledge materials for the relevant unit
- Check the lab README files for specific instructions
- Reach out to your instructor or teaching assistant
- Collaborate with your fellow trainees

---

## 📝 Notes

- All code examples use **healthcare domain** contexts to make learning relevant and practical
- Labs are designed to build on each other - complete them in order
- Don't skip the exercises - they're essential for building muscle memory
- Take your time with expert-level labs - they're meant to challenge you!

---

**Happy Learning! 🎓**