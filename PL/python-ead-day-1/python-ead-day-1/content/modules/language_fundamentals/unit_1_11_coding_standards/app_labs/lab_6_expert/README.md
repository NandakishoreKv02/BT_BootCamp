---
title: "The Pythonic Auditor"
type: app_lab
module: language_fundamentals
unit: unit_1_11_coding_standards
lab_number: 6
difficulty: expert
use_case: security_compliance
domain: healthcare
order: 6
duration_hours: 2
tags:
  topics: ["pythonic", "pep8", "automation"]
  subtopics: ["comprehensive-refactoring"]
---

# Lab 6: The Pythonic Auditor

**Module**: Language Fundamentals  
**Objective**: Transform a "spaghetti code" script into a professional, Pythonic, and standards-compliant medical auditor.  
**Difficulty**: Expert  
**Context**: Healthcare - Information Security

## Generic Information
**Problem Statement**: You've been given a security script that runs on startup. It's written as one giant block of code with bad names, no functions, and no error handling. It's embarrassing to show to the compliance team. You must refactor it into a professional module.

## Use Case
**Title**: Professional Security Auditor  
**Description**: Refactor a script into a class-based or function-based professional module.

### Bad Script Provided (Mental Baseline)
```python
x = ["admin", "root", "guest"]
l = ["guest", "user1", "user2"]
for a in x:
  for u in l:
    if a == u:
      print("LOCK ACCOUNT "+u)
```

### Rules
1. Define a constant `UNAUTHORIZED_USERNAMES` for the forbidden list.
2. Use a membership check (`in`) to avoid nested loops if possible.
3. Wrap logic in a function `audit_logins(login_list)`.
4. Return a list of flagged names.
5. Use `if __name__ == "__main__":` to run a test.

## How to Use This Lab
1. Read `tasks.md`.
2. Edit `starter_code.py`.
3. Run `tests.py`.
