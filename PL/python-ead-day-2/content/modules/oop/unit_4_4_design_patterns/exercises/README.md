# Unit 4.4: Design Patterns - Exercises

## Overview
This unit focuses on implementing common software design patterns in Python. You will practice the Singleton, Factory, Observer, and Strategy patterns using realistic healthcare and enterprise examples.

**File**: `unit_4_4_design_patterns_exercises.py`

---

## Exercise List

### Exercise 1: App Settings Singleton
**Description**: Implement a Singleton class `AppSettings` to store application-wide configuration. It should only allow one instance to ever be created.
- **Inputs**: Setting keys and values.
- **Outputs**: Confirmed single object identity across calls.
- **Requirements**:
  - Implement `__new__` to control instance creation.
  - Store settings in a dictionary.
- **Hints**:
  - Hint 1: Use a class variable `_instance = None`.
  - Hint 2: If `_instance` is None, call `super().__new__(cls)`.
  - See Solution: `if cls._instance is None: cls._instance = super().__new__(cls)`

---

### Exercise 3: Notification Factory
**Description**: Build a `NotificationFactory` that returns either an `EmailNotification` or `SMSNotification` based on a string input.
- **Inputs**: Notification type ("email" or "sms").
- **Outputs**: Instance of the requested class.
- **Requirements**:
  - Base class `Notification` with `send(msg)` method.
  - Concrete classes with specialized `send` logic.
  - Static factory method `get_notification(type)`.
- **Hints**:
  - Hint 1: The factory doesn't need to be instantiated; use `@staticmethod`.

---

### Exercise 6: Emergency Alert Observer
**Description**: Implement an observer pattern where a `VitalMonitor` (Subject) notifies multiple `AlertResponder` objects (Observers) when a critical event occurs.
- **Inputs**: Vital value.
- **Outputs**: Dynamic notifications to all attached responders.
- **Requirements**:
  - `Subject` class with `attach`, `detach`, and `notify`.
  - `Observer` base class with `update(message)`.
  - `NurseStation` and `EmergencyTeam` concrete observers.

---

### Exercise 8: Compression Strategy
**Description**: implement a `FileArchiver` that can switch between `ZipCompression` and `TarCompression` strategies at runtime.
- **Inputs**: Data to compress.
- **Outputs**: Mock compression result string.
- **Requirements**:
  - `CompressionStrategy` interface.
  - Concrete strategies returning different strings.
  - `FileArchiver` context class with `set_strategy`.
- **Hints**:
  - Hint 1: The `FileArchiver` should have a `self.strategy` attribute.
  - Hint 2: Delegate the work: `self.strategy.compress(data)`.
