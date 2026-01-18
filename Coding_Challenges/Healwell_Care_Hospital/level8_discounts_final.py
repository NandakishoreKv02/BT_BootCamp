# Level 8: Discounts + GST + Final Invoice

services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

name = input("Name: ")
age = int(input("Age: "))
gender = input("Gender: ")
contact = input("Contact: ")

choices = list(map(int, input("Select services: ").split()))

subtotal = 0
for choice in choices:
    subtotal += costs[choice - 1]

# Senior citizen discount
if age >= 60:
    subtotal *= 0.90

# High bill discount
if subtotal > 5000:
    subtotal *= 0.95

gst = subtotal * 0.18
grand_total = subtotal + gst

print("\nFinal Invoice")
print("Subtotal after discounts: ₹", subtotal)
print("GST (18%): ₹", gst)
print("Grand Total: ₹", grand_total)
