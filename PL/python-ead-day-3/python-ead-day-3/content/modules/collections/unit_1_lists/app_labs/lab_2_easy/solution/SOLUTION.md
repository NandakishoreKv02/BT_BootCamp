# Lab 2: Dynamic Slot Management - Detailed Solution Guide

## 📋 Lab Overview

**Difficulty**: Easy  
**Duration**: 1 hour  
**Topics**: `.remove()`, `.insert()`, `.pop()`  
**Use Case**: Dynamic Appointment Queue Management

---

## 🎯 Learning Objectives

By completing this lab, you will:
- Master removing items from lists using `.remove()`
- Learn to insert items at specific positions using `.insert()`
- Understand how `.pop()` removes and returns items
- Handle real-world queue management scenarios

---

## 📖 Problem Statement

The Grace City Hospital clinic needs to handle dynamic changes to their patient queue:
- **Cancellations**: Patients might cancel their appointments
- **Emergencies**: Critical patients need to be prioritized at the front
- **Queue Processing**: Serve patients one at a time in order

You need to implement a system that can:
1. Insert emergency patients at the front of the line
2. Remove patients who cancel
3. Process (serve) patients from the front of the queue

---

## 🔍 Task Breakdown

### Task 1: Insert and Serve
**Points**: 100  
**Difficulty**: Easy

#### Requirements:
1. Start with a list `slots = ["Patient A", "Patient B"]`
2. Insert "EMERGENCY" at the beginning (index 0)
3. Remove "Patient A" from the list (cancellation)
4. Use `pop(0)` to remove and return the first person in line, storing them in `current_patient`

---

## 💡 Concept Review

### The `.insert()` Method
```python
my_list.insert(index, item)
```
- Inserts `item` at position `index`
- All items at or after that position shift right
- Does NOT replace existing items
- Time complexity: O(n) - slower than append

**Example**:
```python
queue = ["A", "B", "C"]
queue.insert(0, "URGENT")
# Result: ["URGENT", "A", "B", "C"]
```

### The `.remove()` Method
```python
my_list.remove(value)
```
- Removes the **first occurrence** of `value`
- Raises `ValueError` if value not found
- Modifies list in-place
- Time complexity: O(n)

**Example**:
```python
queue = ["A", "B", "A", "C"]
queue.remove("A")
# Result: ["B", "A", "C"]  # Only first "A" removed
```

### The `.pop()` Method
```python
item = my_list.pop(index)
```
- Removes and **returns** the item at `index`
- If no index given, removes last item
- Raises `IndexError` if index out of range
- Time complexity: O(1) for last item, O(n) for first item

**Example**:
```python
queue = ["A", "B", "C"]
first = queue.pop(0)
# first = "A"
# queue = ["B", "C"]
```

---

## 🛠️ Step-by-Step Solution

### Step 1: Initialize the Queue
```python
slots = ["Patient A", "Patient B"]
```

**Explanation**:
- We start with 2 patients already in the queue
- "Patient A" is at index 0 (first in line)
- "Patient B" is at index 1 (second in line)

**Visual representation**:
```
Index:  0            1
       ┌────────────┬────────────┐
slots: │ Patient A  │ Patient B  │
       └────────────┴────────────┘
```

---

### Step 2: Insert Emergency Patient at Front
```python
slots.insert(0, "EMERGENCY")
```

**Explanation**:
- `.insert(0, "EMERGENCY")` places "EMERGENCY" at index 0
- All existing items shift one position to the right
- "Patient A" moves from index 0 to index 1
- "Patient B" moves from index 1 to index 2

**Before**:
```
Index:  0            1
       ┌────────────┬────────────┐
slots: │ Patient A  │ Patient B  │
       └────────────┴────────────┘
```

**After**:
```
Index:  0            1            2
       ┌────────────┬────────────┬────────────┐
slots: │ EMERGENCY  │ Patient A  │ Patient B  │
       └────────────┴────────────┴────────────┘
```

**Why index 0?**
- Index 0 is the front of the queue
- Emergency patients need immediate attention
- They "cut" to the front of the line

---

### Step 3: Remove Cancelled Patient
```python
slots.remove("Patient A")
```

**Explanation**:
- Patient A calls to cancel their appointment
- `.remove("Patient A")` searches for the first occurrence
- Finds "Patient A" at index 1
- Removes it and shifts remaining items left

**Before**:
```
Index:  0            1            2
       ┌────────────┬────────────┬────────────┐
slots: │ EMERGENCY  │ Patient A  │ Patient B  │
       └────────────┴────────────┴────────────┘
```

**After**:
```
Index:  0            1
       ┌────────────┬────────────┐
slots: │ EMERGENCY  │ Patient B  │
       └────────────┴────────────┘
```

**Important notes**:
- `.remove()` only removes the FIRST match
- If "Patient A" appeared multiple times, only the first would be removed
- If "Patient A" wasn't in the list, you'd get a `ValueError`

---

### Step 4: Serve the Next Patient
```python
current_patient = slots.pop(0)
```

**Explanation**:
- `.pop(0)` removes the item at index 0
- Returns the removed value ("EMERGENCY")
- Stores it in the variable `current_patient`
- Remaining items shift left

