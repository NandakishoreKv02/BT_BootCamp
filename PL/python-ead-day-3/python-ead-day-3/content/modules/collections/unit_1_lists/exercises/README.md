---
title: Lists - Exercises
type: exercises
module: collections
unit: unit_1_lists
order: 1
difficulty: easy
tags: [lists, creation, slicing, methods, comprehensions]
subtopics:
  - name: "Create"
    exercises: [1]
  - name: "Slice"
    exercises: [2]
  - name: "Methods (Append/Remove)"
    exercises: [3]
  - name: "Comprehension - Filtering"
    exercises: [4]
  - name: "Comprehension - Transformation"
    exercises: [5]
  - name: "Sorting"
    exercises: [6]
  - name: "Membership & Counting"
    exercises: [7]
---

# Unit 1: Lists - Exercises

Concept-focused drills testing list fundamentals.

---

## Exercise 1: List Creation and Indexing

**SubTopic**: Create  
**Objective**: Master list creation and index access

**Requirements**:
- Create a list with at least 3 items
- Access and print the first element using index 0
- Access and print the last element using index -1
- Return a tuple of (first_item, last_item)

**Reference Variables**:
```python
items = [1, 2, 3]
```

**Expected Test Cases**:
- `result == (1, 3)` should be True
- Length of `items` should be >= 3
- `first_item` should equal `items[0]`

**Hints**:
<details>
<summary>💡 Hint 1: Getting Started</summary>
Use square brackets to create a list and access elements by their index position.
</details>

<details>
<summary>💡 Hint 2: Accessing Elements</summary>
Use `list[0]` for first element and `list[-1]` for last element.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
items = [1, 2, 3]
first_item = items[0]
last_item = items[-1]
result_1 = (first_item, last_item)
```
</details>

---

## Exercise 2: List Slicing
SubTopic**: Slice  
**
**Objective**: Master list slicing syntax

**Requirements**:
- Given a list of numbers, extract a slice from index 1 to 4
- Extract another slice: all items except the first one
- Return both slices in a tuple

**Reference Variables**:
```python
numbers = [10, 20, 30, 40, 50, 60]
```

**Expected Test Cases**:
- Slice `[1:4]` should be `[20, 30, 40]`
- Slice `[1:]` should be `[20, 30, 40, 50, 60]`
- First slice should have 3 elements

**Hints**:
<details>
<summary>💡 Hint 1: Slicing Syntax</summary>
Slicing uses the format `list[start:end]` where start is inclusive and end is exclusive.
</details>

<details>
<summary>💡 Hint 2: Open-ended Slices</summary>
Use `list[1:]` to get all elements from index 1 to the end.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
numbers = [10, 20, 30, 40, 50, 60]
slice_1 = numbers[1:4]
slice_2 = numbers[1:]
```
</details>

---

## Exercise 3: List Methods (Append and Remove)
SubTopic**: Methods (Append/Remove)  
**
**Objective**: Master list mutating methods

**Requirements**:
- Start with a list: `[1, 2, 3, 2, 4]`
- Append the number 5 to the end
- Remove the first occurrence of 2
- Return the modified list and its length

**Reference Variables**:
```python
my_list = [1, 2, 3, 2, 4]
```

**Expected Test Cases**:
- Modified list should be `[1, 3, 2, 4, 5]`
- Length should be 5
- 5 should be in the list
- Only the first occurrence of 2 should be removed

**Hints**:
<details>
<summary>💡 Hint 1: Adding Elements</summary>
Use `.append()` method to add an element to the end of a list.
</details>

