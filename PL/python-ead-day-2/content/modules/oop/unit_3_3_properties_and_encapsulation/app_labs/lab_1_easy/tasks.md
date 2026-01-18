# Lab 1 Tasks: Patient Vital Signs Monitor - Basic Properties

## Task 1: Create VitalSigns Class with Private Attributes
**Difficulty**: Easy | **Points**: 20

### Objective
Set up the basic class structure with private attributes for storing vital signs data.

### Requirements
- Create a class named `VitalSigns`
- Define `__init__` method that accepts: patient_id, temperature, heart_rate, bp_systolic, bp_diastolic
- Store all values in private attributes (prefix with underscore):
  - `_patient_id`
  - `_temperature`
  - `_heart_rate`
  - `_bp_systolic`
  - `_bp_diastolic`

### Expected Behavior
```python
vitals = VitalSigns("P001", 37.0, 70, 120, 80)
# Private attributes are set but not directly accessible
```

---

## Task 2: Implement Temperature Property Getter
**Difficulty**: Easy | **Points**: 15

### Objective
Create a property that provides read-only access to temperature.

### Requirements
- Use `@property` decorator
- Create method named `temperature`
- Return `_temperature` value
- Should return a float

### Expected Behavior
```python
vitals = VitalSigns("P001", 37.2, 70, 120, 80)
print(vitals.temperature)  # Output: 37.2
```

---

## Task 3: Implement Heart Rate Property Getter
**Difficulty**: Easy | **Points**: 15

### Objective
Create a property for accessing heart rate.

### Requirements
- Use `@property` decorator
- Create method named `heart_rate`
- Return `_heart_rate` value
- Should return an integer

### Expected Behavior
```python
vitals = VitalSigns("P001", 37.0, 72, 120, 80)
print(vitals.heart_rate)  # Output: 72
```

---

## Task 4: Implement Blood Pressure Property Getter
**Difficulty**: Easy | **Points**: 25

### Objective
Create a computed property that formats blood pressure as a string.

### Requirements
- Use `@property` decorator
- Create method named `blood_pressure`
- Return formatted string: "{systolic}/{diastolic}"
- Example: "120/80"

### Expected Behavior
```python
vitals = VitalSigns("P001", 37.0, 70, 120, 80)
print(vitals.blood_pressure)  # Output: "120/80"
```

---

## Task 5: Implement Patient ID Property Getter
**Difficulty**: Easy | **Points**: 15

### Objective
Create a read-only property for patient ID.

### Requirements
- Use `@property` decorator
- Create method named `patient_id`
- Return `_patient_id` value
- Should be read-only (no setter)

### Expected Behavior
```python
vitals = VitalSigns("P12345", 37.0, 70, 120, 80)
print(vitals.patient_id)  # Output: "P12345"
```

---

## Task 6: Add String Representation
**Difficulty**: Easy | **Points**: 10

### Objective
Implement `__str__` method for readable output.

### Requirements
- Define `__str__` method
- Return formatted string with all vital signs
- Format: "Patient {id}: Temp={temp}C, HR={hr}bpm, BP={bp}"

### Expected Behavior
```python
vitals = VitalSigns("P001", 37.2, 72, 120, 80)
print(vitals)  
# Output: "Patient P001: Temp=37.2C, HR=72bpm, BP=120/80"
```

---

## Testing Your Implementation

Run the test file to verify all tasks:
```bash
python tests.py
```

All tests should pass if your implementation is correct.

---

## Hints

**Hint 1 (Conceptual)**: Properties allow you to access methods like attributes. The `@property` decorator converts a method into a "getter" for a read-only attribute.

**Hint 2 (Directional)**: Remember that private attributes in Python use a single underscore prefix by convention. The property methods should return these private attributes.

**Hint 3 (Implementation)**: 
```python
@property
def temperature(self):
    return self._temperature
```

---

## Common Mistakes to Avoid

1. **Forgetting the @property decorator** - Without it, you'd need to call the method with parentheses
2. **Not using private attributes** - Properties should wrap private attributes, not public ones
3. **Trying to set read-only properties** - These properties don't have setters, so assignment will fail

---

## Success Criteria

- ✅ All private attributes initialized correctly
- ✅ All properties return correct values
- ✅ Blood pressure formatted as string
- ✅ Properties are read-only (no setters)
- ✅ All tests pass
