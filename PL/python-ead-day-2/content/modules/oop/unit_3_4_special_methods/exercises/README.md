# Unit 3.4: Special Methods (Dunder Methods) - Exercises

## Overview

This unit contains 12 concept-focused exercises covering Python's special methods (dunder methods). Exercises progress from basic string representation to advanced callable objects and comparison protocols.

**File**: `unit_3_4_special_methods_exercises.py`

---

## Exercise List

### Exercise 1: Basic `__str__` Method
**Objective**: Implement a user-friendly string representation

**Description**: Create a class with a `__str__` method that returns a formatted string.

**Inputs/Outputs**:
- Input: Class with `name` and `value` attributes
- Output: `str(obj)` returns `"Name: {name}, Value: {value}"`

**Requirements**:
- Create class `Item` with `__init__(self, name, value)`
- Implement `__str__` returning formatted string
- String should be human-readable

**Hints**:
1. **Hint 1 (Conceptual)**: `__str__` is called by `print()` and `str()`. It should return a string.
2. **Hint 2 (Directional)**: Use f-strings: `return f"Name: {self.name}, Value: {self.value}"`
3. **See Solution**: Check the solution file.

---

### Exercise 2: Basic `__repr__` Method
**Objective**: Implement a developer-friendly representation

**Description**: Create a class with `__repr__` that outputs a string suitable for debugging.

**Inputs/Outputs**:
- Input: Class with `id` and `status` attributes
- Output: `repr(obj)` returns `"Record(id='123', status='active')"`

**Requirements**:
- Create class `Record` with `__init__(self, id, status)`
- Implement `__repr__` returning eval()-able string
- Format: `ClassName(arg1='val1', arg2='val2')`

**Hints**:
1. **Hint 1**: `__repr__` should ideally return a string that could recreate the object.
2. **Hint 2**: Use `f"Record(id='{self.id}', status='{self.status}')"`.
3. **See Solution**: Check the solution file.

---

### Exercise 3: `__str__` and `__repr__` Together
**Objective**: Implement both methods correctly

**Description**: Create a class with distinct `__str__` (user-friendly) and `__repr__` (debug-friendly) outputs.

**Inputs/Outputs**:
- `str(obj)`: `"Product: Laptop ($999.99)"`
- `repr(obj)`: `"Product('SKU001', 'Laptop', 999.99)"`

**Requirements**:
- Create class `Product` with `sku`, `name`, `price`
- `__str__`: Clean display format
- `__repr__`: Constructor-style format

**Hints**:
1. **Hint 1**: `print()` uses `__str__`; the REPL uses `__repr__`.
2. **Hint 2**: Keep `__str__` simple; make `__repr__` detailed.
3. **See Solution**: Check the solution file.

---

### Exercise 4: `__len__` Method
**Objective**: Make an object work with `len()`

**Description**: Create a custom container that supports `len()`.

**Inputs/Outputs**:
- Input: Container with internal list
- Output: `len(container)` returns count of items

**Requirements**:
- Create class `Playlist` with `_songs` list
- Implement `add(song)` method
- Implement `__len__` returning song count

**Hints**:
1. **Hint 1**: `len(obj)` calls `obj.__len__()`.
2. **Hint 2**: Return `len(self._songs)` from `__len__`.
3. **See Solution**: Check the solution file.

---

### Exercise 5: `__getitem__` Method
**Objective**: Enable index access with `[]`

**Description**: Create a class that supports `obj[index]` syntax.

**Inputs/Outputs**:
- Input: `collection[0]`, `collection[1]`
- Output: Returns item at that index

**Requirements**:
- Create class `TaskList` with `_tasks` list
- Implement `__getitem__(self, index)`
- Should support positive and negative indices

**Hints**:
1. **Hint 1**: `obj[i]` calls `obj.__getitem__(i)`.
2. **Hint 2**: Simply return `self._tasks[index]`.
3. **See Solution**: Check the solution file.

---

### Exercise 6: `__setitem__` Method
**Objective**: Enable index assignment with `[]`

**Description**: Create a class that supports `obj[index] = value` syntax.

**Inputs/Outputs**:
- Input: `grid[0] = "X"`
- Output: Updates internal storage at index

**Requirements**:
- Create class `Grid` with `_cells` list (initialize with 9 `None` values)
- Implement `__getitem__` and `__setitem__`
- Support reading and writing cells

**Hints**:
1. **Hint 1**: `obj[i] = v` calls `obj.__setitem__(i, v)`.
2. **Hint 2**: In `__setitem__`, do `self._cells[index] = value`.
3. **See Solution**: Check the solution file.

---

### Exercise 7: `__contains__` Method
**Objective**: Enable `in` operator

