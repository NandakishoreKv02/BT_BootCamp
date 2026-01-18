---
title: Tuples - Exercises
type: exercises
module: collections
unit: unit_2_tuples
order: 1
difficulty: easy
tags: [tuples, packing, unpacking, immutability, named-tuples]
subtopics:
  - name: "Create"
    exercises: [1]
  - name: "Pack/Unpack"
    exercises: [2]
  - name: "Single Element"
    exercises: [3]
  - name: "Slice"
    exercises: [4]
  - name: "Concatenate"
    exercises: [5]
  - name: "Methods (count/index)"
    exercises: [6]
  - name: "Named Tuples"
    exercises: [7]
---

# Unit 2: Tuples - Exercises

Concept-focused drills testing tuple fundamentals.

---

## Exercise 1: Tuple Creation and Indexing

**SubTopic**: Create  
**Objective**: Master tuple creation and index access

**Requirements**:
- Create a tuple with at least 3 items (e.g., vitals: temp, pulse, bp_sys, bp_dia)
- Access and print the first element using index 0
- Access and print the last element using index -1
- Return a tuple of (first_item, last_item)

**Reference Variables**:
```python
vitals = (98.6, 72, 120, 80)
```

**Expected Test Cases**:
- `result == (98.6, 80)` should be True
- Length of `vitals` should be >= 3
- `first_item` should equal `vitals[0]`

**Hints**:
<details>
<summary>💡 Hint 1: Getting Started</summary>
Use parentheses to create a tuple and access elements by their index position.
</details>

<details>
<summary>💡 Hint 2: Accessing Elements</summary>
Use `tuple[0]` for first element and `tuple[-1]` for last element.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
vitals = (98.6, 72, 120, 80)
first_item = vitals[0]
last_item = vitals[-1]
result_1 = (first_item, last_item)
```
</details>

---

## Exercise 2: Tuple Packing and Unpacking

**SubTopic**: Pack/Unpack  
**Objective**: Master tuple packing and unpacking

**Requirements**:
- Pack three values into a tuple without parentheses: 101, 'John Doe', 'A+'
- Unpack the tuple into three separate variables
- Return the middle value (name)

**Expected Test Cases**:
- Result should be `"John Doe"`
- `patient_id` should be `101`
- `blood_type` should be `"A+"`
- `patient_info` should be a tuple

**Hints**:
<details>
<summary>💡 Hint 1: Packing</summary>
Packing: `patient_info = value1, value2, value3` (no parentheses needed)
</details>

<details>
<summary>💡 Hint 2: Unpacking</summary>
Unpacking: `var1, var2, var3 = patient_info`
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
patient_info = 101, "John Doe", "A+"  # packing
patient_id, name, blood_type = patient_info  # unpacking
result_2 = name
```
</details>

---

## Exercise 3: Single-Element Tuple

**SubTopic**: Single Element  
**Objective**: Master single-element tuple syntax

**Requirements**:
- Create a single-element tuple containing the number 42
- Use trailing comma syntax
- Verify it's a tuple, not an int

**Expected Test Cases**:
- Should be a tuple type
- Should equal `(42,)`
- Should have exactly 1 element

**Hints**:
<details>
<summary>💡 Hint 1: Trailing Comma</summary>
Single-element tuple requires trailing comma: `(42,)`
</details>

<details>
<summary>💡 Hint 2: Common Mistake</summary>
Without comma, `(42)` is just an int in parentheses, not a tuple!
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
single_tuple = (42,)  # Note the trailing comma
```
</details>

---

## Exercise 4: Tuple Slicing

**SubTopic**: Slice  
**Objective**: Master tuple slicing syntax

**Requirements**:
- Given tuple of numbers, extract a slice from index 1 to 4
- Extract another slice: last 3 elements
- Return both slices as a tuple of tuples

**Reference Variables**:
```python
numbers = (10, 20, 30, 40, 50, 60)
```

**Expected Test Cases**:
- Slice `[1:4]` should be `(20, 30, 40)`
- Last 3 elements should be `(40, 50, 60)`
- Slices should be tuples

**Hints**:
<details>
<summary>💡 Hint 1: Slicing Syntax</summary>
Slicing uses the format `tuple[start:end]` where start is inclusive and end is exclusive.
</details>

<details>
<summary>💡 Hint 2: Negative Indexing</summary>
Use `tuple[-3:]` to get last 3 elements.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
numbers = (10, 20, 30, 40, 50, 60)
slice_1 = numbers[1:4]
slice_2 = numbers[-3:]
result_4 = (slice_1, slice_2)
```
</details>

