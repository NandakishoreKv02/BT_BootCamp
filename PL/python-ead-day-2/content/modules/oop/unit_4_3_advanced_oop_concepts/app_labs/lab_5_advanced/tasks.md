# Lab 5 Tasks

## Task 1: Create `TelemetryPacket` with `__slots__`
- Define class `TelemetryPacket`.
- Set `__slots__ = ('device_id', 'timestamp', 'vital_type', 'value')`.
- Implement `__init__(self, device_id, timestamp, vital_type, value)`.

## Task 2: Verify Restriction
- Create an instance of `TelemetryPacket`.
- Assign a new attribute not in the slots list (e.g., `packet.status = "OK"`).
- Catch the `AttributeError`.

## Task 3: Compare with Standard Class
- Create a class `LegacyPacket` without `__slots__`.
- Verify that `LegacyPacket` *has* a `__dict__` attribute while `TelemetryPacket` does *not*.

## Task 4: Memory Simulation (Optional logic)
- Create 10,000 packets and observe success.
