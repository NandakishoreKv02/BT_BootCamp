---
title: Sets - Exercises
type: exercises
module: collections
unit: unit_4_sets
order: 1
difficulty: easy
tags: [sets, collections, uniqueness, math]
subtopics:
  - name: "Creation and Deduplication"
    exercises: [1]
  - name: "Adding and Removing"
    exercises: [2]
  - name: "Union and Intersection"
    exercises: [3]
  - name: "Difference and Symmetric Difference"
    exercises: [4]
  - name: "Set Comprehension"
    exercises: [5]
  - name: "Frozensets"
    exercises: [6]
  - name: "Membership and Subsets"
    exercises: [7]
---

# Unit 4: Sets - Exercises

Concept-focused drills testing implementation of set fundamentals.

---

## Exercise 1: Set Creation and Deduplication

**SubTopic**: Creation and Deduplication  
**Objective**: Master set creation and automatic deduplication

**Requirements**:
- Convert an input iterable (like a list or string) into a set
- Return the count of unique elements in that set

**Expected Test Cases**:
- List `[1, 2, 2, 3]` should return `3`
- Empty list should return `0`
- String `"abracadabra"` should return `5`

**Hints**:
<details>
<summary>💡 Hint 1: Constructor</summary>
Use the `set()` constructor to convert any iterable into a set.
</details>

<details>
<summary>💡 Hint 2: Count</summary>
Use the `len()` function to get the number of items in the set.
</details>

<details>
<summary>💡 Hint 3: See Solution</summary>

```python
unique_items = set(items)
return len(unique_items)
```
</details>

---

## Exercise 2: Basic Set Operations (Add and Discard)

**SubTopic**: Adding and Removing  
**Objective**: Master basic set modification methods

**Requirements**:
- Add an item to the set using `.add()`
- Remove an item from the set safely using `.discard()` (so it doesn't crash if the item is missing)
- Return the modified set

**Expected Test Cases**:
- Adding `4` and removing `2` from `{1, 2, 3}` should result in `{1, 3, 4}`
- Removing a non-existent item should not raise an error
- Adding an item that already exists should not change the set

**Hints**:
<details>
<summary>💡 Hint 1: Addition</summary>
Sets have an `.add()` method for individual items.
</details>

<details>
<summary>💡 Hint 2: Safe Removal</summary>
`.discard()` is safer than `.remove()` because it doesn't raise a KeyError if the item isn't found.
</details>

---

## Exercise 3: Union and Intersection

**SubTopic**: Union and Intersection  
**Objective**: Master Venn diagram logic using symbolic operators

**Requirements**:
- Calculate the union of two sets using `|`
- Calculate the intersection of two sets using `&`
- Return both results as a tuple: `(union, intersection)`

**Expected Test Cases**:
- `{1, 2}` and `{2, 3}` union is `{1, 2, 3}`, intersection is `{2}`
- Disjoint sets should return an empty set (`set()`) as their intersection

**Hints**:
<details>
<summary>💡 Hint 1: Operators</summary>
`a | b` is union (everything), `a & b` is intersection (common items).
</details>

---

## Exercise 4: Difference and Symmetric Difference

**SubTopic**: Difference and Symmetric Difference  
**Objective**: Master directional and mutual exclusion operations

**Requirements**:
- Calculate the difference (`A - B`) using `-`
- Calculate the symmetric difference using `^`
- Return both results as a tuple: `(difference, symmetric_diff)`

**Expected Test Cases**:
- `{1, 2, 3}` minus `{3, 4}` is `{1, 2}`
- Symmetric difference of `{1, 2}` and `{2, 3}` is `{1, 3}`

**Hints**:
<details>
<summary>💡 Hint 1: Operators</summary>
`a - b` finds items in `a` but NOT in `b`. `a ^ b` finds items in either set but NOT in both.
</details>

---

## Exercise 5: Set Comprehensions

**SubTopic**: Set Comprehension  
**Objective**: Master set comprehension syntax

**Requirements**:
- Use a set comprehension to filter even numbers from the input list
- Square each of those even numbers
- Return the resulting set

**Expected Test Cases**:
- Input `[1, 2, 3, 4]` should return `{4, 16}`
- Input with only odd numbers should return an empty set

**Hints**:
<details>
<summary>💡 Hint 1: Syntax</summary>
`{expression for item in iterable if condition}`
</details>

---

## Exercise 6: Frozensets

**SubTopic**: Frozensets  
**Objective**: Understand immutable sets

**Requirements**:
- Convert the input items into a `frozenset`
- Return the resulting frozenset object

**Expected Test Cases**:
- Result must be an instance of `frozenset`
- Result should contain the unique items from the input

**Hints**:
<details>
<summary>💡 Hint 1: Constructor</summary>
Use `frozenset(items)`.
</details>

---

## Exercise 7: Membership and Subsets

**SubTopic**: Membership and Subsets  
**Objective**: Master boolean set comparisons

**Requirements**:
- Check if an item is in a set (`in` operator)
- Check if one set is a subset of another (`issubset()` or `<=`)
- Return both results as a tuple: `(is_member, is_subset)`

**Expected Test Cases**:
- Correct boolean values for presence and subset containment
- Empty sets are always subsets of any other set

**Hints**:
<details>
<summary>💡 Hint 1: Membership</summary>
Use `item in my_set`.
</details>

<details>
<summary>💡 Hint 2: Subset</summary>
Use `set_a.issubset(set_b)` or `set_a <= set_b`.
</details>

---

## How to Use

1. **Read** the exercise objective and requirements
2. **Review** the hints if needed
3. **Write Code** in the `.py` file between the marked sections
4. **Run** the exercise file: `python unit_4_sets_exercises.py`
5. **Validate** that all test cases pass
6. **Move** to the next exercise

---

## Key Concepts Covered

- Set creation and uniqueness
- Adding and removing items (`.add`, `.discard`)
- Set operations (`|`, `&`, `-`, `^`)
- Set comprehensions
- Immutable sets (`frozenset`)
- Membership and subset testing
