# Lab 6 Tasks

## Task 1: The Segment "Constructor"
Define `create_segment(segment_type, field_list)`:
- Returns a dictionary with keys: `'type'` (string) and `'fields'` (list).

## Task 2: The Message Container
Define `create_message()`:
- Returns a dictionary with a `'segments'` key initialized to an empty list.

## Task 3: Component Assembly
Define `add_segment(message_obj, segment_obj)`:
- Append the segment dictionary to the message's list of segments.

## Task 4: The Serialization Engine
Define `to_hl7_string(message_obj)`:
- Initialize a `lines` list.
- For each segment in the message:
  - Join the `type` and the `fields` with the pipe `|` character.
  - Add the resulting string to the `lines` list.
- Join all lines with a newline `\n`.
- Return the final industrial string.

## Task 5: Industrial Simulation
In the `main()` function:
1. Create a message container.
2. Add an `MSH` (Header), a `PID` (Patient ID), and two `OBX` (Vitals) segments.
3. Serialize the message to a string and print it.
4. Verify that the output perfectly matches the HL7 pipe-delimited standard.
