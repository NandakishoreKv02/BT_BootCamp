---
title: Special Methods (Dunder Methods)
type: knowledge
module: oop
unit: unit_3_4_special_methods
order: 4
difficulty: intermediate
tags:
  subtopics:
    - str-repr
    - len-getitem-setitem
    - comparison-methods
    - callable-objects
---

# Unit 3.4: Special Methods (Dunder Methods)

## 1. What

**Special methods** (also called **dunder methods** or **magic methods**) are Python methods with double underscores before and after their names (e.g., `__init__`, `__str__`, `__len__`). They allow your custom classes to integrate seamlessly with Python's built-in operations and syntax.

### What Problem Do They Solve?

Without special methods, your objects would be opaque to Python's built-in functions and operators. You could not:
- Print a meaningful representation of your object with `print()`
- Use `len()` on your custom collection
- Compare two objects with `==` or `<`
- Iterate over your object with `for` loops
- Use your object as a callable function

### When Would You Use This?

- **Building custom collections**: Implement `__len__`, `__getitem__`, `__setitem__` to make your class behave like a list or dictionary
- **Creating readable output**: Implement `__str__` and `__repr__` for debugging and user display
- **Enabling comparisons**: Implement `__eq__`, `__lt__`, etc. to sort and compare objects
- **Making callable objects**: Implement `__call__` to use instances as functions

### Key Terminology

| Term | Meaning |
|------|---------|
| Dunder | Double underscore (e.g., `__name__`) |
| Magic method | Another name for special methods |
| Protocol | A set of special methods that enable specific behavior |
| Operator overloading | Customizing how operators work with your class |

---

## 2. Example

### Example 1: Basic `__str__` and `__repr__`

```python
class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
    
    def __str__(self):
        """User-friendly string for display."""
        return f"Patient: {self.name} (Age: {self.age})"
    
    def __repr__(self):
        """Developer-friendly string for debugging."""
        return f"Patient('{self.patient_id}', '{self.name}', {self.age})"


patient = Patient("P001", "Alice Smith", 34)
print(patient)       # Output: Patient: Alice Smith (Age: 34)
print(repr(patient)) # Output: Patient('P001', 'Alice Smith', 34)
```

### Example 2: `__len__` and `__getitem__` for Collections

```python
class AppointmentBook:
    def __init__(self):
        self._appointments = []
    
    def add(self, appointment):
        self._appointments.append(appointment)
    
    def __len__(self):
        """Enable len(book)."""
        return len(self._appointments)
    
    def __getitem__(self, index):
        """Enable book[0], book[1], etc."""
        return self._appointments[index]


book = AppointmentBook()
book.add("9:00 AM - Dr. Smith")
book.add("10:30 AM - Dr. Johnson")

print(len(book))    # Output: 2
print(book[0])      # Output: 9:00 AM - Dr. Smith

# Iteration works automatically when __getitem__ is defined
for appt in book:
    print(appt)
# Output:
# 9:00 AM - Dr. Smith
# 10:30 AM - Dr. Johnson
```

### Example 3: Comparison Methods

```python
class VitalReading:
    def __init__(self, timestamp, temperature):
        self.timestamp = timestamp
        self.temperature = temperature
    
    def __eq__(self, other):
        """Enable == comparison."""
        if not isinstance(other, VitalReading):
            return NotImplemented
        return self.timestamp == other.timestamp
    
    def __lt__(self, other):
        """Enable < comparison and sorting."""
        if not isinstance(other, VitalReading):
            return NotImplemented
        return self.timestamp < other.timestamp
    
    def __repr__(self):
        return f"VitalReading({self.timestamp}, {self.temperature})"


readings = [
    VitalReading("10:00", 37.2),
    VitalReading("08:00", 36.8),
    VitalReading("09:00", 37.0),
]

sorted_readings = sorted(readings)
print(sorted_readings)
# Output: [VitalReading(08:00, 36.8), VitalReading(09:00, 37.0), VitalReading(10:00, 37.2)]

print(readings[0] == VitalReading("10:00", 99.9))  # Output: True (same timestamp)
```

