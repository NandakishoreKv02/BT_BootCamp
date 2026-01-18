# Lab 6 Tasks: Advanced Workflow Manager

## Task 1: Track Active Meds
**Difficulty**: Intermediate | **Points**: 30

### Objective
Maintain a list of active treatments.

### Requirements
- Update `Patient` to have `self.active_meds = []`.
- Implement `prescribe(self, med_name)`.
- **Side Effect**: Append `med_name` to `self.active_meds`.

---

## Task 2: Prevent Duplicates
**Difficulty**: Advanced | **Points**: 40

### Objective
Use conditional logic to control side effects.

### Requirements
- Update `prescribe`.
- If `med_name` is already in `self.active_meds`, do **NOT** append it.
- **Return Value**: 
    - Return `True` if successfully added.
    - Return `False` if it was a duplicate.

---

## Task 3: Status Summary
**Difficulty**: Advanced | **Points**: 30

### Objective
Provide a query method.

### Requirements
- Implement `get_status(self)`.
- Return a string: "[name] currently taking: [med1, med2, ...]"
- If no meds, return "[name] currently taking no medications."
