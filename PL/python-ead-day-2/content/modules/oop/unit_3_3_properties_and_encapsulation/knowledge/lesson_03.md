---
title: Properties and Encapsulation
type: knowledge
module: oop
unit: unit_3_3_properties_and_encapsulation
order: 3
difficulty: intermediate
tags:
  subtopics:
    - property-decorators
    - getters-setters
    - data-validation
    - encapsulation
    - access-control
    - read-only-properties
---

# Unit 3.3: Properties and Encapsulation

## 1. What

**Properties and encapsulation** are fundamental object-oriented programming concepts that control how data is accessed and modified within a class. Encapsulation is the practice of bundling data (attributes) and methods that operate on that data within a single unit (class), while restricting direct access to some of the object's components. Properties provide a Pythonic way to implement controlled access to attributes through getter and setter methods.

### What Problem Does It Solve?

In real-world applications, you often need to:
- Validate data before storing it in an object
- Compute values dynamically based on other attributes
- Maintain backward compatibility when changing internal implementations
- Protect sensitive data from unauthorized modification
- Enforce business rules and constraints

### When Would You Use This?

Use properties and encapsulation when:
- You need to validate or transform data before assignment
- An attribute's value depends on other attributes
- You want to make an attribute read-only or write-only
- You need to maintain data integrity and enforce business rules
- You're building APIs where internal changes shouldn't break external code

### Key Terminology

- **Encapsulation**: Hiding internal state and requiring all interaction through methods
- **Property**: A special attribute that uses methods to control access
- **Getter**: A method that retrieves an attribute's value
- **Setter**: A method that sets an attribute's value with validation
- **Private attribute**: Conventionally prefixed with underscore(s) to indicate restricted access
- **Read-only property**: A property with only a getter, no setter

## 2. Example

### Example 1: Basic Property with Getter and Setter

```python
class Patient:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        """Getter for age"""
        return self._age
    
    @age.setter
    def age(self, value):
        """Setter for age with validation"""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

# Usage
patient = Patient("Alice", 30)
print(patient.age)  # Output: 30

patient.age = 31  # Uses setter with validation
print(patient.age)  # Output: 31

# patient.age = -5  # Raises ValueError
# patient.age = "thirty"  # Raises TypeError
```

### Example 2: Read-Only Property (Computed Value)

```python
class MedicalRecord:
    def __init__(self, patient_id, diagnosis_date):
        self._patient_id = patient_id
        self._diagnosis_date = diagnosis_date
        self._treatment_start = None
    
    @property
    def patient_id(self):
        """Read-only patient ID"""
        return self._patient_id
    
    @property
    def days_since_diagnosis(self):
        """Computed property - no setter"""
        from datetime import datetime
        if isinstance(self._diagnosis_date, str):
            diagnosis = datetime.fromisoformat(self._diagnosis_date)
        else:
            diagnosis = self._diagnosis_date
        return (datetime.now() - diagnosis).days

# Usage
record = MedicalRecord("P12345", "2024-01-01")
print(record.patient_id)  # Output: P12345
print(record.days_since_diagnosis)  # Output: (calculated days)

# record.patient_id = "P99999"  # AttributeError: can't set attribute
```

### Example 3: Private Attributes and Name Mangling

```python
class HealthInsurance:
    def __init__(self, policy_number, premium):
        self.__policy_number = policy_number  # Private (name mangled)
        self._premium = premium  # Protected (convention only)
    
    @property
    def policy_number(self):
        """Controlled access to private attribute"""
        return self.__policy_number
    
    @property
    def premium(self):
        return self._premium
    
    @premium.setter
    def premium(self, value):
        if value < 0:
            raise ValueError("Premium cannot be negative")
        self._premium = value

# Usage
insurance = HealthInsurance("INS-2024-001", 500)
print(insurance.policy_number)  # Output: INS-2024-001
print(insurance.premium)  # Output: 500

insurance.premium = 550  # Valid
# insurance.policy_number = "NEW"  # AttributeError: can't set attribute

# Name mangling in action
# print(insurance.__policy_number)  # AttributeError
print(insurance._HealthInsurance__policy_number)  # Output: INS-2024-001 (not recommended)
```

### Example 4: Healthcare System - Vital Signs with Validation

