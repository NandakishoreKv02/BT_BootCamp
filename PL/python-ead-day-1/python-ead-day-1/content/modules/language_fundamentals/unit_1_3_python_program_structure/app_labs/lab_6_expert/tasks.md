# Lab 6: HL7 Message Parser - Tasks

## Task 1: Module Level Documentation
Add a top-level docstring explaining that this is an HL7 parsing library. Include a simple usage example in the docstring.

## Task 2: Implement parse_segment(segment_str)
Helper function.
- Input: String like `PID|1||DOE^JOHN`
- Logic: Split by `|`.
- Output: List of strings.
- **Docstring**: Fully descriptive.

## Task 3: Implement parse_message(hl7_string)
Main function.
- Input: Multiline string containing segments (MSH, PID, OBX).
- Logic: Split lines, call `parse_segment` for each.
- Output: Dictionary where keys are Segment Names (e.g., "PID") and values are lists of fields.
- **Handling**: If multiple segments of same type exist (e.g. multiple OBX), store them as a list of lists.
    - Example: `{'MSH': [...], 'PID': [...], 'OBX': [[...], [...]]}`

## Task 4: Implement extract_patient_name(parsed_data)
Utility.
- Logic: Look at `PID` segment. Field 5 usually contains Name `Surname^Given`.
- Return dictionary `{"family": "...", "given": "..."}`.
- Docstring must describe exact field index assumptions (e.g., "Assumes PID-5 is Patient Name").

## Task 5: Professional Structure
- Constants for delimiters (`|`, `^`).
- `__all__` variable to define exported symbols.
- `if __name__ == "__main__":` block that runs a demo parsing.
