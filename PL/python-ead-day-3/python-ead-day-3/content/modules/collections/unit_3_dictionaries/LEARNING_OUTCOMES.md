# Unit 3: Dictionaries - Learning Outcomes

## Overview
By completing this unit, you will master Python Dictionaries - high-performance associative arrays that map unique keys to values. You'll learn how to build complex data models, perform fast lookups, and use advanced dictionary methods for data management.

**Estimated Time**: 6-7 hours total
- Knowledge: 40 min
- Check Your Understanding: 15 min
- Exercises: 90-120 min
- App Labs (Easy, Intermediate, Advanced): 3-4 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Define** Python dictionaries and explain their key-value structure.
- [ ] **Explain** the concept of hashability and why only certain types can be keys.
- [ ] **Understand** dictionary time complexity: why lookups are O(1) on average.
- [ ] **Describe** the difference between dictionaries and lists for data retrieval.

### Creation & Modification

- [ ] **Create** dictionaries using literals `{}` and the `dict()` constructor.
- [ ] **Add** and **Update** entries using key assignment `d[key] = value`.
- [ ] **Remove** entries using `del`, `pop()`, and `popitem()`.
- [ ] **Clear** dictionaries completely using `clear()`.

### Access & Retrieval

- [ ] **Retrieve** values safely using the `get()` method to avoid KeyError.
- [ ] **Access** all keys using `.keys()`, all values using `.values()`, and all pairs using `.items()`.
- [ ] **Set** default values efficiently using `setdefault()` and `collections.defaultdict`.

### Iteration & Transformation

- [ ] **Iterate** over keys, values, and item pairs using for loops.
- [ ] **Use** dictionary comprehensions to create or transform dictionaries concisely.
- [ ] **Filter** dictionaries based on keys or values using comprehensions.

### Merging & Sorting

- [ ] **Merge** dictionaries using the `update()` method or the union operators `|` and `|=` (Python 3.9+).
- [ ] **Understand** how dictionaries handle duplicate keys during merges.
- [ ] **Sort** dictionaries by keys or values using the `sorted()` function.

### Best Practices

- [ ] **Use** `get()` for optional keys to prevent runtime crashes.
- [ ] **Prefer** `dict.items()` when you need both keys and values during iteration.
- [ ] **Use** `defaultdict` for grouping data or counting occurrences.
- [ ] **Keep** keys immutable (strings, numbers, or tuples of immutable types).

### Real-World Application

- [ ] **Map** Patient IDs to their full clinical records for instant lookup.
- [ ] **Store** configuration settings for a medical lab system.
- [ ] **Group** healthcare data by categories (e.g., grouping patients by blood type).
- [ ] **Translate** medical codes to human-readable descriptions.

---

## Assessment Criteria

### Exercises (Pass: All drills with all tests passing)
- Successfully complete all concept drills in `unit_3_dictionaries_exercises.py`.
- Correct use of dictionary-specific methods and comprehensions.
- Code follows PEP 8 conventions.

### App Labs (Pass: 80% or higher)
- **Functionality**: Correct implementation of key-value lookups and data aggregation.
- **Efficiency**: Use of O(1) lookups instead of O(n) list scans.
- **Safety**: Proper handling of missing keys and invalid input.

---

## Next Steps

After mastering dictionaries:
1. **Move to Unit 4: Sets** for unique collections and set math.
2. **Review Unit 5: Collection Selection Guide** to learn when to use Dicts vs Lists vs Sets.
3. **Apply** dictionaries as the basis for JSON-like data handling.

---

## Common Pitfalls to Avoid

✅ **Do**: Use `.get(key, default)` when you aren't certain a key exists.  
❌ **Don't**: Use `dict[key]` directly unless you are sure the key is present (avoids KeyError).

✅ **Do**: Use dictionary comprehensions for simple transformations.  
❌ **Don't**: Use them for complex logic that spans multiple lines of code.

✅ **Do**: Use immutable types (strings, ints) as keys.  
❌ **Don't**: Try to use a list as a dictionary key (causes TypeError: unhashable type).

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Create a dictionary that maps 3 medical departments to their room numbers?
2. Explain the difference between `pop()` and `popitem()`?
3. Merge two dictionaries without losing data from the second one?
4. Write a dictionary comprehension that swaps keys and values?
5. Explain why checking the length of a dictionary is fast?

If you answered "yes" to all, you're ready to proceed! 🎉
