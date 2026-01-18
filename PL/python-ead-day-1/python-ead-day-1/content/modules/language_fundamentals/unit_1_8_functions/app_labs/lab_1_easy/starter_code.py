"""
Lab 1: Vital Sign Formatter - Starter Code
"""

def format_vital(name, value, unit):
    return f"{name}: {value} {unit}"

if __name__ == "__main__":
    print(format_vital("Temp", 37.5, "C"))
