# Level 5: GST Calculation

services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

choices = list(map(int, input("Select services: ").split()))

subtotal = 0
for choice in choices:
    subtotal += costs[choice - 1]

gst = subtotal * 0.18
grand_total = subtotal + gst

print("\nSubtotal: ₹", subtotal)
print("GST (18%): ₹", gst)
print("Grand Total: ₹", grand_total)
