# Lab 2 Tasks: Setters & Validation

## Task 1: Temperature Setter with Validation
**Difficulty**: Easy | **Points**: 20

Add a setter for temperature that validates the range.

**Requirements**:
- Use @temperature.setter decorator
- Accept float value
- Validate: 35.0 <= value <= 42.0
- Raise ValueError if out of range with message: "Temperature must be between 35.0 and 42.0 Celsius"
- Update _temperature if valid

## Task 2: Heart Rate Setter with Validation
**Difficulty**: Easy | **Points**: 20

Add a setter for heart rate with range checking.

**Requirements**:
- Use @heart_rate.setter decorator
- Accept int value
- Validate: 40 <= value <= 200
- Raise ValueError if out of range with message: "Heart rate must be between 40 and 200 BPM"
- Update _heart_rate if valid

## Task 3: Blood Pressure Setters
**Difficulty**: Intermediate | **Points**: 30

Add individual setters for systolic and diastolic BP.

**Requirements**:
- Create @property for bp_systolic and bp_diastolic
- Systolic range: 70-200 mmHg
- Diastolic range: 40-130 mmHg
- Raise ValueError with appropriate messages

## Task 4: Set Blood Pressure Method
**Difficulty**: Intermediate | **Points**: 20

Create method to set both BP values with cross-validation.

**Requirements**:
- Method: set_blood_pressure(systolic, diastolic)
- Validate ranges for both values
- Ensure systolic > diastolic
- Raise ValueError if systolic <= diastolic

## Task 5: Update All Vitals Method
**Difficulty**: Easy | **Points**: 10

Create method to update all vitals at once.

**Requirements**:
- Method: update_vitals(temperature, heart_rate, bp_systolic, bp_diastolic)
- Use existing setters for validation
- Update all values if all valid
