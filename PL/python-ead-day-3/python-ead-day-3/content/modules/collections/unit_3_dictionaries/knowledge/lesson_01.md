---
title: Dictionaries Fundamentals
type: knowledge
module: collections
unit: unit_3_dictionaries
order: 1
difficulty: easy
tags: [dictionaries, key-value, mapping]
use_case: patient_records_management
---

# Dictionaries Fundamentals

## 1. What
Python dictionaries are **unordered, mutable collections** that store key-value pairs. They excel at fast lookups, mapping relationships, and representing structured data. In a clinic system, a dictionary can map patient IDs to records, doctor names to schedules, or appointment times to patient details. Dictionaries provide O(1) average-case lookup by key, making them ideal for caching, indexing, and configuration. They are not ideal for ordered sequences (use lists) or when you need multiple identical keys (keys must be unique and hashable). Scope: this lesson covers creation, access, modification, methods, comprehensions, and nested structures.

## 2. Example
```python
# Example 1: Create and access
patient = {"id": 101, "name": "John Doe", "blood_type": "A+"}
name = patient["name"]        # "John Doe"
blood = patient.get("blood_type", "Unknown")  # Safe access

# Example 2: Add, update, delete
patient["age"] = 35           # add new key
patient["name"] = "Jane Doe"  # update existing
del patient["blood_type"]     # remove key

# Example 3: Dictionary methods
keys = patient.keys()         # dict_keys(['id', 'name', 'age'])
values = patient.values()     # dict_values([101, 'Jane Doe', 35])
items = patient.items()       # key-value pairs

# Example 4: Real-world (healthcare)
appointments = {
	"09:00": {"patient_id": 101, "doctor_id": 201, "reason": "Checkup"},
	"10:00": {"patient_id": 102, "doctor_id": 202, "reason": "Follow-up"},
}
morning_appt = appointments["09:00"]
appointments["11:00"] = {"patient_id": 103, "doctor_id": 201, "reason": "Consultation"}

# Example 5: Dictionary comprehension
patient_ids = [101, 102, 103]
records = {pid: {"name": f"Patient {pid}", "status": "Active"} for pid in patient_ids}
```

## 3. Explanation
- **Key-Value Mapping**: Dictionaries store associations between unique keys and values. Keys must be hashable (strings, numbers, tuples), values can be anything.
- **Hash Table Implementation**: Python uses hash tables for O(1) average lookup. Keys are hashed to determine storage location.
- **Mutability**: You can add, update, and delete key-value pairs. Unlike lists, access is by key, not index.
- **Iteration**: Loop over keys (default), values, or items. Order is insertion-ordered (Python 3.7+).
- **Performance**: Lookups, inserts, deletes are O(1) average. Iteration is O(n). Space complexity is O(n).
- **Memory model**: Dictionaries use more memory than lists due to hash table overhead, but provide faster lookups.

## 4. Why
1. **Fast Lookups**: O(1) access by key makes dictionaries ideal for caching, indexing, and mapping relationships.
2. **Structured Data**: Represent complex objects (patient records, configurations) with named fields instead of positional indices.
3. **Flexible Schema**: Add/remove fields dynamically without restructuring, perfect for evolving data models.
4. **Readable Code**: `patient["name"]` is clearer than `patient[1]`, making code self-documenting.

## 5. Advantages & Disadvantages
**Advantages**
- O(1) average lookup, insert, delete by key
- Self-documenting with descriptive keys
- Flexible: add/remove keys dynamically
- Native JSON serialization for APIs

**Disadvantages**
- Higher memory overhead than lists
- Keys must be hashable (no lists/dicts as keys)
- No guaranteed order before Python 3.7
- Slower iteration than lists

## 6. Real-World Use Cases
**Healthcare**: Patient records indexed by ID `{101: {"name": "John", "blood_type": "A+"}}`. Doctor schedules by day `{"Monday": ["09:00", "10:00"]}`. Appointment lookup by time slot for fast conflict checking.

