# Lab 2 (Intermediate): Appointment Scheduling Part 2 - Detailed Solution Guide

## 📋 Lab Overview

**Difficulty**: Intermediate  
**Duration**: 2-3 hours  
**Topics**: `.remove()`, `.sort()`, list filtering, string searching  
**Use Case**: Daily Schedule Organization

---

## 🎯 Learning Objectives

By completing this lab, you will:
- Safely remove items from lists with error handling
- Sort lists in-place using `.sort()`
- Filter lists based on conditions
- Search for items containing specific values
- Work with time-formatted strings

---

## 📖 Problem Statement

The Grace City Hospital receptionist has a chaotic appointment list:
```python
["14:00 - Smith", "09:00 - Doe", "12:00 - Jones", "08:30 - Wilson"]
```

You need to build an organizer that can:
1. **Cancel appointments** - Remove when patients call to cancel
2. **Sort chronologically** - Order by time
3. **Filter morning slots** - Extract appointments before 12:00
4. **Find patients** - Search by name to find their time slot

---

## 🔍 Task Breakdown

### Task 1: Cancel Appointment (10 points)
Remove an appointment safely without crashing if it doesn't exist.

### Task 2: Organize Schedule (15 points)
Sort appointments chronologically using `.sort()`.

### Task 3: Get Morning Shift (20 points)
Filter and return only morning appointments (before 12:00).

### Task 4: Find Patient Slot (15 points)
Search for a patient by name and return their appointment string.

---

## 💡 Concept Review

### Safe Removal Pattern
```python
if item in my_list:
    my_list.remove(item)
```
- Always check existence before removing
- Prevents `ValueError` exceptions
- Returns boolean to indicate success

### In-Place Sorting
```python
my_list.sort()  # Modifies the list directly
```
- **Important**: `.sort()` returns `None`
- Don't do: `new_list = old_list.sort()`  # new_list will be None!
- For a copy: `new_list = sorted(old_list)`

### String Comparison for Times
```python
"09:00" < "12:00"  # True (alphabetical comparison works for HH:MM format)
```
- ISO time format (HH:MM) sorts correctly alphabetically
- "08:00" < "09:00" < "10:00" < "12:00" < "14:00"

---

## 🛠️ Step-by-Step Solutions

## Task 1: Cancel Appointment

### The Challenge
Remove an appointment without crashing if it doesn't exist.

### Solution Approach
```python
def cancel_appointment(schedule, appointment_string):
    """Remove an appointment from the schedule."""
    if appointment_string in schedule:
        schedule.remove(appointment_string)
        return True
    return False
```

### Detailed Explanation

**Step 1: Check if appointment exists**
```python
if appointment_string in schedule:
```
- The `in` operator searches the entire list
- Returns `True` if found, `False` otherwise
- Time complexity: O(n) - must check each item

**Step 2: Remove if found**
```python
    schedule.remove(appointment_string)
    return True
```
- `.remove()` deletes the first matching item
- Return `True` to indicate successful cancellation
- List is modified in-place

**Step 3: Handle not found case**
```python
return False
```
- If appointment doesn't exist, return `False`
- No error is raised
- Caller knows the cancellation failed

### Example Usage
```python
schedule = ["09:00 - Doe", "14:00 - Smith"]

# Successful cancellation
result = cancel_appointment(schedule, "14:00 - Smith")
# result = True
# schedule = ["09:00 - Doe"]

# Failed cancellation (not found)
result = cancel_appointment(schedule, "10:00 - Jones")
# result = False
# schedule = ["09:00 - Doe"]  # Unchanged
```

### Why This Approach?
✅ **Safe**: Never crashes  
✅ **Informative**: Returns success/failure status  
✅ **Clean**: Simple and readable  

### Alternative Approaches

**Using try-except**:
```python
def cancel_appointment(schedule, appointment_string):
    try:
        schedule.remove(appointment_string)
        return True
    except ValueError:
        return False
```
**Pros**: More Pythonic (EAFP - Easier to Ask Forgiveness than Permission)  
**Cons**: Slightly slower when item doesn't exist

