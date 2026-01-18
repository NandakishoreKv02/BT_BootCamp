"""
Lab 6: Dynamic Config Loader - Starter Code
"""

def infer_type(value_str):
    """
    Infer the correct Python type from a string representation.
    
    Args:
        value_str (str): Raw string value.
        
    Returns:
        Any: int, float, bool, None, or str.
    """
    if value_str.lower() in ["none", "null"]:
        return None
    
    if value_str.lower() in ["true", "false"]:
        return value_str.lower() == "true"
    
    try:
        return int(value_str)
    except ValueError:
        pass
    
    try:
        return float(value_str)
    except ValueError:
        pass
    
    return value_str

def load_config(raw_config):
    """
    Convert dictionary values to their inferred types.
    
    Args:
        raw_config (dict): Dict with string values.
        
    Returns:
        dict: Dict with typed values.
    """
    return {key: infer_type(value) for key, value in raw_config.items()}

if __name__ == "__main__":
    raw = {"RETRIES": "5", "DEBUG": "True"}
    print(load_config(raw))
