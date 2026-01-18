# Unit 1.7: Core Built-in Data Structures - Learning Outcomes

## Overview
Data structures are the containers that hold and organize information in your programs. In this unit, you will master Python's four primary built-in data structures: Lists, Tuples, Sets, and Dictionaries. Understanding when and how to use each is crucial for managing patient records, lab results, and medical device logs efficiently.

**Estimated Time**: 12-14 hours
- Knowledge: 2 hours
- Exercises: 4 hours
- App Labs: 6-8 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Lists (Ordered & Mutable)
- [ ] **Create** and manipulate lists of patient data.
- [ ] **Perform** indexing and slicing to extract specific ranges of data.
- [ ] **Apply** common list methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, and `reverse()`.

### Tuples (Ordered & Immutable)
- [ ] **Define** tuples for static data that should not change (e.g., medical constants or fixed coordinates).
- [ ] **Explain** the advantages of immutability and when to choose tuples over lists.
- [ ] **Perform** tuple unpacking to assign multiple variables at once.

### Sets (Unordered & Unique)
- [ ] **Utilize** sets to automatically remove duplicate entries from datasets (e.g., unique patient IDs in a log).
- [ ] **Perform** set operations: `union()`, `intersection()`, `difference()`, and `symmetric_difference()`.
- [ ] **Explain** why sets are highly efficient for membership testing.

### Dictionaries (Key-Value Pairs)
- [ ] **Construct** dictionaries to represent complex records (e.g., a patient profile with various attributes).
- [ ] **Perform** key-based lookups, updates, and removals.
- [ ] **Apply** dictionary methods: `keys()`, `values()`, `items()`, `get()`, and `update()`.

### Strategy & Selection
- [ ] **Categorize** data based on whether it needs to be ordered, unique, or mutable.
- [ ] **Select** the most appropriate data structure for a given healthcare scenario using the "Nature of Data" framework.

---

## Assessment Criteria

### Exercises (Pass: All tests passing)
- Correct usage of list methods for managing a dynamic queue.
- Successful use of sets to identify unique occurrences in clinical notes.
- Accurate mapping of patient keys to values using dictionaries.
- Proper use of tuples for fixed reference data.

### App Labs (Pass: 80% or higher)
- **Data Integrity**: Using the right structure to prevent accidental modification (tuples) or duplicates (sets).
- **Efficiency**: Leveraging dictionary lookups for performance.
- **Complexity Management**: Organizing nested data structures (e.g., a list of patient dictionaries) logically.
- **Code Style**: Following PEP 8 for container initialization and spacing.

---

## Next Steps
1. **Module 1.8: File I/O** will show you how to read data from local files into these structures.
2. **Module 2: Advanced Data Handling** will delve into specialized collections.

---

## Common Pitfalls to Avoid
✅ **Do**: Use `.get()` for dictionary lookups when the key might be missing to avoid `KeyError`.

❌ **Don't**: Use a list for lookups if the dataset is large and uniqueness is key; use a set or dictionary instead.

✅ **Do**: Use tuples for data that represents a single record of fixed items (e.g., `(lat, lon)` or `(first_name, last_name)`).

❌ **Don't**: Attempt to `append()` to a tuple; it will result in an `AttributeError`.

✅ **Do**: Remember that sets and dictionary keys must be "hashable" (immutable types like strings, numbers, or tuples).

❌ **Don't**: Use a list as a dictionary key.

✅ **Do**: Use list slicing `[:]` to create a shallow copy if you need to modify a list without affecting the original.

❌ **Don't**: Assume `list2 = list1` creates a copy; it only creates a new reference to the same memory object.
