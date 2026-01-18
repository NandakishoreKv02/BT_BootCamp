vitals_data = (38.2, 85, 120)

temperature, heart_rate, systolic_bp = vitals_data

doc_a = "Dr. Smith"
doc_b = "Dr. Jones"

doc_a, doc_b = doc_b, doc_a

print(f"Temp: {temperature}, HR: {heart_rate}")
print(f"Swap Result - A: {doc_a}, B: {doc_b}")