### Example 4: `__call__` for Callable Objects

```python
class DosageCalculator:
    def __init__(self, base_dose_mg):
        self.base_dose = base_dose_mg
    
    def __call__(self, weight_kg):
        """Calculate dosage based on patient weight."""
        return self.base_dose * weight_kg
    
    def __repr__(self):
        return f"DosageCalculator(base={self.base_dose}mg)"


calculate_ibuprofen = DosageCalculator(10)  # 10mg per kg

# Use instance like a function
dose = calculate_ibuprofen(70)  # 70kg patient
print(f"Recommended dose: {dose}mg")  # Output: Recommended dose: 700mg

# Still an object with attributes
print(calculate_ibuprofen.base_dose)  # Output: 10
```

### Example 5: `__setitem__` for Mutable Collections

```python
class MedicalRecord:
    def __init__(self):
        self._data = {}
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __setitem__(self, key, value):
        """Enable record['key'] = value syntax."""
        self._data[key] = value
    
    def __contains__(self, key):
        """Enable 'key' in record syntax."""
        return key in self._data


record = MedicalRecord()
record["blood_type"] = "O+"
record["allergies"] = ["Penicillin"]

print(record["blood_type"])        # Output: O+
print("allergies" in record)       # Output: True
```

---

## 3. Explanation

### How Special Methods Work

When you call a built-in function or use an operator, Python looks for the corresponding special method on the object:

```
len(obj)        -->  obj.__len__()
str(obj)        -->  obj.__str__()
obj[key]        -->  obj.__getitem__(key)
obj[key] = val  -->  obj.__setitem__(key, val)
obj == other    -->  obj.__eq__(other)
obj < other     -->  obj.__lt__(other)
obj()           -->  obj.__call__()
```

### Method Resolution

Python follows a specific order when looking for special methods:

1. Check the object's class (not the instance)
2. Check parent classes in MRO (Method Resolution Order)
3. If not found, raise `TypeError` or use default behavior

### Comparison Method Relationships

Python's `functools.total_ordering` decorator can generate missing comparison methods:

| If you define | Python can infer |
|---------------|------------------|
| `__eq__` + `__lt__` | `__le__`, `__gt__`, `__ge__` |
| `__eq__` + `__gt__` | `__ge__`, `__lt__`, `__le__` |

```python
from functools import total_ordering

@total_ordering
class Priority:
    def __init__(self, level):
        self.level = level
    
    def __eq__(self, other):
        return self.level == other.level
    
    def __lt__(self, other):
        return self.level < other.level

# Now <=, >, >= all work automatically
```

### `__str__` vs `__repr__`

| Aspect | `__str__` | `__repr__` |
|--------|-----------|------------|
| Purpose | User-friendly display | Developer debugging |
| Called by | `print()`, `str()` | `repr()`, interactive shell |
| Fallback | Falls back to `__repr__` | No fallback |
| Goal | Human readable | Unambiguous, ideally `eval()`-able |

### Visual: Method Call Flow

```
User Code              Python Internals           Your Class
----------              ----------------           ----------
len(patient_list)  -->  type(patient_list).__len__(patient_list)
                                                   |
                                                   v
                                           def __len__(self):
                                               return len(self._patients)
```

### Performance Characteristics

Special methods have minimal overhead:
- Direct C-level dispatch for built-in types
- One method lookup for custom classes
- No runtime introspection cost

---

## 4. Why

### 1. Pythonic Integration

Special methods let your classes feel like native Python types. Users can work with your objects using familiar syntax (`len()`, `[]`, `in`, etc.) without learning new APIs.

```python
# Without special methods
patient_list.get_count()
patient_list.get_item(0)

# With special methods
len(patient_list)
patient_list[0]
```

### 2. Interoperability with Built-in Functions

