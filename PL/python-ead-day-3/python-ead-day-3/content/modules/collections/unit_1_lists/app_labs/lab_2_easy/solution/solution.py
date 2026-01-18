slots = ["Patient A", "Patient B"]
slots.insert(0, "EMERGENCY")
slots.remove("Patient A")
current_patient = slots.pop(0)

print(f"Serving: {current_patient}")
print(f"Remaining: {slots}")
