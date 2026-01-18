"""
HL7 Message Parser - Parse HL7 healthcare messages.

Usage:
    parsed = parse_message(hl7_string)
    name = extract_patient_name(parsed)
"""

DELIMITER_FIELD = "|"
DELIMITER_COMPONENT = "^"

__all__ = ["parse_segment", "parse_message", "extract_patient_name"]


def parse_segment(segment_str):
    """
    Parse a single HL7 segment.
    
    Args:
        segment_str (str): HL7 segment string.
    
    Returns:
        list: List of fields split by delimiter.
    """
    return segment_str.split(DELIMITER_FIELD)


def parse_message(hl7_string):
    """
    Parse a full HL7 message.
    
    Args:
        hl7_string (str): Multiline HL7 message.
    
    Returns:
        dict: Dictionary with segment names as keys and field lists as values.
    """
    result = {}
    for line in hl7_string.strip().split("\n"):
        if not line.strip():
            continue
        fields = parse_segment(line)
        segment_name = fields[0]
        if segment_name in result:
            if not isinstance(result[segment_name][0], list):
                result[segment_name] = [result[segment_name]]
            result[segment_name].append(fields)
        else:
            result[segment_name] = fields
    return result


def extract_patient_name(parsed_data):
    """
    Extract patient name from PID segment.
    Assumes PID-5 (index 5) contains patient name in format Surname^Given.
    
    Args:
        parsed_data (dict): Parsed HL7 message.
    
    Returns:
        dict: Dictionary with 'family' and 'given' name components.
    """
    pid = parsed_data.get("PID", [])
    name_field = pid[5] if len(pid) > 5 else ""
    parts = name_field.split(DELIMITER_COMPONENT)
    return {
        "family": parts[0] if len(parts) > 0 else "",
        "given": parts[1] if len(parts) > 1 else ""
    }


if __name__ == "__main__":
    sample = "MSH|^~\&|HIS\nPID|1||12345|||DOE^JOHN"
    parsed = parse_message(sample)
    print(parsed)
    print(extract_patient_name(parsed))
