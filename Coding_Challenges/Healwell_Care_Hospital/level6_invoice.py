# Level 6: Invoice Generation

services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

name = input("Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
contact = input("Contact: ")

choices = list(map(int, input("Select services: ").split()))

subtotal = 0

print("\n--------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("--------------------------------")

print("\nPatient Information")
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Contact:", contact)

print("\nServices Availed:")
for i, choice in enumerate(choices):
    print(i + 1, ".", services[choice - 1], ": ₹", costs[choice - 1])
    subtotal += costs[choice - 1]

gst = subtotal * 0.18
grand_total = subtotal + gst

print("\nSubtotal: ₹", subtotal)
print("GST (18%): ₹", gst)
print("Grand Total: ₹", grand_total)
print("\nThank you for choosing HealWell Care Hospital!")
print("--------------------------------")