```python
class VitalSigns:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self._temperature = None
        self._heart_rate = None
        self._blood_pressure_systolic = None
        self._blood_pressure_diastolic = None
    
    @property
    def temperature(self):
        """Temperature in Celsius"""
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if value < 35.0 or value > 42.0:
            raise ValueError("Temperature out of safe range (35-42 C)")
        self._temperature = value
    
    @property
    def heart_rate(self):
        """Heart rate in beats per minute"""
        return self._heart_rate
    
    @heart_rate.setter
    def heart_rate(self, value):
        if value < 40 or value > 200:
            raise ValueError("Heart rate out of safe range (40-200 bpm)")
        self._heart_rate = value
    
    @property
    def blood_pressure(self):
        """Read-only formatted blood pressure"""
        if self._blood_pressure_systolic and self._blood_pressure_diastolic:
            return f"{self._blood_pressure_systolic}/{self._blood_pressure_diastolic}"
        return "Not recorded"
    
    def set_blood_pressure(self, systolic, diastolic):
        """Method to set both BP values with validation"""
        if systolic < 70 or systolic > 200:
            raise ValueError("Systolic pressure out of range (70-200)")
        if diastolic < 40 or diastolic > 130:
            raise ValueError("Diastolic pressure out of range (40-130)")
        if systolic <= diastolic:
            raise ValueError("Systolic must be greater than diastolic")
        
        self._blood_pressure_systolic = systolic
        self._blood_pressure_diastolic = diastolic

# Usage
vitals = VitalSigns("P001")
vitals.temperature = 37.2
vitals.heart_rate = 72
vitals.set_blood_pressure(120, 80)

print(f"Temperature: {vitals.temperature}C")  # Output: Temperature: 37.2C
print(f"Heart Rate: {vitals.heart_rate} bpm")  # Output: Heart Rate: 72 bpm
print(f"Blood Pressure: {vitals.blood_pressure}")  # Output: Blood Pressure: 120/80
```

### Example 5: Advanced - Property with Deleter

```python
class Prescription:
    def __init__(self, medication, dosage):
        self._medication = medication
        self._dosage = dosage
        self._notes = None
    
    @property
    def notes(self):
        """Optional prescription notes"""
        return self._notes if self._notes else "No notes"
    
    @notes.setter
    def notes(self, value):
        if value and len(value) > 500:
            raise ValueError("Notes cannot exceed 500 characters")
        self._notes = value
    
    @notes.deleter
    def notes(self):
        """Clear prescription notes"""
        print("Clearing prescription notes")
        self._notes = None

# Usage
rx = Prescription("Amoxicillin", "500mg")
rx.notes = "Take with food"
print(rx.notes)  # Output: Take with food

del rx.notes  # Output: Clearing prescription notes
print(rx.notes)  # Output: No notes
```

## 3. Explanation

### How Properties Work

Properties in Python are implemented using **descriptors** - a protocol that allows you to customize attribute access. When you use the `@property` decorator, Python creates a property object that intercepts attribute access and redirects it to your getter, setter, or deleter methods.

**Step-by-Step Mechanism**:

1. **Property Creation**: The `@property` decorator converts a method into a property object
2. **Getter Invocation**: When you access `obj.attribute`, Python calls the getter method
3. **Setter Invocation**: When you assign `obj.attribute = value`, Python calls the setter method
4. **Deleter Invocation**: When you execute `del obj.attribute`, Python calls the deleter method

### Encapsulation Levels in Python

Python uses naming conventions to indicate access levels:

| Convention | Example | Meaning | Enforcement |
|------------|---------|---------|-------------|
| Public | `name` | Intended for external use | None |
| Protected | `_name` | Internal use, subclasses OK | Convention only |
| Private | `__name` | Class-internal only | Name mangling |

**Name Mangling**: When you prefix an attribute with double underscores, Python automatically renames it to `_ClassName__attribute`. This prevents accidental access but isn't true privacy - it's a deterrent, not a lock.

### Property vs Direct Attribute Access

```python
# Direct attribute access
class PatientDirect:
    def __init__(self, age):
        self.age = age  # No validation

patient = PatientDirect(-5)  # Invalid but allowed!

# Property-based access
class PatientProperty:
    def __init__(self, age):
        self._age = None
        self.age = age  # Uses setter
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# patient = PatientProperty(-5)  # Raises ValueError immediately
```