**Before**:
```
Index:  0            1
       ┌────────────┬────────────┐
slots: │ EMERGENCY  │ Patient B  │
       └────────────┴────────────┘
```

**After**:
```
current_patient = "EMERGENCY"

Index:  0
       ┌────────────┐
slots: │ Patient B  │
       └────────────┘
```

**Why use `.pop()` instead of `.remove()`?**
- `.pop()` gives us the value back (we need to know who we're serving)
- `.remove()` just deletes without returning
- `.pop(0)` is perfect for queue operations (FIFO - First In, First Out)

---

### Step 5: Display Results
```python
print(f"Serving: {current_patient}")
print(f"Remaining: {slots}")
```

**Explanation**:
- Shows who is currently being served
- Shows who is still waiting
- Uses f-strings for clean formatting

**Output**:
```
Serving: EMERGENCY
Remaining: ['Patient B']
```

---

## ✅ Complete Solution

```python
"""
Lab 2: Dynamic Slot Management
Complete Solution
"""

# Step 1: Initialize the queue with 2 patients
slots = ["Patient A", "Patient B"]

# Step 2: Emergency patient arrives - insert at front (index 0)
slots.insert(0, "EMERGENCY")
# slots is now: ["EMERGENCY", "Patient A", "Patient B"]

# Step 3: Patient A cancels - remove them from the queue
slots.remove("Patient A")
# slots is now: ["EMERGENCY", "Patient B"]

# Step 4: Serve the next patient (remove from front and get their name)
current_patient = slots.pop(0)
# current_patient = "EMERGENCY"
# slots is now: ["Patient B"]

# Step 5: Display the results
print(f"Serving: {current_patient}")
print(f"Remaining: {slots}")
```

**Expected Output**:
```
Serving: EMERGENCY
Remaining: ['Patient B']
```

---

## 🧪 Testing Your Solution

### Manual Testing
Run your code and verify:
1. ✅ "EMERGENCY" is served first
2. ✅ "Patient A" is not in the remaining list
3. ✅ Only "Patient B" remains waiting

### Understanding the Flow
```python
# Initial state
slots = ["Patient A", "Patient B"]

# After insert(0, "EMERGENCY")
slots = ["EMERGENCY", "Patient A", "Patient B"]

# After remove("Patient A")
slots = ["EMERGENCY", "Patient B"]

# After pop(0)
current_patient = "EMERGENCY"
slots = ["Patient B"]
```

---

## 🎓 Key Takeaways

### 1. `.insert(index, item)` - Precise Placement
- Allows insertion at any position
- Index 0 = front of list
- Index len(list) = end of list (same as append)
- All items shift right to make room

### 2. `.remove(value)` - Remove by Value
- Searches for the value, then removes it
- Only removes the FIRST occurrence
- Raises error if value not found
- Use when you know the value but not the position

### 3. `.pop(index)` - Remove and Return
- Removes item AND gives it back to you
- Perfect for queue operations
- `.pop()` without index removes last item
- `.pop(0)` removes first item (queue behavior)

### 4. List Shifting
- Inserting/removing from the middle or front is expensive
- All subsequent items must shift positions
- For large lists, consider using `collections.deque` for better performance

---

## 🚫 Common Mistakes

### Mistake 1: Confusing `.insert()` with Replacement
```python
# ❌ WRONG THINKING
slots = ["A", "B"]
slots.insert(0, "C")
# Some students think this replaces "A" with "C"

# ✅ CORRECT - It inserts, shifting everything right
# Result: ["C", "A", "B"]
```

### Mistake 2: Using `.remove()` with Index
```python
# ❌ WRONG - remove() takes a VALUE, not an index
slots.remove(0)  # Tries to remove the value 0, not index 0

# ✅ CORRECT - Use pop() for index-based removal
slots.pop(0)
```

### Mistake 3: Forgetting `.pop()` Returns a Value
```python
# ❌ WRONG - Discarding the returned value
slots.pop(0)
print(current_patient)  # NameError: current_patient not defined

# ✅ CORRECT - Capture the return value
current_patient = slots.pop(0)
print(current_patient)
```

### Mistake 4: Removing Non-Existent Items
```python
slots = ["A", "B"]

# ❌ WRONG - Will raise ValueError
slots.remove("C")  # ValueError: list.remove(x): x not in list

# ✅ CORRECT - Check first
if "C" in slots:
    slots.remove("C")
```

### Mistake 5: Wrong Index for `.pop()`
```python
slots = ["A", "B", "C"]

# ❌ WRONG - pop(1) removes the SECOND item, not the first
first = slots.pop(1)  # Removes "B", not "A"

# ✅ CORRECT - Use index 0 for the first item
first = slots.pop(0)  # Removes "A"
```

---

## 🔄 Alternative Approaches

### Approach 1: Using Slicing for Removal
```python
# Instead of .remove("Patient A")
slots = ["EMERGENCY", "Patient A", "Patient B"]
slots = [p for p in slots if p != "Patient A"]
# Result: ["EMERGENCY", "Patient B"]
```
**Pros**: More flexible (can remove all occurrences)  
**Cons**: Creates a new list (less memory efficient)

### Approach 2: Using `del` for Index-Based Removal
```python
# Instead of .pop(0)
del slots[0]  # Removes first item but doesn't return it
```
**Pros**: Slightly faster  
**Cons**: Doesn't give you the value back

### Approach 3: Using `collections.deque` for Better Performance
```python
from collections import deque

slots = deque(["Patient A", "Patient B"])
slots.appendleft("EMERGENCY")  # Faster than insert(0)
slots.remove("Patient A")
current_patient = slots.popleft()  # Faster than pop(0)
```
**Pros**: O(1) for front operations  
**Cons**: More complex, overkill for small lists

---

## 🏥 Real-World Application

### Emergency Department Triage System
```python
class EmergencyQueue:
    def __init__(self):
        self.queue = []
    
    def add_patient(self, name, priority):
        """Add patient based on priority level"""
        if priority == "CRITICAL":
            self.queue.insert(0, name)  # Front of line
        elif priority == "URGENT":
            # Insert after critical but before routine
            critical_count = sum(1 for p in self.queue if p.startswith("CRITICAL"))
            self.queue.insert(critical_count, name)
        else:
            self.queue.append(name)  # End of line
    
    def cancel_appointment(self, name):
        """Remove patient who cancels"""
        if name in self.queue:
            self.queue.remove(name)
            return True
        return False
    
    def serve_next(self):
        """Serve the next patient"""
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def get_waiting_count(self):
        """Get number of patients waiting"""
        return len(self.queue)

# Usage
ed = EmergencyQueue()
ed.add_patient("John Doe", "ROUTINE")
ed.add_patient("Jane Smith", "CRITICAL")
ed.add_patient("Bob Wilson", "URGENT")

print(f"Next patient: {ed.serve_next()}")  # Jane Smith (CRITICAL)
print(f"Patients waiting: {ed.get_waiting_count()}")  # 2
```

---

## 📚 Method Comparison Table

| Method | Purpose | Returns Value? | Modifies List? | Time Complexity |
|--------|---------|----------------|----------------|-----------------|
| `.append(x)` | Add to end | No | Yes | O(1) |
| `.insert(i, x)` | Add at index | No | Yes | O(n) |
| `.remove(x)` | Remove by value | No | Yes | O(n) |
| `.pop(i)` | Remove by index | Yes | Yes | O(n) for i=0, O(1) for i=-1 |
| `del list[i]` | Remove by index | No | Yes | O(n) |

---

## 📈 Performance Considerations

### When to Use Each Method

**Use `.insert(0, x)` when:**
- You need to add to the front occasionally
- List is small (< 1000 items)
- Code clarity is more important than speed

**Use `collections.deque` when:**
- Frequent front/back operations
- Large lists (> 1000 items)
- Performance is critical

**Use `.remove(x)` when:**
- You know the value but not the position
- You only want to remove the first occurrence
- You're okay with potential ValueError

**Use `.pop(i)` when:**
- You need the removed value
- You know the index
- You're implementing queue/stack behavior

---

## 🎯 Practice Exercises

### Exercise 1: Multiple Emergencies
Modify the code to handle 2 emergency patients:
```python
slots = ["Patient A", "Patient B", "Patient C"]
# Insert "EMERGENCY 1" at front
# Insert "EMERGENCY 2" at front (should be before EMERGENCY 1)
# What's the final order?
```

<details>
<summary>Solution</summary>

```python
slots = ["Patient A", "Patient B", "Patient C"]
slots.insert(0, "EMERGENCY 1")
# slots: ["EMERGENCY 1", "Patient A", "Patient B", "Patient C"]

slots.insert(0, "EMERGENCY 2")
# slots: ["EMERGENCY 2", "EMERGENCY 1", "Patient A", "Patient B", "Patient C"]
```
</details>

### Exercise 2: Remove All Occurrences
Remove ALL occurrences of "Patient A" from the list:
```python
slots = ["Patient A", "Patient B", "Patient A", "Patient C", "Patient A"]
# Remove all "Patient A" entries
```

<details>
<summary>Solution</summary>

```python
# Method 1: Loop until not found
while "Patient A" in slots:
    slots.remove("Patient A")

# Method 2: List comprehension
slots = [p for p in slots if p != "Patient A"]
```
</details>

### Exercise 3: Safe Pop
Write code that safely pops from an empty list:
```python
slots = []
# Pop without crashing if empty
```

<details>
<summary>Solution</summary>

```python
if slots:
    current = slots.pop(0)
else:
    current = None
    print("Queue is empty")

# Or using try-except
try:
    current = slots.pop(0)
except IndexError:
    current = None
    print("Queue is empty")
```
</details>

---

## ✨ Congratulations!

You've mastered dynamic list manipulation! You can now:
- ✅ Insert items at any position
- ✅ Remove items by value
- ✅ Pop items and use their values
- ✅ Handle real-world queue scenarios

**Next Lab**: Lab 3 - List Indexing and Slicing

---

*Last Updated: 2026-01-06*  
*Grace City Hospital Training Program*
