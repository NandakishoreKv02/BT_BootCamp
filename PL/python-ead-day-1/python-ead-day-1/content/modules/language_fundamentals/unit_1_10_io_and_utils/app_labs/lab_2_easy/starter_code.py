"""
Lab 2: Clinical Shift Report Generator - Solution
"""

def generate_report_row(patient_id, vitals_count, status):
    return f"{patient_id:<10} | {vitals_count:>5} | {status:>12}"

if __name__ == "__main__":
    print(generate_report_row("P-101", 8, "ADMITTED"))