### Performance Characteristics

- **Property access**: Slightly slower than direct attribute access (function call overhead)
- **Typical overhead**: ~50-100 nanoseconds per access
- **When it matters**: Tight loops with millions of iterations
- **When it doesn't**: Normal application code (the validation/logic benefit far outweighs the cost)

### Internal Mechanisms

```python
# What @property actually does (simplified)
class MyClass:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val

# Is roughly equivalent to:
class MyClass:
    def get_value(self):
        return self._value
    
    def set_value(self, val):
        self._value = val
    
    value = property(get_value, set_value)
```

## 4. Why

### 1. Data Validation and Integrity

Properties allow you to enforce business rules and data constraints at the point of assignment, preventing invalid states from ever existing in your objects.

**Benefits**:
- Catch errors immediately rather than later in execution
- Ensure data consistency across the application
- Reduce debugging time by failing fast
- Maintain invariants (conditions that must always be true)

**Example Impact**: In a healthcare system, preventing a negative age or out-of-range vital signs could prevent critical errors in treatment decisions.

### 2. Backward Compatibility

Properties enable you to change internal implementation without breaking external code. You can start with a simple attribute and later add validation or computation without changing the interface.

**Benefits**:
- Refactor internals safely
- Add features without breaking existing code
- Maintain stable APIs
- Evolve code over time

**Example**: You might start with a simple `patient.age` attribute, then later change it to compute age from birth date without breaking any code that uses `patient.age`.

### 3. Computed Attributes

Properties can calculate values on-the-fly based on other attributes, ensuring derived data is always current without storing redundant information.

**Benefits**:
- No data duplication
- Always up-to-date values
- Reduced memory usage
- Simplified data management

**Example**: BMI can be computed from height and weight rather than stored separately, ensuring it's always accurate.

### 4. Encapsulation and Information Hiding

By controlling access to internal state, you can change how data is stored internally without affecting external code, and prevent accidental corruption of object state.

**Benefits**:
- Reduced coupling between components
- Easier to maintain and refactor
- Better separation of concerns
- Clearer interfaces

### 5. Professional Code Quality

Using properties demonstrates understanding of OOP principles and produces more maintainable, enterprise-grade code.

**Benefits**:
- Code reviews pass more easily
- Easier for teams to collaborate
- Follows industry best practices
- Reduces technical debt

## 5. Advantages & Disadvantages

### Advantages

#### 1. Transparent Validation
**Description**: Validation happens automatically when attributes are set, with no special syntax required.

**Code Example**:
```python
class Appointment:
    @property
    def duration_minutes(self):
        return self._duration
    
    @duration_minutes.setter
    def duration_minutes(self, value):
        if value not in [15, 30, 45, 60]:
            raise ValueError("Duration must be 15, 30, 45, or 60 minutes")
        self._duration = value

# Clean, natural syntax
appt = Appointment()
appt.duration_minutes = 30  # Validation happens automatically
```

**Impact**: Users of your class don't need to remember to call validation methods - it's built into the assignment operation itself.

#### 2. Lazy Evaluation
**Description**: Computed properties are only calculated when accessed, not when the object is created.

**Code Example**:
```python
class PatientReport:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self._full_history = None
    
    @property
    def full_history(self):
        """Only load expensive data when needed"""
        if self._full_history is None:
            self._full_history = self._load_from_database()
        return self._full_history
    
    def _load_from_database(self):
        # Expensive operation
        return "Complete medical history..."
```

**Impact**: Improves performance by deferring expensive operations until they're actually needed.

#### 3. Interface Stability
**Description**: You can change internal implementation without breaking external code.

**Code Example**:
```python
# Version 1: Simple attribute
class Patient:
    def __init__(self, age):
        self.age = age

# Version 2: Add validation without breaking existing code
class Patient:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value

# External code still works: patient.age = 30
```

**Impact**: Enables safe refactoring and evolution of codebases.

#### 4. Read-Only Attributes
**Description**: Create attributes that can be read but not modified externally.

**Code Example**:
```python
class MedicalRecord:
    def __init__(self, record_id):
        self._record_id = record_id
        self._created_at = datetime.now()
    
    @property
    def record_id(self):
        """Immutable record ID"""
        return self._record_id
    
    @property
    def created_at(self):
        """Immutable creation timestamp"""
        return self._created_at
```

