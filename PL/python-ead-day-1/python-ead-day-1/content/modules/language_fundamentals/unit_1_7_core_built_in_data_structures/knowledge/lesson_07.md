---
title: "Core Data Structures: Organizing Information"
type: knowledge
module: language_fundamentals
unit: unit_1_7_core_built_in_data_structures
order: 7
difficulty: beginner
tags:
  subtopics:
    - lists
    - tuples
    - sets
    - dictionaries
---

# Unit 1.7: Core Built-in Data Structures

## 1. What
**Data Structures** are specialized formats for organizing and storing data. In Python, four built-in types are the foundations of almost every program:
1.  **Lists**: Ordered, mutable collections (like a patient queue).
2.  **Tuples**: Ordered, immutable collections (like fixed research coordinates).
3.  **Sets**: Unordered collections of unique items (like a list of distinct diagnoses).
4.  **Dictionaries**: Key-value pairs (like a patient record where 'ID' maps to 'Doe^John').

---

## 2. Example

### Example 1: Lists (The Dynamic Queue)
```python
patients = ["Alice", "Bob"]
patients.append("Charlie") # Add to end
patients.insert(0, "Dave") # Add to beginning
print(patients[1])         # Accessing Alice
```

### Example 2: Tuples (The Fixed Constant)
```python
# A patient's fixed birth record: (Year, Month, Day)
dob = (1980, 5, 12)
# dob[0] = 1981  # ERROR: Tuples are immutable
```

### Example 3: Sets (Uniqueness)
```python
# Raw symptoms often have duplicates
raw_symptoms = ["Fever", "Cough", "Fever", "Nausea"]
unique_symptoms = set(raw_symptoms)
print(unique_symptoms) # {'Fever', 'Cough', 'Nausea'}
```

### Example 4: Dictionaries (Mappings)
```python
patient_record = {
    "mrn": "12345",
    "name": "Smith^Jane",
    "vitals": [80, 120, 72]
}
print(patient_record["name"])
```

---

## 3. Explanation

### Choosing the Right Structure
| Feature | List | Tuple | Set | Dictionary |
| :--- | :--- | :--- | :--- | :--- |
| **Ordered** | Yes | Yes | No | Yes (since 3.7+) |
| **Mutable** | Yes | No | Yes | Yes |
| **Duplicates** | Yes | Yes | No | No (Keys must be unique) |
| **Fast Lookup** | No (O(n)) | No (O(n)) | **Yes (O(1))** | **Yes (O(1))** |

### Common Methods
- **Lists**: `.append()`, `.pop()`, `.sort()`, `.extend()`
- **Dictionaries**: `.keys()`, `.values()`, `.get(key, default)`, `.update()`
- **Sets**: `.add()`, `.remove()`, `.intersection()`, `.union()`

---

## 4. Why

### Why Lists?
- When the **order** of items matters (e.g., chronological order of lab results).
- When you need to frequently add or remove items.

### Why Tuples?
- **Safety**: To prevent accidental modification of critical data.
- **Performance**: Tuples are slightly faster and use less memory than lists.
- **Dictionary Keys**: Only immutable objects (like tuples) can be used as keys.

### Why Sets?
- **Deduplication**: Automatically removing duplicate records from an import.
- **Fast Search**: Checking if `id in set_of_1_million_ids` is nearly instantaneous.

### Why Dictionaries?
- **Direct Access**: Instead of searching a whole list for MRN 5, you go directly to `records["5"]`.

---

## 5. Advantages & Disadvantages

### Advantages
- **Versatility**: You can nest them (e.g., a list of dictionaries).
- **Batteries Included**: No external libraries needed for 90% of data handling.
- **Memory Management**: Python handles growing and shrinking these containers automatically.

### Disadvantages
- **Memory Overhead**: Large dictionaries and sets use more RAM than compact arrays.
- **Complexity**: Deeply nested structures (`dict[list[dict]]`) can become hard to navigate.

---

## 6. Real-World Use Cases

### Case 1: Prescription Tracking (List)
A list keeps track of the sequence of medications administered.
```python
meds = ["Aspirin", "Ibuprofen"]
meds.append("Metformin")
```

### Case 2: Encounter Data (Dictionary)
Mapping a unique Encounter ID to the full data of that visit.
```python
encounters = {
    "ENC_101": {"doctor": "Dr. Strange", "dept": "ER"},
    "ENC_102": {"doctor": "Dr. House", "dept": "Diag"}
}
```

### Case 3: Unique Pathogens (Set)
Tracking distinct bacterial strains found in a ward.
```python
strains = {"MRSA", "E.Coli"}
strains.add("MRSA") # No change, already exists
```

---

## 7. Best Practices

### Best Practice 1: Use `.get()` for Dictionaries
**Why**: Avoids `KeyError` crashes.
```python
# Safer
weight = patient_dict.get("weight", 0) # Returns 0 if "weight" is missing
```

### Best Practice 2: Use List Comprehensions (Intro)
**Why**: More Pythonic for simple filter/map operations.
```python
# Create a list of high HRs
high_vitals = [v for v in vitals if v > 100]
```

### Best Practice 3: Tuple Unpacking
**Why**: Cleaner code when a function or record returns multiple fixed items.
```python
# record = ("Alice", "Fever", 39.5)
name, diagnosis, temp = record
```

---

## 8. Top 3 Mistakes

### Mistake 1: Modifying a List While Iterating
#### Improper Code
```python
for p in patients:
    if p == "Bob":
        patients.remove(p) # Can skip items in the loop
```
#### Correction
Iterate over a copy: `for p in patients[:]`.

### Mistake 2: Missing Key Error
#### Improper Code
```python
print(record["blood_type"]) # Crashes if key is missing
```
#### Correction
Use `record.get("blood_type")` or `if "blood_type" in record:`.

### Mistake 3: Equality vs Identity (Revisited for containers)
#### Improper Code
```python
list1 = [1, 2]
list2 = [1, 2]
print(list1 is list2) # False! Different memory, same content.
```
#### Correction
Use `==` to compare content of lists/dicts/sets.
