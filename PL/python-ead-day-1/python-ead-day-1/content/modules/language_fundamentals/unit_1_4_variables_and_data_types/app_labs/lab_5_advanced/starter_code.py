"""
Lab 5: HL7 Field Extractor - Starter Code
"""

def extract_pid_fields(pid_segment):
    """
    Extract Name (field 5) and DOB (field 7).
    
    Args:
        pid_segment (str): e.g. "PID|1||123||DOE^JOHN||19800101"
        
    Returns:
        dict: {'name': str, 'dob': str}
    """
    if not pid_segment.startswith("PID|"):
        raise ValueError("Invalid PID segment")
    
    fields = pid_segment.split('|')
    return {'name': fields[5], 'dob': fields[7]}

def mask_patient_name(pid_segment):
    """
    Replace patient name with '***'.
    
    Returns:
        str: New HL7 string with masked name.
    """
    fields = pid_segment.split('|')
    fields[5] = '***'
    return '|'.join(fields)

if __name__ == "__main__":
    segment = "PID|1||12345^^^MRN||DOE^JOHN||19800101|M"
    data = extract_pid_fields(segment)
    print(data)
    masked = mask_patient_name(segment)
    print(masked)