---

## Task 2: Organize Schedule

### The Challenge
Sort appointments chronologically.

### Solution Approach
```python
def organize_schedule(schedule):
    """Sort the schedule chronologically in-place."""
    schedule.sort()
    return schedule
```

### Detailed Explanation

**Why `.sort()` works for times**:
```python
schedule = ["14:00 - Smith", "09:00 - Doe", "12:00 - Jones"]
schedule.sort()
# Result: ["09:00 - Doe", "12:00 - Jones", "14:00 - Smith"]
```

**How string sorting works**:
1. Python compares strings character by character
2. "0" < "1" < "2" ... < "9"
3. "09:00" < "12:00" < "14:00" (lexicographic order)
4. Since we use HH:MM format, alphabetical = chronological!

**Important: `.sort()` returns None**
```python
# ❌ WRONG
sorted_schedule = schedule.sort()  # sorted_schedule is None!

# ✅ CORRECT
schedule.sort()  # Modifies in-place
# Now use 'schedule' directly

# OR use sorted() for a copy
sorted_schedule = sorted(schedule)  # Original unchanged
```

### Example Usage
```python
schedule = ["14:00 - Smith", "09:00 - Doe", "11:30 - Wilson", "08:00 - Brown"]

organize_schedule(schedule)

# schedule is now:
# ["08:00 - Brown", "09:00 - Doe", "11:30 - Wilson", "14:00 - Smith"]
```

### Edge Cases

**Empty list**:
```python
schedule = []
organize_schedule(schedule)
# Result: []  # No error
```

**Single item**:
```python
schedule = ["10:00 - Doe"]
organize_schedule(schedule)
# Result: ["10:00 - Doe"]  # Already sorted
```

**Already sorted**:
```python
schedule = ["09:00 - A", "10:00 - B"]
organize_schedule(schedule)
# Result: ["09:00 - A", "10:00 - B"]  # No change needed
```

---

## Task 3: Get Morning Appointments

### The Challenge
Extract only appointments before 12:00 PM.

### Solution Approach
```python
def get_morning_appointments(schedule):
    """Get all appointments before 12:00."""
    morning = []
    for slot in schedule:
        # Extract time portion and compare
        if slot[:5] < "12:00":
            morning.append(slot)
    return morning
```

### Detailed Explanation

**Step 1: Create empty result list**
```python
morning = []
```
- Will hold filtered appointments
- Starts empty, grows as we find matches

**Step 2: Iterate through schedule**
```python
for slot in schedule:
```
- Check each appointment one by one
- `slot` is a string like "09:00 - Doe"

**Step 3: Extract and compare time**
```python
if slot[:5] < "12:00":
```
- `slot[:5]` extracts first 5 characters: "09:00"
- String comparison: "09:00" < "12:00" is `True`
- "14:00" < "12:00" is `False`

**Step 4: Add matching appointments**
```python
    morning.append(slot)
```
- If time is before 12:00, add to result
- Original list is not modified

**Step 5: Return filtered list**
```python
return morning
```
- New list containing only morning appointments

### Example Usage
```python
schedule = [
    "08:00 - Early",
    "09:00 - Morning",
    "12:00 - Noon",
    "14:00 - Afternoon"
]

morning = get_morning_appointments(schedule)
# morning = ["08:00 - Early", "09:00 - Morning"]
# Note: "12:00 - Noon" is NOT included (strictly before 12:00)
```

### Alternative Approaches

**List Comprehension** (more Pythonic):
```python
def get_morning_appointments(schedule):
    return [slot for slot in schedule if slot[:5] < "12:00"]
```
**Pros**: More concise, faster  
**Cons**: Less readable for beginners

**Using filter()**:
```python
def get_morning_appointments(schedule):
    return list(filter(lambda slot: slot[:5] < "12:00", schedule))
```
**Pros**: Functional programming style  
**Cons**: Less readable, overkill for simple task

