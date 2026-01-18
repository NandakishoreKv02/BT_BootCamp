"""
Lab 4: Encapsulated Triage Logic - Starter Code
"""

# TODO: Define get_triage_category(systolic_bp)
def get_triage_category(systolic_bp):
    limit = 180
    if systolic_bp > limit:
        return "CRITICAL"
    if systolic_bp > 140:
        return "URGENT"
    if systolic_bp > 120:
        return "ELEVATED"
    return "NORMAL"

if __name__ == "__main__":
    print(get_triage_category(200))
    print(get_triage_category(110))