Python's rich standard library (sorting, filtering, serialization) works automatically with objects that implement the right protocols:

```python
# sorted() works when __lt__ is defined
sorted_patients = sorted(patients, key=lambda p: p.priority)

# list() works when __iter__ or __getitem__ is defined
patient_list = list(patient_generator)
```

### 3. Clean, Readable Code

Operator overloading reduces boilerplate and makes code self-documenting:

```python
# Verbose
if patient1.equals(patient2) and patient1.is_less_than(patient3):
    process(patient1)

# Pythonic
if patient1 == patient2 and patient1 < patient3:
    process(patient1)
```

### 4. Framework Compatibility

Many Python frameworks (Django ORM, SQLAlchemy, Pydantic) rely on special methods. Implementing them correctly ensures your classes work with these tools.

### 5. Debugging and Logging

A well-implemented `__repr__` makes debugging significantly easier:

```python
# Poor debugging experience
print(patients)  # [<Patient object at 0x...>, <Patient object at 0x...>]

# With __repr__
print(patients)  # [Patient('P001', 'Alice'), Patient('P002', 'Bob')]
```

---

## 5. Advantages & Disadvantages

### Advantages

#### 1. Seamless Language Integration
- Objects work with all built-in functions
- Enables duck typing and polymorphism
- Code reads naturally

```python
# Works with any object that has __len__
def is_empty(container):
    return len(container) == 0
```

#### 2. Reduced Boilerplate
- No need for explicit method calls
- Cleaner, more maintainable code
- Less documentation needed

#### 3. Consistent Behavior
- Users expect `len()` to work the same way everywhere
- Reduces cognitive load
- Follows principle of least surprise

#### 4. Enables Advanced Patterns
- Context managers (`__enter__`, `__exit__`)
- Descriptors (`__get__`, `__set__`)
- Metaclasses (`__new__`, `__init__`)

### Disadvantages

#### 1. Learning Curve
- Many methods to remember
- Subtle differences (e.g., `__str__` vs `__repr__`)
- Protocol requirements not always obvious

#### 2. Hidden Complexity
- Method calls are implicit
- Debugging can be harder when behavior is unexpected
- Workaround: Use explicit method calls during debugging

#### 3. Potential for Misuse
- Overloading operators in non-intuitive ways
- Breaking expected semantics
- Example: Using `+` for something other than addition

```python
# Confusing: What does + mean for patients?
patient1 + patient2  # Bad design
```

#### 4. NotImplemented Complexity
- Must handle `NotImplemented` correctly in comparisons
- Can cause subtle bugs if not done properly

---

## 6. Real-World Use Cases

### Healthcare: Patient Record System

**Problem**: Need to compare, sort, and display patient records consistently across a hospital information system.

**Solution**: Implement comparison and string methods for natural ordering and display.

```python
from functools import total_ordering

@total_ordering
class PatientRecord:
    def __init__(self, mrn, name, priority):
        self.mrn = mrn  # Medical Record Number
        self.name = name
        self.priority = priority  # 1=Critical, 5=Routine
    
    def __eq__(self, other):
        if not isinstance(other, PatientRecord):
            return NotImplemented
        return self.mrn == other.mrn
    
    def __lt__(self, other):
        """Sort by priority (lower = more urgent)."""
        if not isinstance(other, PatientRecord):
            return NotImplemented
        return self.priority < other.priority
    
    def __str__(self):
        return f"{self.name} (MRN: {self.mrn}) - Priority {self.priority}"
    
    def __repr__(self):
        return f"PatientRecord('{self.mrn}', '{self.name}', {self.priority})"


# Usage: Triage queue
queue = [
    PatientRecord("MRN001", "John Smith", 3),
    PatientRecord("MRN002", "Jane Doe", 1),
    PatientRecord("MRN003", "Bob Wilson", 2),
]

# Sorted by priority automatically
for patient in sorted(queue):
    print(patient)
# Output:
# Jane Doe (MRN: MRN002) - Priority 1
# Bob Wilson (MRN: MRN003) - Priority 2
# John Smith (MRN: MRN001) - Priority 3
```