---

## Task 4: Find Patient Slot

### The Challenge
Search for a patient by name and return their appointment time.

### Solution Approach
```python
def find_patient_slot(schedule, patient_name):
    """Find appointment string for a patient name."""
    for slot in schedule:
        if patient_name in slot:
            return slot
    return None
```

### Detailed Explanation

**Step 1: Iterate through appointments**
```python
for slot in schedule:
```
- Check each appointment string
- `slot` might be "09:00 - John Smith"

**Step 2: Check if name is in string**
```python
if patient_name in slot:
```
- `in` operator checks substring
- "Smith" in "09:00 - John Smith" is `True`
- Case-sensitive!

**Step 3: Return first match**
```python
    return slot
```
- Immediately return when found
- Exits the function (no need for `break`)
- Returns the full appointment string

**Step 4: Handle not found**
```python
return None
```
- If loop completes without finding a match
- `None` indicates "not found"
- Caller can check: `if result is None:`

### Example Usage
```python
schedule = [
    "09:00 - John Doe",
    "10:00 - Jane Smith",
    "14:00 - Bob Smith"
]

# Find by last name
slot = find_patient_slot(schedule, "Smith")
# slot = "10:00 - Jane Smith"  # Returns FIRST match

# Find by full name
slot = find_patient_slot(schedule, "Bob Smith")
# slot = "14:00 - Bob Smith"

# Not found
slot = find_patient_slot(schedule, "Wilson")
# slot = None
```

### Edge Cases

**Multiple matches**:
```python
schedule = ["09:00 - Smith", "14:00 - Smith"]
slot = find_patient_slot(schedule, "Smith")
# Returns: "09:00 - Smith"  # First match only
```

**Partial name match**:
```python
schedule = ["09:00 - John Smith"]
slot = find_patient_slot(schedule, "Smi")
# Returns: "09:00 - John Smith"  # Substring match works
```

**Case sensitivity**:
```python
schedule = ["09:00 - Smith"]
slot = find_patient_slot(schedule, "smith")  # lowercase
# Returns: None  # No match (case-sensitive)
```

### Improved Version (Case-Insensitive)
```python
def find_patient_slot(schedule, patient_name):
    """Find appointment (case-insensitive)."""
    name_lower = patient_name.lower()
    for slot in schedule:
        if name_lower in slot.lower():
            return slot
    return None
```

---

## ✅ Complete Solution

```python
"""
Lab 2 (Intermediate): Appointment Scheduling - Part 2
Complete Solution
"""

def cancel_appointment(schedule, appointment_string):
    """
    Remove an appointment from the schedule.
    
    Args:
        schedule: List of appointment strings
        appointment_string: The appointment to remove
    
    Returns:
        True if removed, False if not found
    """
    if appointment_string in schedule:
        schedule.remove(appointment_string)
        return True
    return False


def organize_schedule(schedule):
    """
    Sort the schedule chronologically in-place.
    
    Args:
        schedule: List of appointment strings (HH:MM - Name format)
    
    Returns:
        The sorted schedule (same list, modified in-place)
    """
    schedule.sort()
    return schedule


def get_morning_appointments(schedule):
    """
    Get all appointments before 12:00.
    
    Args:
        schedule: List of appointment strings
    
    Returns:
        New list containing only morning appointments
    """
    morning = []
    for slot in schedule:
        # Extract time portion (first 5 chars) and compare
        if slot[:5] < "12:00":
            morning.append(slot)
    return morning


def find_patient_slot(schedule, patient_name):
    """
    Find appointment string for a patient name.
    
    Args:
        schedule: List of appointment strings
        patient_name: Name to search for (substring match)
    
    Returns:
        Full appointment string if found, None otherwise
    """
    for slot in schedule:
        if patient_name in slot:
            return slot
    return None


# Example usage
if __name__ == "__main__":
    # Create a messy schedule
    schedule = [
        "14:00 - Smith",
        "09:00 - Doe",
        "12:00 - Jones",
        "08:30 - Wilson",
        "16:00 - Brown"
    ]
    
    print("Original schedule:")
    for apt in schedule:
        print(f"  {apt}")
    
    # Cancel an appointment
    cancelled = cancel_appointment(schedule, "12:00 - Jones")
    print(f"\nCancelled Jones: {cancelled}")
    
    # Organize the schedule
    organize_schedule(schedule)
    print("\nOrganized schedule:")
    for apt in schedule:
        print(f"  {apt}")
    
    # Get morning appointments
    morning = get_morning_appointments(schedule)
    print("\nMorning appointments:")
    for apt in morning:
        print(f"  {apt}")
    
    # Find a patient
    smith_slot = find_patient_slot(schedule, "Smith")
    print(f"\nSmith's appointment: {smith_slot}")
```