**Impact**: Prevents accidental modification of critical data that should never change.

#### 5. Cleaner Syntax Than Getter/Setter Methods
**Description**: Properties provide attribute-like access instead of verbose method calls.

**Code Example**:
```python
# Without properties (Java-style)
patient.set_temperature(37.5)
temp = patient.get_temperature()

# With properties (Pythonic)
patient.temperature = 37.5
temp = patient.temperature
```

**Impact**: More readable, maintainable code that follows Python conventions.

### Disadvantages

#### 1. Hidden Complexity
**Description**: Properties can hide expensive operations behind simple attribute access, making performance issues non-obvious.

**When This Becomes a Problem**: When a property performs database queries, network calls, or heavy computation.

**Workaround**:
```python
# Bad: Hidden expensive operation
@property
def all_appointments(self):
    return database.query("SELECT * FROM appointments")  # Slow!

# Better: Make it explicit with a method
def fetch_all_appointments(self):
    """Explicitly indicates this is an expensive operation"""
    return database.query("SELECT * FROM appointments")
```

#### 2. Debugging Difficulty
**Description**: Stack traces show property access as attribute access, making it harder to identify which getter/setter is causing issues.

**When This Becomes a Problem**: When debugging complex property chains or circular dependencies.

**Workaround**: Use descriptive property names and add logging in getters/setters during development.

#### 3. Inheritance Complexity
**Description**: Overriding properties in subclasses requires careful handling of both getter and setter.

**When This Becomes a Problem**:
```python
class Base:
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val

class Derived(Base):
    @property
    def value(self):
        # Overriding getter also removes setter!
        return self._value * 2
```

**Workaround**: Explicitly redefine both getter and setter in the subclass.

#### 4. No Type Hints for Setters
**Description**: Type checkers can't always infer setter parameter types from property declarations.

**When This Becomes a Problem**: In large codebases with strict type checking.

**Workaround**:
```python
from typing import Optional

class Patient:
    _age: Optional[int]
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        self._age = value
```

#### 5. Testing Overhead
**Description**: Properties require testing both getter and setter logic separately, plus validation rules.

**When This Becomes a Problem**: When you have many properties with complex validation.

**Workaround**: Use parameterized tests and test fixtures to reduce boilerplate.

## 6. Real-World Use Cases

### Healthcare: Patient Vital Signs Monitoring

**Problem**: A hospital needs to track patient vital signs with strict validation rules. Invalid vitals could lead to incorrect treatment decisions. The system must prevent out-of-range values and maintain audit trails.

**Solution**: Use properties to validate vital signs at assignment time and compute risk scores based on multiple vitals.

**Code Example**:
```python
from datetime import datetime
from typing import Optional

class PatientVitals:
    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self._temperature: Optional[float] = None
        self._heart_rate: Optional[int] = None
        self._oxygen_saturation: Optional[int] = None
        self._last_updated: Optional[datetime] = None
    
    @property
    def temperature(self) -> Optional[float]:
        """Temperature in Celsius"""
        return self._temperature
    
    @temperature.setter
    def temperature(self, value: float) -> None:
        if not 35.0 <= value <= 42.0:
            raise ValueError(f"Temperature {value}C out of safe range (35-42C)")
        self._temperature = value
        self._last_updated = datetime.now()
    
    @property
    def heart_rate(self) -> Optional[int]:
        """Heart rate in beats per minute"""
        return self._heart_rate
    
    @heart_rate.setter
    def heart_rate(self, value: int) -> None:
        if not 40 <= value <= 200:
            raise ValueError(f"Heart rate {value} bpm out of safe range (40-200 bpm)")
        self._heart_rate = value
        self._last_updated = datetime.now()
    
    @property
    def oxygen_saturation(self) -> Optional[int]:
        """Blood oxygen saturation percentage"""
        return self._oxygen_saturation
    
    @oxygen_saturation.setter
    def oxygen_saturation(self, value: int) -> None:
        if not 70 <= value <= 100:
            raise ValueError(f"O2 saturation {value}% out of range (70-100%)")
        self._oxygen_saturation = value
        self._last_updated = datetime.now()
    
    @property
    def risk_level(self) -> str:
        """Computed risk assessment based on vitals"""
        if not all([self._temperature, self._heart_rate, self._oxygen_saturation]):
            return "INCOMPLETE_DATA"
        
        risk_score = 0
        
        # Temperature risk
        if self._temperature >= 38.5 or self._temperature <= 35.5:
            risk_score += 2
        elif self._temperature >= 38.0 or self._temperature <= 36.0:
            risk_score += 1
        
        # Heart rate risk
        if self._heart_rate >= 120 or self._heart_rate <= 50:
            risk_score += 2
        elif self._heart_rate >= 100 or self._heart_rate <= 60:
            risk_score += 1
        
        # Oxygen saturation risk
        if self._oxygen_saturation <= 90:
            risk_score += 3
        elif self._oxygen_saturation <= 94:
            risk_score += 1
        
        if risk_score >= 4:
            return "CRITICAL"
        elif risk_score >= 2:
            return "WARNING"
        else:
            return "NORMAL"

# Usage
vitals = PatientVitals("P12345")
vitals.temperature = 38.7
vitals.heart_rate = 95
vitals.oxygen_saturation = 96

print(f"Risk Level: {vitals.risk_level}")  # Output: Risk Level: WARNING
```

