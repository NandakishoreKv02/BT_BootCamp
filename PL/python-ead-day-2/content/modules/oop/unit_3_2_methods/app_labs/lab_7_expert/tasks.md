# Lab 7 Tasks: Production-Grade Clinical Auditor

## Task 1: Audit Initialization
**Difficulty**: Intermediate | **Points**: 15

### Objective
Track every change to an object.

### Requirements
- Update `Patient` to have `self.audit_logs = []`.
- Implement a helper method `_log(self, action)`.
- **Logic**: Append a string "[Action Name] performed" to `self.audit_logs`.

---

## Task 2: Advanced Census Manager
**Difficulty**: Advanced | **Points**: 25

### Objective
Coordinate class state with auditing.

### Requirements
- Use class variable `census`.
- In `__init__`, increment census AND call `self._log("Initalization")`.

---

## Task 3: Integrated Business Logic
**Difficulty**: Expert | **Points**: 40

### Objective
Combine static, class, and instance methods.

### Requirements
- Implement `apply_treatment(self, severity_index)`.
- It should:
    1. Call a static method `calculate_recovery_time(severity_index)`.
    2. Recovery Time Formula: `severity_index * 2`.
    3. Update `self.recovery_est` with the result.
    4. Call `self._log("Treatment Applied")`.
    5. Return recovery time.

---

## Task 4: Bulk Ingestion Auditor
**Difficulty**: Expert | **Points**: 20

### Objective
Factory integration with audit trail.

### Requirements
- Create `@classmethod from_records(cls, list_of_dicts)`.
- Create multiple patients and return a list of objects.
- Ensure each created object has a unique "Initalization" log entry.
