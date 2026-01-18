"""
Lab 5: Hospital Department Manager - Starter Code
"""

HOSPITAL_DATA = {
    "Cardiology": {
        "Ward A": {"occupied": 20, "total": 20},
        "Ward B": {"occupied": 15, "total": 20}
    },
    "Neurology": {
        "Ward C": {"occupied": 5, "total": 10},
        "Ward D": {"occupied": 8, "total": 15}
    },
    "Pediatrics": {} # Empty department
}

def generate_report(hospital_data):
    """
    Generate occupancy report from nested hospital data.

    Args:
        hospital_data (dict): Nested structure of Dept -> Ward -> Stats

    Returns:
        dict: A summary containing:
              - total_beds (int)
              - total_occupied (int)
              - occupancy_rate (float, rounded to 2 decimals)
    """
    total_beds = 0
    total_occupied = 0

    for department in hospital_data.values():
        for ward in department.values():
            total_beds += ward["total"]
            total_occupied += ward["occupied"]

    occupancy_rate = round((total_occupied / total_beds * 100), 2) if total_beds > 0 else 0.0
    
    return {
        "total_beds": total_beds,
        "total_occupied": total_occupied,
        "occupancy_rate": occupancy_rate
    }

if __name__ == "__main__":
    report = generate_report(HOSPITAL_DATA)
    print(report)