**Benefits**:
- Prevents invalid vital signs from being recorded
- Automatically computes risk levels without manual calculation
- Maintains data integrity critical for patient safety
- Provides clear error messages for out-of-range values

### eCommerce: Product Pricing and Inventory

**Problem**: An eCommerce platform needs to manage product prices with dynamic discounts, tax calculations, and inventory tracking. Prices must always be positive, discounts must be valid percentages, and inventory must prevent overselling.

**Solution**: Use properties to validate pricing data, compute final prices with discounts and taxes, and enforce inventory constraints.

**Code Example**:
```python
class Product:
    def __init__(self, product_id: str, name: str, base_price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self._base_price = base_price
        self._discount_percent = 0
        self._stock = stock
        self._tax_rate = 0.08  # 8% tax
    
    @property
    def base_price(self) -> float:
        """Base price before discounts"""
        return self._base_price
    
    @base_price.setter
    def base_price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Price must be positive")
        self._base_price = value
    
    @property
    def discount_percent(self) -> float:
        """Discount percentage (0-100)"""
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self, value: float) -> None:
        if not 0 <= value <= 100:
            raise ValueError("Discount must be between 0 and 100")
        self._discount_percent = value
    
    @property
    def discounted_price(self) -> float:
        """Price after discount, before tax"""
        return self._base_price * (1 - self._discount_percent / 100)
    
    @property
    def final_price(self) -> float:
        """Final price including tax"""
        return self.discounted_price * (1 + self._tax_rate)
    
    @property
    def stock(self) -> int:
        """Current inventory level"""
        return self._stock
    
    @stock.setter
    def stock(self, value: int) -> None:
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = value
    
    @property
    def in_stock(self) -> bool:
        """Check if product is available"""
        return self._stock > 0
    
    def reserve_stock(self, quantity: int) -> bool:
        """Attempt to reserve stock for purchase"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self._stock:
            return False
        self._stock -= quantity
        return True

# Usage
product = Product("PROD-001", "Laptop", 999.99, 50)
product.discount_percent = 15

print(f"Base Price: ${product.base_price:.2f}")
print(f"Discount: {product.discount_percent}%")
print(f"Discounted Price: ${product.discounted_price:.2f}")
print(f"Final Price (with tax): ${product.final_price:.2f}")
print(f"In Stock: {product.in_stock}")

if product.reserve_stock(2):
    print(f"Reserved 2 units. Remaining: {product.stock}")
```

**Benefits**:
- Prevents negative prices and invalid discounts
- Automatically calculates final prices with all factors
- Prevents overselling through stock validation
- Provides clear inventory status

### Banking: Account Balance and Transaction Limits

**Problem**: A banking system must enforce strict rules on account balances, transaction limits, and overdraft protection. Negative balances may only be allowed for accounts with overdraft protection, and daily transaction limits must be enforced.

**Solution**: Use properties to validate transactions, enforce limits, and protect account integrity.