<details>
<summary>💡 Hint 2: Removing Elements</summary>
Use `.remove(value)` to remove the first occurrence of a value from the list.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
my_list = [1, 2, 3, 2, 4]
my_list.append(5)
my_list.remove(2)
modified_list = my_list
list_length = len(modified_list)
```
</details>

---

##SubTopic**: Comprehension - Filtering  
** Exercise 4: List Comprehension - Filtering

**Objective**: Master list comprehension with filtering

**Requirements**:
- Given list: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- Filter numbers greater than 5
- Use list comprehension (single line preferred)
- Return the filtered list

**Reference Variables**:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Expected Test Cases**:
- Result should be `[6, 7, 8, 9, 10]`
- All items should be > 5
- Should have 5 items

**Hints**:
<details>
<summary>💡 Hint 1: List Comprehension Structure</summary>
List comprehensions follow the pattern: `[expression for item in list if condition]`
</details>

<details>
<summary>💡 Hint 2: Filtering Condition</summary>
Use `if x > 5` to filter numbers greater than 5.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_4 = [x for x in numbers if x > 5]
```
</details>

---
SubTopic**: Comprehension - Transformation  
**
## Exercise 5: List Comprehension - Transformation

**Objective**: Master list comprehension with transformation

**Requirements**:
- Given list: `[1, 2, 3, 4, 5]`
- Square each number using list comprehension
- Return the transformed list

**Reference Variables**:
```python
numbers = [1, 2, 3, 4, 5]
```

**Expected Test Cases**:
- Result should be `[1, 4, 9, 16, 25]`
- Should have 5 items
- Last item should be 25 (5²)

**Hints**:
<details>
<summary>💡 Hint 1: Transformation Pattern</summary>
Use list comprehension to transform each element: `[expression for item in list]`
</details>

<details>
<summary>💡 Hint 2: Squaring Numbers</summary>
Square a number using `x**2` or `x * x`.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
numbers = [1, 2, 3, 4, 5]
result_5 = [x**2 for x in numbers]
```
</details>

--SubTopic**: Sorting  
**-

## Exercise 6: Sorting Lists

**Objective**: Master list sorting

**Requirements**:
- Given list: `[3, 1, 4, 1, 5, 9, 2, 6]`
- Sort the list in ascending order (without modifying original)
- Return both the original and sorted lists

**Reference Variables**:
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
```

**Expected Test Cases**:
- Original list should remain unchanged: `[3, 1, 4, 1, 5, 9, 2, 6]`
- Sorted list should be: `[1, 1, 2, 3, 4, 5, 6, 9]`
- Sorted list should be in ascending order

**Hints**:
<details>
<summary>💡 Hint 1: Sorting Without Modifying</summary>
Use `sorted(list)` to create a new sorted list without changing the original.
</details>

<details>
<summary>💡 Hint 2: Keeping Original</summary>
Store the original list in one variable and the sorted result in another.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
result_6 = (numbers, sorted_numbers)
```
</details>

--SubTopic**: Membership & Counting  
**-

## Exercise 7: Membership Checking and Counting

**Objective**: Master membership checking and counting

**Requirements**:
- Given list: `['apple', 'banana', 'apple', 'orange', 'apple']`
- Check if 'apple' is in the list (True/False)
- Count how many times 'apple' appears
- Return both results in a tuple

**Reference Variables**:
```python
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
```

**Expected Test Cases**:
- 'apple' should be in the list: `True`
- 'apple' should appear 3 times
- Result should be tuple: `(True, 3)`

**Hints**:
<details>
<summary>💡 Hint 1: Membership Testing</summary>
Use the `in` operator to check if an element exists in a list: `item in list`
</details>

<details>
<summary>💡 Hint 2: Counting Occurrences</summary>
Use the `.count(item)` method to count how many times an item appears.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
is_present = 'apple' in fruits
count = fruits.count('apple')
result_7 = (is_present, count)
```
</details>

---

## How to Use

1. **Read** the exercise objective and requirements
2. **Review** the reference variables provided
3. **Understand** the expected test cases
4. **Write Code** in the `.py` file between the marked sections
5. **Run** the exercise file: `python unit_1_lists_exercises.py`
6. **Validate** that all test cases pass
7. **Move** to the next exercise

---

## Key Concepts Covered

- List creation and initialization
- Indexing and slicing
- List methods: append, remove, count
- List comprehensions for filtering and transformation
- Sorting lists
- Membership checking