**Description**: Create a class that supports `item in container` syntax.

**Inputs/Outputs**:
- Input: `"apple" in basket`
- Output: `True` or `False`

**Requirements**:
- Create class `Basket` with `_items` list
- Implement `add(item)` method
- Implement `__contains__(self, item)`

**Hints**:
1. **Hint 1**: `x in obj` calls `obj.__contains__(x)`.
2. **Hint 2**: Return `item in self._items`.
3. **See Solution**: Check the solution file.

---

### Exercise 8: `__eq__` Method
**Objective**: Define equality comparison

**Description**: Create a class where `==` compares by a specific attribute, not memory address.

**Inputs/Outputs**:
- `obj1 == obj2`: `True` if IDs match, else `False`

**Requirements**:
- Create class `Entity` with `entity_id`
- Implement `__eq__` comparing `entity_id`
- Return `NotImplemented` for non-Entity types

**Hints**:
1. **Hint 1**: `a == b` calls `a.__eq__(b)`.
2. **Hint 2**: Check `isinstance(other, Entity)` first; return `NotImplemented` if not.
3. **See Solution**: Check the solution file.

---

### Exercise 9: `__lt__` for Sorting
**Objective**: Enable sorting with `<` comparison

**Description**: Create a class that can be sorted using `sorted()`.

**Inputs/Outputs**:
- Input: List of `Priority` objects
- Output: `sorted(list)` orders by priority value

**Requirements**:
- Create class `Priority` with `level` (int) and `name`
- Implement `__lt__` comparing by `level`
- Lower level = higher priority

**Hints**:
1. **Hint 1**: `sorted()` uses `__lt__` for comparisons.
2. **Hint 2**: `return self.level < other.level`.
3. **See Solution**: Check the solution file.

---

### Exercise 10: `__eq__` and `__hash__` Together
**Objective**: Make objects usable in sets and as dict keys

**Description**: Create a hashable class with custom equality.

**Inputs/Outputs**:
- Objects with same ID are equal and have same hash
- Can be added to sets, used as dict keys

**Requirements**:
- Create class `Tag` with `tag_id` and `label`
- Implement `__eq__` based on `tag_id`
- Implement `__hash__` based on `tag_id`

**Hints**:
1. **Hint 1**: When you define `__eq__`, you must also define `__hash__` for hashability.
2. **Hint 2**: `__hash__` should return `hash(self.tag_id)`.
3. **See Solution**: Check the solution file.

---

### Exercise 11: `__call__` Method
**Objective**: Make an object callable like a function

**Description**: Create a class instance that can be called with `obj()`.

**Inputs/Outputs**:
- `multiplier = Multiplier(3)`
- `multiplier(10)` returns `30`

**Requirements**:
- Create class `Multiplier` with `factor` attribute
- Implement `__call__(self, value)` returning `value * factor`

**Hints**:
1. **Hint 1**: `obj()` calls `obj.__call__()`.
2. **Hint 2**: `return value * self.factor`.
3. **See Solution**: Check the solution file.

---

### Exercise 12: Complete Protocol Implementation
**Objective**: Combine multiple special methods

**Description**: Create a fully-featured collection class with multiple dunder methods.

**Inputs/Outputs**:
- Supports `len()`, `[]`, `in`, iteration, and string representation

**Requirements**:
- Create class `Inventory` with `_items` dict `{name: quantity}`
- `__len__`: Number of unique items
- `__getitem__(name)`: Get quantity by name
- `__setitem__(name, qty)`: Set quantity
- `__contains__(name)`: Check if item exists
- `__iter__`: Iterate over item names
- `__repr__`: Show inventory state

**Hints**:
1. **Hint 1**: Each special method handles one operation.
2. **Hint 2**: `__iter__` should return `iter(self._items)`.
3. **See Solution**: Check the solution file.

---

## How to Use These Exercises

1. Open `unit_3_4_special_methods_exercises.py`
2. Read each exercise's docstring for requirements
3. Implement your solution between the TODO markers
4. Run the file to test: `python unit_3_4_special_methods_exercises.py`
5. All tests should pass when complete

---

## Learning Path

| Exercises | Difficulty | Focus |
|-----------|------------|-------|
| 1-3 | Foundational | String representations (`__str__`, `__repr__`) |
| 4-7 | Intermediate | Collection protocols (`__len__`, `__getitem__`, etc.) |
| 8-10 | Intermediate | Comparison and hashing |
| 11-12 | Advanced | Callable objects and complete protocols |

---

## Success Criteria

- All 12 exercises pass their test cases
- Code follows Python conventions
- Special methods return correct types
- `NotImplemented` used correctly in comparisons
