"""
Lab 3: Pediatric Multi-Dose Calculator - Starter Code
"""

# TODO: Define calculate_dosage(mg_per_kg, weight, daily_doses, precision=2)
def calculate_dosage(mg_per_kg, weight, daily_doses, precision=2):
    return round((mg_per_kg * weight) / daily_doses, precision)

if __name__ == "__main__":
    # TODO: Call using keyword arguments
    result = calculate_dosage(weight=15, mg_per_kg=10, daily_doses=3)
    print(result)
