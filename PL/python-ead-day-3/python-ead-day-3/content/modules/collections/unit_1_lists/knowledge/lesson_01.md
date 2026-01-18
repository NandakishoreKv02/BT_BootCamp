---
title: Lists Fundamentals
type: knowledge
module: collections
unit: unit_1_lists
order: 1
difficulty: easy
tags: [lists, indexing, slicing]
use_case: appointment_scheduling
---

# Lists Fundamentals

## 1. What
Python lists are ordered, mutable collections that let you store and work with sequences of items. They shine when you need to maintain order, grow or shrink collections, and iterate predictably. In a clinic system, a list can hold appointment slots, patient IDs in a waiting queue, or messages to be sent. Lists preserve insertion order, allow duplicates, and support fast append/pop at the end. They are not ideal for membership checks at large scale (linear time) or for enforcing uniqueness (use a set for that). Scope: this lesson covers creation, indexing, slicing, mutation, iteration, and common list operations.

## 2. Example
```python
# Example 1: Create and append
slots = ["09:00", "10:00", "11:00"]
slots.append("14:00")  # add new slot

# Example 2: Indexing and slicing
first = slots[0]        # "09:00"
morning = slots[:2]     # ["09:00", "10:00"]

# Example 3: Insert and remove
slots.insert(1, "09:30")  # keep order
slots.remove("11:00")     # remove by value

# Example 4: Sort and deduplicate politely
slots.append("10:00")
slots = sorted(set(slots))  # simple uniqueness + order

# Example 5: Real-world (healthcare)
appointments = [
	{"patient_id": 101, "doctor_id": 201, "time": "09:00"},
	{"patient_id": 102, "doctor_id": 202, "time": "10:00"},
]
appointments.append({"patient_id": 103, "doctor_id": 201, "time": "11:00"})
filtered = [a for a in appointments if a["doctor_id"] == 201]
```

## 3. Explanation
- **Order**: Lists preserve insertion order, making them ideal for queues, timelines, and ordered results.
- **Mutability**: You can append, insert, remove, and sort in place; this is convenient but requires care with shared references.
- **Indexing & slicing**: Constant-time access by index; slicing creates shallow copies, which is useful for subranges without mutating the original.
- **Iteration**: Straightforward looping; list comprehensions provide concise transformations and filters.
- **Performance**: Appends at the end are amortized O(1); inserts/removes in the middle are O(n); membership checks are O(n). If you need frequent membership tests, add a companion set.
- **Memory model**: Lists store references, not copies. Mutating referenced objects affects all holders of that object.

## 4. Why
1. **Ordered workflows**: Appointment queues and notification batches depend on predictable order.
2. **Fast growth**: Adding slots or tasks dynamically is efficient at list tails.
3. **Expressive transforms**: Comprehensions make filtering and mapping appointment data concise.
4. **Interoperable**: Lists serialize cleanly to JSON for APIs and front-end consumption.

## 5. Advantages & Disadvantages
**Advantages**
- Simple, readable syntax for ordered data
- Fast append/pop at the end
- Rich built-ins: sort, reverse, count, index, comprehensions

**Disadvantages**
- O(n) membership and mid-list inserts/removals
- No uniqueness guarantees (duplicates easy to introduce)
- Shallow copies via slicing can surprise when holding mutable items

## 6. Real-World Use Cases
**Healthcare**: Appointment slot lists; waiting-room queue; batch lab result notifications.

**eCommerce**: Shopping cart item list in order added; browsing history; prioritized packing queue.

**Banking**: Recent transaction feed; pending approval queue; batch payment instructions ordered by cut-off time.

## 7. Best Practices
- Keep list items uniform in shape (dicts with same keys) for predictable processing.
- Pair a list with a set when you need both order and fast membership checks.
- Avoid mutating lists while iterating; iterate over a copy when removing items.
- Use comprehensions for clarity; fall back to loops when logic is multi-step or needs early exits.
- For large datasets that are append-only and need uniqueness, consider `list` + `set` or move to `deque`/database.

## 8. Top 3 Mistakes
1) **Mutating while iterating**
```python
for slot in slots:
	if slot < "10:00":
		slots.remove(slot)  # skips elements
```
Correct: build a new list.
```python
slots = [s for s in slots if s >= "10:00"]
```

2) **Assuming membership is fast**
```python
"15:00" in slots  # O(n) scan
```
Correct: maintain a companion set for fast checks.
```python
slot_set = set(slots)
"15:00" in slot_set
```

3) **Sharing mutable items unintentionally**
```python
template = {"doctor_id": None, "time": None}
appointments = [template] * 3  # all references same dict
```
Correct: copy per element.
```python
appointments = [template.copy() for _ in range(3)]
```

---

## Check Your Understanding

Test your comprehension before moving to exercises. Try answering without looking back, then verify.

**Question 1**: What is the time complexity of checking if an item exists in a list using the `in` operator?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

**Question 2**: True or False: Lists in Python maintain the insertion order of elements.

**Question 3**: What happens when you use `list.remove(item)` and the item doesn't exist?
- A) Returns None
- B) Returns False
- C) Raises ValueError
- D) Does nothing

**Question 4**: Which operation is most efficient on Python lists?
- A) Inserting at the beginning
- B) Appending at the end
- C) Removing from the middle
- D) Searching for an element

**Question 5**: What does the following code produce?
```python
nums = [1, 2, 3]
result = [x * 2 for x in nums if x > 1]
```
- A) [2, 4, 6]
- B) [4, 6]
- C) [2, 3]
- D) [1, 2, 3]

**Question 6**: What's the difference between `list.sort()` and `sorted(list)`?
- A) No difference, they're identical
- B) sort() modifies in place, sorted() returns new list
- C) sorted() is faster
- D) sort() works only on numbers

**Question 7**: What does slicing `my_list[1:4]` return?
- A) Elements at indices 1, 2, 3
- B) Elements at indices 1, 2, 3, 4
- C) Elements at indices 0, 1, 2, 3
- D) Elements at index 1 and 4

**Question 8**: Why is this code problematic?
```python
for appointment in appointments:
    if appointment['time'] < '10:00':
        appointments.remove(appointment)
```
- A) Syntax error
- B) Modifying list while iterating can skip elements
- C) remove() doesn't work in loops
- D) It's not problematic

---

### Answers

1. **C) O(n)** - The `in` operator scans through the list linearly
2. **True** - Lists preserve insertion order
3. **C) Raises ValueError** - Attempting to remove non-existent item raises an error
4. **B) Appending at the end** - Append is amortized O(1), others are O(n)
5. **B) [4, 6]** - Filters elements > 1 (2, 3), then doubles them (4, 6)
6. **B) sort() modifies in place, sorted() returns new list** - Key difference in mutability
7. **A) Elements at indices 1, 2, 3** - Slicing is inclusive of start, exclusive of end
8. **B) Modifying list while iterating can skip elements** - Classic Python pitfall

---

**Ready to Practice?** Move on to the exercises to apply these concepts hands-on!