**Code Example**:
```python
from datetime import datetime, date
from typing import List, Optional

class BankAccount:
    def __init__(self, account_number: str, initial_balance: float = 0):
        self._account_number = account_number
        self._balance = initial_balance
        self._overdraft_limit = 0
        self._daily_withdrawal_limit = 1000
        self._daily_withdrawals = 0
        self._last_withdrawal_date: Optional[date] = None
        self._is_frozen = False
    
    @property
    def account_number(self) -> str:
        """Read-only account number"""
        return self._account_number
    
    @property
    def balance(self) -> float:
        """Current account balance"""
        return self._balance
    
    @property
    def available_balance(self) -> float:
        """Balance including overdraft protection"""
        return self._balance + self._overdraft_limit
    
    @property
    def overdraft_limit(self) -> float:
        """Maximum allowed negative balance"""
        return self._overdraft_limit
    
    @overdraft_limit.setter
    def overdraft_limit(self, value: float) -> None:
        if value < 0:
            raise ValueError("Overdraft limit cannot be negative")
        if value > 5000:
            raise ValueError("Overdraft limit cannot exceed $5000")
        self._overdraft_limit = value
    
    @property
    def daily_withdrawal_limit(self) -> float:
        """Maximum withdrawals per day"""
        return self._daily_withdrawal_limit
    
    @daily_withdrawal_limit.setter
    def daily_withdrawal_limit(self, value: float) -> None:
        if value < 0:
            raise ValueError("Daily limit cannot be negative")
        if value > 10000:
            raise ValueError("Daily limit cannot exceed $10,000")
        self._daily_withdrawal_limit = value
    
    @property
    def is_frozen(self) -> bool:
        """Account freeze status"""
        return self._is_frozen
    
    def freeze_account(self) -> None:
        """Freeze account to prevent transactions"""
        self._is_frozen = True
    
    def unfreeze_account(self) -> None:
        """Unfreeze account to allow transactions"""
        self._is_frozen = False
    
    def deposit(self, amount: float) -> None:
        """Deposit money into account"""
        if self._is_frozen:
            raise ValueError("Account is frozen")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money from account"""
        if self._is_frozen:
            raise ValueError("Account is frozen")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        # Reset daily counter if new day
        today = date.today()
        if self._last_withdrawal_date != today:
            self._daily_withdrawals = 0
            self._last_withdrawal_date = today
        
        # Check daily limit
        if self._daily_withdrawals + amount > self._daily_withdrawal_limit:
            raise ValueError(f"Daily withdrawal limit of ${self._daily_withdrawal_limit} exceeded")
        
        # Check available balance
        if amount > self.available_balance:
            raise ValueError("Insufficient funds (including overdraft)")
        
        self._balance -= amount
        self._daily_withdrawals += amount

# Usage
account = BankAccount("ACC-123456", 1000)
account.overdraft_limit = 500

print(f"Balance: ${account.balance:.2f}")
print(f"Available (with overdraft): ${account.available_balance:.2f}")

account.withdraw(1200)  # Uses overdraft
print(f"Balance after withdrawal: ${account.balance:.2f}")

account.deposit(500)
print(f"Balance after deposit: ${account.balance:.2f}")

# account.withdraw(2000)  # Raises ValueError: Daily limit exceeded
```

**Benefits**:
- Enforces transaction limits automatically
- Prevents unauthorized overdrafts
- Protects frozen accounts from transactions
- Maintains accurate balance tracking with overdraft consideration

## 7. Best Practices

### Best Practice 1: Use Properties for Validation, Not Just Access

**When to apply**: Whenever an attribute has constraints or business rules

**Why**: Properties are most valuable when they enforce rules, not just wrap attributes

**Good Practice**:
```python
class Prescription:
    @property
    def dosage_mg(self):
        return self._dosage_mg
    
    @dosage_mg.setter
    def dosage_mg(self, value):
        if value <= 0:
            raise ValueError("Dosage must be positive")
        if value > 1000:
            raise ValueError("Dosage exceeds maximum safe limit")
        self._dosage_mg = value
```

**Why This Works Better**:
- Catches invalid data immediately
- Prevents invalid states from existing
- Makes constraints explicit in code
- Reduces bugs from invalid data

### Best Practice 2: Keep Property Logic Simple

**When to apply**: Always - properties should be fast and side-effect free

**Why**: Properties should behave like attributes, not methods

