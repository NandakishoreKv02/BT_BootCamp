# Unit 1: Lists - Learning Outcomes

## Overview
By completing this unit, you will master Python lists - ordered, mutable collections that are fundamental to most Python programs. You'll learn to create, manipulate, and optimize lists for real-world scenarios.

**Estimated Time**: 5-6 hours total
- Knowledge: 30 min
- Check Your Understanding: 10 min
- Exercises: 60-90 min
- App Lab 1: 2 hours

---

## Learning Outcomes

After successfully completing this unit, you will be able to:

### Knowledge & Understanding

- [ ] **Define** what Python lists are and explain their characteristics (ordered, mutable, allows duplicates)
- [ ] **Explain** when to use lists versus other data structures (sets, tuples, dicts)
- [ ] **Understand** list time complexity for common operations (access, append, insert, search)
- [ ] **Describe** how lists store references to objects, not copies

### Creation & Access

- [ ] **Create** lists using square brackets and list() constructor
- [ ] **Access** elements using positive and negative indexing
- [ ] **Extract** sublists using slicing syntax [start:end:step]
- [ ] **Retrieve** first, last, and arbitrary elements safely

### Modification

- [ ] **Append** elements to the end of a list efficiently
- [ ] **Insert** elements at specific positions
- [ ] **Remove** elements by value using remove() and by index using del/pop()
- [ ] **Modify** elements in place by index assignment
- [ ] **Sort** lists in place (sort()) and create sorted copies (sorted())

### Iteration & Transformation

- [ ] **Iterate** through lists using for loops
- [ ] **Filter** lists using list comprehensions with conditions
- [ ] **Transform** lists using list comprehensions with expressions
- [ ] **Combine** filtering and transformation in single comprehensions

### Operations

- [ ] **Check** membership using the 'in' operator
- [ ] **Count** occurrences of elements using count() method
- [ ] **Find** element positions using index() method
- [ ] **Concatenate** lists using + operator or extend() method
- [ ] **Reverse** lists using reverse() method or [::-1] slicing

### Best Practices

- [ ] **Avoid** mutating lists while iterating over them
- [ ] **Use** list comprehensions for clarity when appropriate
- [ ] **Pair** lists with sets for fast membership checks when needed
- [ ] **Handle** edge cases (empty lists, out-of-range indices)
- [ ] **Choose** appropriate methods for performance (append vs insert)

### Real-World Application

- [ ] **Implement** appointment scheduling with lists
- [ ] **Manage** ordered sequences in healthcare contexts
- [ ] **Validate** data using list operations
- [ ] **Optimize** list operations for larger datasets
- [ ] **Debug** common list-related errors (IndexError, ValueError)

---

## Assessment Criteria

### Exercises (Pass: 7/7 exercises with all tests passing)
- Successfully complete all 7 concept drills
- All test cases pass without modification
- Code follows Python conventions

### App Lab 1 (Pass: 80% or higher)
- **Functionality (40%)**: All tasks work as specified
- **Code Quality (30%)**: Clean, readable, follows best practices
- **Testing (30%)**: Edge cases handled, validation present

---

## Next Steps

After mastering lists:
1. **Move to Unit 2: Dictionaries** for key-value data structures
2. **Explore Unit 3: Sets** for uniqueness and set operations
3. **Study Unit 4: Tuples** for immutable sequences
4. **Apply** all collection types in integrated labs

---

## Common Pitfalls to Avoid

✅ **Do**: Build new lists when filtering during iteration  
❌ **Don't**: Modify lists while iterating (causes skipped elements)

✅ **Do**: Use list comprehensions for simple transformations  
❌ **Don't**: Overuse comprehensions for complex multi-step logic

✅ **Do**: Check if list is empty before accessing first/last  
❌ **Don't**: Assume lists always have elements

✅ **Do**: Use sorted() to create new sorted list  
❌ **Don't**: Use sort() if you need to keep original order

---

## Self-Assessment Questions

Before moving to the next unit, can you:

1. Write a list comprehension that filters and transforms in one line?
2. Explain why `list.remove()` during iteration is problematic?
3. Choose between append(), insert(), and extend() for a given scenario?
4. Handle empty list edge cases in your functions?
5. Estimate time complexity of your list operations?

If you answered "yes" to all, you're ready to proceed! 🎉