---

## Exercise 5: Tuple Concatenation

**SubTopic**: Concatenate  
**Objective**: Master tuple concatenation

**Requirements**:
- Concatenate two tuples using the + operator
- First tuple: (1, 2, 3)
- Second tuple: (4, 5, 6)
- Return the combined tuple

**Expected Test Cases**:
- Result should be `(1, 2, 3, 4, 5, 6)`
- Should have 6 elements
- Should be a tuple

**Hints**:
<details>
<summary>💡 Hint 1: Concatenation</summary>
Use + operator to concatenate tuples: `tuple1 + tuple2`
</details>

<details>
<summary>💡 Hint 2: Immutability</summary>
Result is a new tuple, original tuples remain unchanged.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_5 = tuple1 + tuple2
```
</details>

---

## Exercise 6: Tuple Methods (count and index)

**SubTopic**: Methods  
**Objective**: Master tuple methods count() and index()

**Requirements**:
- Given tuple: (1, 2, 3, 2, 4, 2, 5)
- Count how many times 2 appears
- Find the index of the first occurrence of 2
- Return both results as a tuple

**Reference Variables**:
```python
data = (1, 2, 3, 2, 4, 2, 5)
```

**Expected Test Cases**:
- 2 appears 3 times
- First occurrence of 2 is at index 1
- Result should be `(3, 1)`

**Hints**:
<details>
<summary>💡 Hint 1: Count Method</summary>
Use `.count(value)` to count occurrences.
</details>

<details>
<summary>💡 Hint 2: Index Method</summary>
Use `.index(value)` to find first occurrence index.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
data = (1, 2, 3, 2, 4, 2, 5)
count_result = data.count(2)
index_result = data.index(2)
result_6 = (count_result, index_result)
```
</details>

---

## Exercise 7: Named Tuples

**SubTopic**: Named Tuples  
**Objective**: Master named tuple creation and usage

**Requirements**:
- Import namedtuple from collections
- Create a named tuple called 'Patient' with fields: id, name, blood_type
- Create an instance with id=101, name='Jane Doe', blood_type='O+'
- Access the name field and return it

**Expected Test Cases**:
- Name should be `"Jane Doe"`
- `patient.id` should be `101`
- `blood_type` should be `"O+"`
- Index access `patient[1]` should also work

**Hints**:
<details>
<summary>💡 Hint 1: Import</summary>
`from collections import namedtuple`
</details>

<details>
<summary>💡 Hint 2: Define Named Tuple</summary>
`Patient = namedtuple('Patient', ['id', 'name', 'blood_type'])`
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
from collections import namedtuple

Patient = namedtuple('Patient', ['id', 'name', 'blood_type'])
patient = Patient(id=101, name='Jane Doe', blood_type='O+')
result_7 = patient.name
```
</details>

---

## How to Use

1. **Read** the exercise objective and requirements
2. **Review** the reference variables provided
3. **Understand** the expected test cases
4. **Write Code** in the `.py` file between the marked sections
5. **Run** the exercise file: `python exercise_2_tuples.py`
6. **Validate** that all test cases pass
7. **Move** to the next exercise

---

## Key Concepts Covered

- Tuple creation and initialization
- Indexing and slicing
- Tuple packing and unpacking
- Single-element tuple syntax (trailing comma)
- Tuple concatenation
- Tuple methods: count(), index()
- Named tuples for readable code