**Good Practice**:
```python
class Patient:
    @property
    def full_name(self):
        """Simple, fast computation"""
        return f"{self.first_name} {self.last_name}"
    
    def load_medical_history(self):
        """Expensive operation - use a method, not a property"""
        return database.query_history(self.patient_id)
```

**Avoid**:
```python
class Patient:
    @property
    def medical_history(self):
        # BAD: Expensive database query in property
        return database.query_history(self.patient_id)
```

**Why This Works Better**:
- Properties feel like attributes to users
- Expensive operations should be explicit (methods)
- Prevents performance surprises
- Follows principle of least astonishment

### Best Practice 3: Use Read-Only Properties for Computed Values

**When to apply**: When a value is derived from other attributes

**Why**: Prevents inconsistencies and reduces data duplication

**Good Practice**:
```python
class Patient:
    def __init__(self, weight_kg, height_m):
        self.weight_kg = weight_kg
        self.height_m = height_m
    
    @property
    def bmi(self):
        """Computed value - no setter needed"""
        return self.weight_kg / (self.height_m ** 2)
```

**Why This Works Better**:
- BMI is always accurate
- No risk of stale data
- Single source of truth
- Automatic updates when weight or height changes

### Best Practice 4: Use Descriptive Names for Private Attributes

**When to apply**: Always, for internal attributes

**Why**: Makes code more maintainable and intentions clear

**Good Practice**:
```python
class MedicalRecord:
    def __init__(self, patient_id):
        self._patient_id = patient_id  # Protected
        self.__encryption_key = generate_key()  # Private
    
    @property
    def patient_id(self):
        return self._patient_id
```

**Why This Works Better**:
- Clear distinction between public and internal
- Follows Python conventions
- Easier to understand code intent
- Helps prevent accidental misuse

### Best Practice 5: Provide Meaningful Error Messages

**When to apply**: In all property setters with validation

**Why**: Helps users understand what went wrong and how to fix it

**Good Practice**:
```python
class Appointment:
    @property
    def duration_minutes(self):
        return self._duration
    
    @duration_minutes.setter
    def duration_minutes(self, value):
        valid_durations = [15, 30, 45, 60]
        if value not in valid_durations:
            raise ValueError(
                f"Duration must be one of {valid_durations}, got {value}"
            )
        self._duration = value
```

**Why This Works Better**:
- Users know exactly what's wrong
- Shows valid options
- Reduces debugging time
- Improves developer experience

### Best Practice 6: Document Properties with Docstrings

**When to apply**: For all public properties

**Why**: Properties are part of your class's public API

**Good Practice**:
```python
class VitalSigns:
    @property
    def temperature(self):
        """
        Patient temperature in Celsius.
        
        Valid range: 35.0 - 42.0
        Raises ValueError if out of range.
        """
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if not 35.0 <= value <= 42.0:
            raise ValueError("Temperature out of safe range")
        self._temperature = value
```

**Why This Works Better**:
- Clear documentation for users
- IDE autocomplete shows constraints
- Reduces need to read implementation
- Professional code quality

### Best Practice 7: Don't Overuse Properties

**When to apply**: Use properties judiciously, not for everything

**Why**: Not every attribute needs to be a property

**Good Practice**:
```python
class Patient:
    def __init__(self, name, age):
        self.name = name  # Simple attribute, no property needed
        self._age = age
    
    @property
    def age(self):
        """Property only where validation is needed"""
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError("Invalid age")
        self._age = value
```

**Why This Works Better**:
- Simpler code where properties aren't needed
- Easier to understand and maintain
- Better performance for simple attributes
- Follows "simple is better than complex"

## 8. Top 3 Mistakes

### Mistake 1: Forgetting to Initialize Private Attributes

**What's the Problem?**
Developers create properties but forget to initialize the underlying private attribute in `__init__`, leading to `AttributeError` when the property is first accessed.

**Why It Happens**
When focusing on property decorators, it's easy to forget that properties are just wrappers around actual attributes that need to exist.

**Impact**
- Runtime errors when accessing properties
- Confusing error messages
- Objects in invalid states
- Difficult debugging

**Incorrect Approach**:
```python
class Patient:
    def __init__(self, name):
        self.name = name
        # Forgot to initialize _age!
    
    @property
    def age(self):
        return self._age  # AttributeError: 'Patient' object has no attribute '_age'
    
    @age.setter
    def age(self, value):
        self._age = value

patient = Patient("Alice")
print(patient.age)  # AttributeError!
```