**eCommerce**: Product catalog by SKU `{"SKU-001": {"name": "Laptop", "price": 999}}`. Shopping cart by user ID `{user_id: [items]}`. Inventory tracking by warehouse location for quick stock checks.

**Banking**: Account balances by account number `{"ACC-123": 5000.00}`. Transaction metadata `{txn_id: {"amount": 100, "type": "debit"}}`. Currency exchange rates `{"USD": 1.0, "EUR": 0.85}` for fast conversion lookups.

## 7. Best Practices
- Use `.get(key, default)` instead of `dict[key]` to avoid KeyError on missing keys.
- Use `dict.setdefault(key, default)` to initialize keys if absent.
- Prefer dictionary comprehensions for transformations: `{k: v*2 for k, v in data.items()}`.
- Use `collections.defaultdict` when you need automatic default values for missing keys.
- Keep keys simple and hashable; avoid complex mutable objects.
- For ordered dictionaries pre-3.7, use `collections.OrderedDict`.
- Use `dict.update()` to merge dictionaries efficiently.

## 8. Top 3 Mistakes
1) **Accessing missing keys without .get()**
```python
patient = {"id": 101, "name": "John"}
age = patient["age"]  # KeyError!
```
Correct: use `.get()` with default.
```python
age = patient.get("age", 0)  # Returns 0 if missing
```

2) **Modifying dictionary while iterating**
```python
for key in appointments:
	if key < "10:00":
		del appointments[key]  # RuntimeError!
```
Correct: iterate over a copy of keys.
```python
for key in list(appointments.keys()):
	if key < "10:00":
		del appointments[key]
```

3) **Using mutable objects as keys**
```python
key = [1, 2, 3]
data = {key: "value"}  # TypeError: unhashable type: 'list'
```
Correct: use immutable types (tuples, strings).
```python
key = (1, 2, 3)
data = {key: "value"}  # Works!
```

---

## Check Your Understanding

Test your comprehension before moving to exercises. Try answering without looking back, then verify.

**Question 1**: What is the average time complexity of dictionary lookup by key?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

**Question 2**: True or False: Dictionary keys must be hashable.

**Question 3**: What happens when you access a missing key with `dict[key]`?
- A) Returns None
- B) Returns empty string
- C) Raises KeyError
- D) Returns 0

**Question 4**: Which method safely accesses a key with a default value?
- A) dict[key]
- B) dict.get(key, default)
- C) dict.find(key)
- D) dict.access(key)

**Question 5**: What does the following code produce?
```python
data = {"a": 1, "b": 2}
result = {k: v*2 for k, v in data.items()}
```
- A) {"a": 1, "b": 2}
- B) {"a": 2, "b": 4}
- C) [2, 4]
- D) Error

**Question 6**: Can you use a list as a dictionary key?
- A) Yes, always
- B) No, lists are not hashable
- C) Only if the list is empty
- D) Only with special syntax

**Question 7**: What does `dict.keys()` return?
- A) A list of keys
- B) A dict_keys view object
- C) A tuple of keys
- D) A set of keys

**Question 8**: Why is this code problematic?
```python
for key in patient:
    if key == "temp_field":
        del patient[key]
```
- A) Syntax error
- B) Modifying dict while iterating can cause RuntimeError
- C) del doesn't work in loops
- D) It's not problematic

---

### Answers

1. **A) O(1)** - Dictionary lookup is constant time on average
2. **True** - Keys must be hashable (immutable types)
3. **C) Raises KeyError** - Missing keys raise an exception
4. **B) dict.get(key, default)** - Safe access with fallback
5. **B) {"a": 2, "b": 4}** - Dict comprehension doubles values
6. **B) No, lists are not hashable** - Only immutable types can be keys
7. **B) A dict_keys view object** - Dynamic view, not a list
8. **B) Modifying dict while iterating can cause RuntimeError** - Classic Python pitfall

---

**Ready to Practice?** Move on to the exercises to apply these concepts hands-on!