### eCommerce: Shopping Cart

**Problem**: Need a cart that behaves like a collection but tracks totals and quantities.

**Solution**: Implement collection protocols for intuitive cart operations.

```python
class ShoppingCart:
    def __init__(self):
        self._items = {}  # {product_id: (name, price, quantity)}
    
    def add(self, product_id, name, price, quantity=1):
        if product_id in self._items:
            _, _, existing_qty = self._items[product_id]
            self._items[product_id] = (name, price, existing_qty + quantity)
        else:
            self._items[product_id] = (name, price, quantity)
    
    def __len__(self):
        """Total number of unique products."""
        return len(self._items)
    
    def __getitem__(self, product_id):
        """Get item details by product ID."""
        return self._items[product_id]
    
    def __contains__(self, product_id):
        """Check if product is in cart."""
        return product_id in self._items
    
    def __iter__(self):
        """Iterate over product IDs."""
        return iter(self._items)
    
    @property
    def total(self):
        return sum(price * qty for _, price, qty in self._items.values())
    
    def __repr__(self):
        return f"ShoppingCart({len(self)} items, ${self.total:.2f})"


cart = ShoppingCart()
cart.add("SKU001", "Laptop", 999.99)
cart.add("SKU002", "Mouse", 29.99, quantity=2)

print(len(cart))           # 2
print("SKU001" in cart)    # True
print(cart["SKU001"])      # ('Laptop', 999.99, 1)
print(cart)                # ShoppingCart(2 items, $1059.97)
```

### Banking: Transaction History

**Problem**: Need to store and query immutable transaction records efficiently.

**Solution**: Implement callable validator and comparison-based sorting.

```python
from datetime import datetime

class Transaction:
    def __init__(self, txn_id, amount, timestamp, txn_type):
        self.txn_id = txn_id
        self.amount = amount
        self.timestamp = timestamp
        self.txn_type = txn_type  # 'credit' or 'debit'
    
    def __eq__(self, other):
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.txn_id == other.txn_id
    
    def __lt__(self, other):
        """Sort by timestamp (oldest first)."""
        return self.timestamp < other.timestamp
    
    def __repr__(self):
        sign = "+" if self.txn_type == "credit" else "-"
        return f"Transaction({self.txn_id}: {sign}${self.amount:.2f})"


class TransactionValidator:
    def __init__(self, max_amount):
        self.max_amount = max_amount
    
    def __call__(self, transaction):
        """Validate transaction amount."""
        if transaction.amount > self.max_amount:
            raise ValueError(f"Amount exceeds limit of ${self.max_amount}")
        return True


# Usage
validate = TransactionValidator(max_amount=10000)
txn = Transaction("TXN001", 500, datetime.now(), "debit")

if validate(txn):  # Using __call__
    print(f"Transaction {txn.txn_id} approved")
```

---

## 7. Best Practices

### 1. Always Implement `__repr__`

Every class should have a `__repr__` for debugging. Aim for output that could recreate the object.

```python
# Good
def __repr__(self):
    return f"Patient('{self.patient_id}', '{self.name}', {self.age})"

# Acceptable fallback
def __repr__(self):
    return f"<Patient: {self.patient_id}>"
```

### 2. Return `NotImplemented` for Unknown Types

In comparison methods, return `NotImplemented` instead of `False` to allow Python to try the reverse operation.

```python
def __eq__(self, other):
    if not isinstance(other, Patient):
        return NotImplemented  # Not False!
    return self.patient_id == other.patient_id
```

### 3. Use `@total_ordering` for Complete Comparisons

Implement `__eq__` and one ordering method, then use the decorator.

```python
from functools import total_ordering

@total_ordering
class Priority:
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    # __le__, __gt__, __ge__ are auto-generated
```

