---
title: Dictionaries - Exercises
type: exercises
module: collections
unit: unit_3_dictionaries
order: 1
difficulty: easy
tags: [dictionaries, keys, values, methods, comprehension]
subtopics:
  - name: "Creation and Access"
    exercises: [1]
  - name: "Adding/Updating"
    exercises: [2]
  - name: "Removing"
    exercises: [3]
  - name: "Methods (keys/values)"
    exercises: [4]
  - name: "Safe Access (.get)"
    exercises: [5]
  - name: "Comprehension"
    exercises: [6]
  - name: "Nested Dictionaries"
    exercises: [7]
---

# Unit 3: Dictionaries - Exercises

Concept-focused drills testing dictionary fundamentals.

---

## Exercise 1: Dictionary Creation and Access

**SubTopic**: Creation and Access  
**Objective**: Master dictionary creation and key-based access

**Requirements**:
- Create a dictionary with 3 key-value pairs: `"a": 1, "b": 2, "c": 3`
- Access the value for key `"b"`
- Return the value

**Expected Test Cases**:
- Result should be `2`
- Result should be an integer
- Result should be positive

**Hints**:
<details>
<summary>💡 Hint 1: Syntax</summary>
Use curly braces `{}` to create a dictionary with `key: value` pairs.
</details>

<details>
<summary>💡 Hint 2: Access</summary>
Access values using square brackets with the key: `my_dict["key"]`.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
data = {"a": 1, "b": 2, "c": 3}
result = data["b"]
```
</details>

---

## Exercise 2: Adding and Updating Items

**SubTopic**: Adding/Updating  
**Objective**: Master dictionary modification

**Requirements**:
- Add a new key `"z"` with value `99`
- Update the existing key `"x"` to value `0`
- Return the modified dictionary

**Expected Test Cases**:
- Key `"z"` should be `99`
- Key `"x"` should be `0`
- Other keys should remain unchanged

**Hints**:
<details>
<summary>💡 Hint 1: Assignment</summary>
Use assignment syntax for both adding and updating: `my_dict["key"] = value`.
</details>

<details>
<summary>💡 Hint 2: Add vs Update</summary>
If the key exists, it updates. If not, it adds.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
data["z"] = 99  # Add
data["x"] = 0   # Update
```
</details>

---

## Exercise 3: Removing Items

**SubTopic**: Removing  
**Objective**: Master dictionary item removal

**Requirements**:
- Remove the key `"temp"` using `.pop()`
- Return the value that was associated with `"temp"`

**Expected Test Cases**:
- Should return the removed value (`99` in example)
- Key `"temp"` should be gone from dictionary
- Other keys should remain

**Hints**:
<details>
<summary>💡 Hint 1: Pop Method</summary>
Use `my_dict.pop("key")` to remove a key and get its value.
</details>

<details>
<summary>💡 Hint 2: Del vs Pop</summary>
`del` just removes; `.pop()` removes and returns the value.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
removed_value = data.pop("temp")
return removed_value
```
</details>

---

## Exercise 4: Dictionary Methods (keys, values)

**SubTopic**: Methods (keys/values)  
**Objective**: Master keys() and values() methods

**Requirements**:
- Get all keys as a list (convert view to list)
- Get all values as a list (convert view to list)
- Return a tuple of `(list_of_keys, list_of_values)`

**Expected Test Cases**:
- Keys list should contain all keys
- Values list should contain all values
- Both should be of type `list`

**Hints**:
<details>
<summary>💡 Hint 1: Methods</summary>
Use `.keys()` and `.values()` methods.
</details>

<details>
<summary>💡 Hint 2: Conversion</summary>
These return view objects, so wrap them in `list()`: `list(my_dict.keys())`.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
keys = list(data.keys())
values = list(data.values())
return (keys, values)
```
</details>

---

## Exercise 5: Safe Access with .get()

**SubTopic**: Safe Access (.get)  
**Objective**: Master .get() method for safe access

**Requirements**:
- Use `.get()` to access the key
- If key is missing, return `"Not Found"` (default value)
- Do NOT use if/else or try/except

**Expected Test Cases**:
- Should return value if key exists
- Should return `"Not Found"` if key is missing
- Should work on empty dictionaries

**Hints**:
<details>
<summary>💡 Hint 1: Get Method</summary>
Syntax: `my_dict.get(key, default_value)`.
</details>

<details>
<summary>💡 Hint 2: Default</summary>
The second argument is what gets returned if the key isn't found.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
result = data.get(key, "Not Found")
return result
```
</details>

---

## Exercise 6: Dictionary Comprehension

**SubTopic**: Comprehension  
**Objective**: Master dictionary comprehensions

**Requirements**:
- Create a dict where keys are numbers from the input list
- Values are the square of the keys
- Only include numbers greater than 2
- Return the dictionary

**Expected Test Cases**:
- Should contain valid key-value pairs (`3: 9`, `4: 16`, etc.)
- Should exclude numbers <= 2
- Should handle empty result

**Hints**:
<details>
<summary>💡 Hint 1: Syntax</summary>
`{key_expr: value_expr for item in iterable if condition}`.
</details>

<details>
<summary>💡 Hint 2: Logic</summary>
Key is `n`, value is `n**2`, condition is `n > 2`.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
result = {n: n**2 for n in numbers if n > 2}
return result
```
</details>

---

## Exercise 7: Nested Dictionaries

**SubTopic**: Nested Dictionaries  
**Objective**: Master nested dictionary access

**Requirements**:
- Create a nested dict: `{"group1": {"id": 1}, "group2": {"id": 2}}`
- Access the `"id"` value inside `"group2"`
- Return that id

**Expected Test Cases**:
- Result should be `2`
- Result should be integer
- Should strictly match the target path

**Hints**:
<details>
<summary>💡 Hint 1: Chained Access</summary>
Use multiple brackets: `my_dict["outer_key"]["inner_key"]`.
</details>

<details>
<summary>💡 Hint 2: Structure</summary>
First access `"group2"`, which gives you a dict. Then access `"id"` from that dict.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
data = {"group1": {"id": 1}, "group2": {"id": 2}}
result = data["group2"]["id"]
return result
```
</details>

---

## How to Use

1. **Read** the exercise objective and requirements
2. **Review** the hints if needed
3. **Write Code** in the `.py` file between the marked sections
4. **Run** the exercise file: `python unit_3_dictionaries_exercises.py`
5. **Validate** that all test cases pass
6. **Move** to the next exercise

---

## Key Concepts Covered

- Dictionary creation `{}` and access `[]`
- Adding and updating items `d[k] = v`
- Removing items with `.pop()`
- Using iteration methods `.keys()`, `.values()`
- Safe access with `.get()`
- Dictionary comprehensions `{k:v for ...}`
- Working with nested data structures
