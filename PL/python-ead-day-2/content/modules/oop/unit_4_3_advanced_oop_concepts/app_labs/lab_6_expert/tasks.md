# Lab 6 Tasks

## Task 1: implement `MonitorRegistry` Metaclass
- Inherit from `type`.
- Maintain a class-level dictionary `plugins = {}`.
- Implement `__new__(mcs, name, bases, attrs)`.
- **Validation**: If `MONITOR_ID` is not in `attrs` (and the class is not "BaseMonitor"), raise a `TypeError`.
- **Registration**: Store the class in `plugins[attrs['MONITOR_ID']] = new_class`.

## Task 2: Create `BaseMonitor`
- Set `metaclass=MonitorRegistry`.

## Task 3: Implement Plugins
- Create `HeartMonitor(BaseMonitor)` with `MONITOR_ID = "HR"`.
- Create `OxygenMonitor(BaseMonitor)` with `MONITOR_ID = "O2"`.

## Task 4: Dynamic Creation
- Use `MonitorRegistry.plugins` to instantiate one of each monitor without knowing their class names explicitly.
