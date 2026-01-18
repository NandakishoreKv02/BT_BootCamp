"""
Importable Logger - Log messages with timestamps.
"""

import datetime


def log_message(level, message):
    """
    Create a formatted log message with timestamp.
    
    Args:
        level (str): Log level (e.g., INFO, ERROR).
        message (str): Log message content.
    
    Returns:
        str: Formatted log message with timestamp.
    """
    timestamp = datetime.datetime.now()
    return f"[{timestamp}] [{level}] {message}"


if __name__ == "__main__":
    print("Logger Demo Started")
    print(log_message("INFO", "Test message"))
    print("Logger Demo Finished")