### 4. Keep `__str__` User-Friendly

`__str__` is for end-users; keep it clean and readable.

```python
def __str__(self):
    return f"Patient: {self.name}"  # Not: Patient(id='P001', name='Alice', ...)
```

### 5. Make `__call__` Semantically Meaningful

Only implement `__call__` when your object genuinely represents a callable operation.

```python
# Good: Calculator performs a calculation
calculator(70)

# Bad: Patient is not a callable concept
patient()  # Confusing
```

### 6. Document Non-Obvious Special Methods

If your special method does something unexpected, document it clearly.

```python
def __len__(self):
    """Returns number of active appointments, not total."""
    return sum(1 for a in self._appointments if a.is_active)
```

---

## 8. Top 3 Mistakes

### Mistake 1: Returning `False` Instead of `NotImplemented`

**What's the Problem?**
When comparing objects of different types, returning `False` prevents Python from trying the reverse comparison.

**Why It Happens**
Developers assume `False` is correct when types don't match.

**Impact**
- Breaks symmetry: `a == b` may differ from `b == a`
- Prevents interoperability with other types

**Incorrect Approach**
```python
class Patient:
    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False  # Wrong!
        return self.id == other.id
```

**Correct Approach**
```python
class Patient:
    def __eq__(self, other):
        if not isinstance(other, Patient):
            return NotImplemented  # Correct!
        return self.id == other.id
```

**Lesson Learned**
`NotImplemented` signals Python to try `other.__eq__(self)` instead.

---

### Mistake 2: Forgetting `__hash__` When Defining `__eq__`

**What's the Problem?**
When you define `__eq__`, Python automatically sets `__hash__ = None`, making instances unhashable.

**Why It Happens**
The rule "equal objects must have equal hashes" requires both methods to be consistent.

**Impact**
- Objects cannot be used in sets or as dictionary keys
- `TypeError: unhashable type`

**Incorrect Approach**
```python
class Patient:
    def __eq__(self, other):
        return self.id == other.id
    # No __hash__ defined

patients = {Patient("P001")}  # TypeError!
```

**Correct Approach**
```python
class Patient:
    def __eq__(self, other):
        if not isinstance(other, Patient):
            return NotImplemented
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)

patients = {Patient("P001")}  # Works!
```

**Lesson Learned**
If you define `__eq__`, also define `__hash__` based on the same attributes used for equality.

---

### Mistake 3: Overloading Operators in Non-Intuitive Ways

**What's the Problem?**
Using operators for operations that don't match their mathematical or logical meaning.

**Why It Happens**
Desire for "clever" syntax or misunderstanding of operator semantics.

**Impact**
- Code becomes confusing
- Breaks principle of least surprise
- Maintenance nightmare

**Incorrect Approach**
```python
class Patient:
    def __add__(self, other):
        """Merge medical records?"""  # Confusing!
        return MergedRecord(self, other)
    
    def __mul__(self, n):
        """Clone patient n times?"""  # Very confusing!
        return [copy(self) for _ in range(n)]

# What does this even mean?
patient1 + patient2
patient * 3
```

**Correct Approach**
```python
class Patient:
    def merge_records(self, other):
        """Explicit method with clear intent."""
        return MergedRecord(self, other)
    
    # Don't define __add__ or __mul__ for non-mathematical objects
```

**Lesson Learned**
Reserve operator overloading for cases where the operation has a clear, intuitive meaning (e.g., `+` for concatenation of strings or addition of vectors).

---

## Summary

Special methods are the key to making your Python classes feel native and Pythonic. They enable:

- **Integration** with built-in functions (`len()`, `str()`, `sorted()`)
- **Operator support** (`==`, `<`, `[]`, `()`)
- **Clean syntax** that users already know

Master `__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__`, `__getitem__`, and `__call__` to cover most use cases. Always return `NotImplemented` for unknown types, and define `__hash__` when you define `__eq__` if you need hashable objects.
