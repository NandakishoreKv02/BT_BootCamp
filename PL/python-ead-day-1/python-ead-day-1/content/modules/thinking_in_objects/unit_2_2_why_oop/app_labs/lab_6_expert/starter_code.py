"""
Lab 6: The HL7 Industry Simulator - Starter Code
"""

def create_segment(segment_type, field_list):
    # TODO: Return segment dict
    pass

def create_message():
    # TODO: Return message dict with empty segments list
    pass

def add_segment(message, segment):
    # TODO: Implement
    pass

def to_hl7_string(message):
    """
    Renders the clinical 'Object' into a raw industrial 'String'.
    Example: PID|1|DOE^JOHN|...
    """
    # TODO: Loop through segments
    # TODO: Join fields with '|'
    # TODO: Join segments with '\n'
    return ""

def main():
    print("--- HL7 Message Generator ---")
    
    # TODO: Create message
    # TODO: Add MSH, PID, and OBX segments
    # TODO: Print the final serialized string

if __name__ == "__main__":
    main()