**Correct Approach**:
```python
class Patient:
    def __init__(self, name, age=None):
        self.name = name
        self._age = age  # Initialize the private attribute
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value is not None and (value < 0 or value > 150):
            raise ValueError("Invalid age")
        self._age = value

patient = Patient("Alice")
print(patient.age)  # Output: None (or set a default)
patient.age = 30
print(patient.age)  # Output: 30
```

**Lesson Learned**
Always initialize private attributes in `__init__`, even if just to `None`. Properties are wrappers, not storage - the actual data must exist somewhere.

### Mistake 2: Creating Circular Dependencies in Properties

**What's the Problem?**
Properties that reference each other or use the property name instead of the private attribute create infinite recursion loops.

**Why It Happens**
Confusion between the property name and the private attribute name, or attempting to use properties within their own setters.

**Impact**
- `RecursionError` crashes
- Stack overflow
- Application hangs
- Difficult to diagnose

**Incorrect Approach**:
```python
class VitalSigns:
    def __init__(self):
        self.temperature = None  # This calls the setter!
    
    @property
    def temperature(self):
        return self.temperature  # Calls itself infinitely!
    
    @temperature.setter
    def temperature(self, value):
        self.temperature = value  # Calls itself infinitely!

# vitals = VitalSigns()  # RecursionError!
```

**Correct Approach**:
```python
class VitalSigns:
    def __init__(self):
        self._temperature = None  # Use private attribute
    
    @property
    def temperature(self):
        return self._temperature  # Return private attribute
    
    @temperature.setter
    def temperature(self, value):
        if value is not None and not (35.0 <= value <= 42.0):
            raise ValueError("Temperature out of range")
        self._temperature = value  # Set private attribute

vitals = VitalSigns()
vitals.temperature = 37.5
print(vitals.temperature)  # Output: 37.5
```

**Lesson Learned**
Always use a different name for the private attribute (convention: prefix with underscore). Never reference the property name inside its own getter or setter.

### Mistake 3: Putting Complex Logic in Getters

**What's the Problem?**
Placing expensive operations (database queries, API calls, complex calculations) in property getters makes simple attribute access unexpectedly slow and creates hidden side effects.

**Why It Happens**
Properties look like simple attributes, making it tempting to hide complexity behind them. Developers may not realize the performance implications.

**Impact**
- Severe performance degradation
- Unexpected delays in code
- Difficult to profile and optimize
- Violates principle of least surprise
- Hidden I/O operations

**Incorrect Approach**:
```python
class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id
    
    @property
    def medical_history(self):
        # BAD: Expensive database query every time property is accessed
        import time
        time.sleep(2)  # Simulating slow database query
        return database.query(f"SELECT * FROM history WHERE patient_id = {self.patient_id}")
    
    @property
    def risk_score(self):
        # BAD: Calls expensive property multiple times
        history = self.medical_history  # Slow!
        conditions = self.medical_history  # Slow again!
        return calculate_risk(history, conditions)

# Simple-looking code that's actually very slow
patient = Patient("P001")
score = patient.risk_score  # Takes 4+ seconds!
```

**Correct Approach**:
```python
class Patient:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self._medical_history_cache = None
    
    def load_medical_history(self):
        """Explicit method for expensive operation"""
        import time
        time.sleep(2)  # Simulating slow database query
        self._medical_history_cache = database.query(
            f"SELECT * FROM history WHERE patient_id = {self.patient_id}"
        )
        return self._medical_history_cache
    
    @property
    def medical_history(self):
        """Fast property using cached data"""
        if self._medical_history_cache is None:
            raise ValueError("Medical history not loaded. Call load_medical_history() first.")
        return self._medical_history_cache
    
    @property
    def risk_score(self):
        """Fast computation using cached data"""
        return calculate_risk(self.medical_history)

# Clear, explicit code
patient = Patient("P001")
patient.load_medical_history()  # Explicit: "this will be slow"
score = patient.risk_score  # Fast: uses cached data
```

**Lesson Learned**
Properties should be fast and side-effect free. Use explicit methods for expensive operations, and cache results if needed. Properties should feel like attributes, not method calls.