**Output**:
```
Original schedule:
  14:00 - Smith
  09:00 - Doe
  12:00 - Jones
  08:30 - Wilson
  16:00 - Brown

Cancelled Jones: True

Organized schedule:
  08:30 - Wilson
  09:00 - Doe
  14:00 - Smith
  16:00 - Brown

Morning appointments:
  08:30 - Wilson
  09:00 - Doe

Smith's appointment: 14:00 - Smith
```

---

## 🎓 Key Takeaways

### 1. Safe Removal
- Always check `if item in list` before `.remove()`
- Return boolean to indicate success/failure
- Prevents crashes from removing non-existent items

### 2. In-Place vs. Copy
- `.sort()` modifies the list and returns `None`
- `sorted()` creates a new sorted list
- Choose based on whether you need the original

### 3. String Slicing for Parsing
- `slot[:5]` extracts time portion
- Works because format is consistent
- Faster than splitting strings

### 4. Early Return Pattern
- Return immediately when found
- No need for `break` or flag variables
- Makes code cleaner and more efficient

---

## 🚫 Common Mistakes

### Mistake 1: Assigning `.sort()` Result
```python
# ❌ WRONG
sorted_schedule = schedule.sort()
print(sorted_schedule)  # Prints: None

# ✅ CORRECT
schedule.sort()
print(schedule)  # Prints sorted list
```

### Mistake 2: Removing While Iterating
```python
# ❌ WRONG - Skips items!
for slot in schedule:
    if "Smith" in slot:
        schedule.remove(slot)  # Modifying while iterating

# ✅ CORRECT - Filter to new list
schedule = [s for s in schedule if "Smith" not in s]
```

### Mistake 3: Forgetting String Slicing
```python
# ❌ WRONG - Compares full strings
if slot < "12:00":  # "09:00 - Doe" < "12:00" is False!

# ✅ CORRECT - Extract time first
if slot[:5] < "12:00":  # "09:00" < "12:00" is True
```

### Mistake 4: Case Sensitivity
```python
schedule = ["09:00 - Smith"]

# ❌ WRONG - Won't find it
find_patient_slot(schedule, "smith")  # Returns None

# ✅ CORRECT - Match case or use .lower()
find_patient_slot(schedule, "Smith")  # Returns appointment
```

---

## 📚 Performance Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| `cancel_appointment` | O(n) | O(1) |
| `organize_schedule` | O(n log n) | O(1) |
| `get_morning_appointments` | O(n) | O(n) |
| `find_patient_slot` | O(n) | O(1) |

**Why these complexities?**
- **Removal**: Must search entire list
- **Sorting**: Python uses Timsort (efficient hybrid)
- **Filtering**: Must check every item, creates new list
- **Searching**: Linear search through list

---

## ✨ Congratulations!

You've mastered intermediate list operations! You can now:
- ✅ Safely modify lists without crashes
- ✅ Sort data chronologically
- ✅ Filter lists based on conditions
- ✅ Search for specific items

**Next Lab**: Lab 3 - Advanced List Processing with Comprehensions

---

*Last Updated: 2026-01-06*  
*Grace City Hospital Training Program*
