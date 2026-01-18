"""
Lab 2: IV Flow Rate Calculator - Starter Code
"""

def calculate_flow_rate(volume_ml, time_hr=1.0):
    return volume_ml / time_hr

if __name__ == "__main__":
    print(calculate_flow_rate(500, 2))
    print(calculate_flow_rate(100))
