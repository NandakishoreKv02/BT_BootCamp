# Python Development Training Program - Day 3

Welcome to Day 3 of the Python Development Training Program! Today, we dive deep into one of the most powerful features of Python: **Collections**.

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

### Step 2: Checkout the Day-3 Branch

```bash
git checkout day-3
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
│       └── collections/       # Day 3: Collections Deep Dive
│           ├── unit_1_lists/
│           ├── unit_2_tuples/
│           ├── unit_3_dictionaries/
│           ├── unit_4_sets/
│           └── unit_5_collection_selection/
└── README.md                  # This file
```

### Inside Each Unit

Each unit is organized into three types of learning materials:

```
unit_name/
├── knowledge/              # 📚 Theory and Concepts (lesson_XX.md)
├── exercises/             # ✏️ Practice Exercises (*.py)
└── app_labs/              # 🔬 Hands-on Labs (lab_1 to lab_6)
```

---

## 📖 How to Use This Repository

Each unit contains three types of learning materials. Here's what you'll find and how to use them:

---

### 1. **📚 Knowledge (Theory Lessons)**

**Location**: `content/modules/collections/{unit_name}/knowledge/`

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
2. **Run the code examples** in your own Python environment
3. **Take notes** on key concepts and best practices

#### Example:
```
knowledge/
└── lesson_01.md  # "Lists Fundamentals"
```

---

### 2. **✏️ Exercises (Quick Practice)**

**Location**: `content/modules/collections/{unit_name}/exercises/`

#### What You'll Find:
- **`README.md`**: Overview and instructions
- **`unit_X_topic_name_exercises.py`**: Python file with exercise functions and test runner

#### How to Use:
1. Open the `.py` file
2. **Implement your solution** in the empty functions
3. Run the file to test:
   ```bash
   python unit_1_lists_exercises.py
   ```
4. Aim for **100% tests passed** before moving to labs

---

### 3. **🔬 App Labs (Hands-on Projects)**

**Location**: `content/modules/collections/{unit_name}/app_labs/`

#### Difficulty Levels:
- **lab_1_easy** & **lab_2_easy**: Fundamental tasks
- **lab_3_intermediate** & **lab_4_intermediate**: Multi-step logic
- **lab_5_advanced** & **lab_6_expert**: Real-world complex scenarios

#### Lab Workflow (Step-by-Step):

```
┌─────────────────────────────────────────────────────────┐
│  Step 1: Read README.md                                 │
│  → Understand the problem, use case, and rules          │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 2: Review tasks.md                                │
│  → See the breakdown of tasks                           │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 3: Open starter_code.py                           │
│  → Implement logic where you see # TODO                 │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 4: Run tests.py                                   │
│  → Command: python tests.py                             │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Step 5: Debug & Iterate                                │
│  → Goal: All tests pass ✅                              │
└─────────────────────────────────────────────────────────┘
```

#### Example Lab Execution:
```bash
# Navigate to the lab folder
cd content/modules/collections/unit_1_lists/app_labs/lab_1_easy

# Run the tests
python tests.py
```

---

## 🎯 Learning Path

### Today's Focus: Collections Deep Dive

1. **Unit 1: Lists** → Understanding mutable ordered sequences
2. **Unit 2: Tuples** → Immutability and structured record data
3. **Unit 3: Dictionaries** → Key-value mapping for complex state
4. **Unit 4: Sets** → Uniqueness and mathematical operations
5. **Unit 5: Selection Guide** → Choosing the right collection for the right task

### Recommended Workflow:
**Knowledge** → **Exercises** → **Labs**

---

## 🆘 Support

If you encounter any issues:
- Review the knowledge materials for the relevant unit
- Check the lab README files for specific instructions
- Reach out to your instructor or teaching assistant
- Collaborate with your fellow trainees

---

## 📝 Notes

- All code examples use **healthcare domain** contexts (e.g., patient records, drug lists, clinic schedules)
- Labs build on top of each other - complete them in order
- Don't skip the exercises - they build foundational muscle memory!

---

**Happy Learning! 🎓**