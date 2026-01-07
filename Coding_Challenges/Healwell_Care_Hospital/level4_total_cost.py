# Level 4: Calculate Total Cost

services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

choices = list(map(int, input("Select services: ").split()))

total = 0
for choice in choices:
    total += costs[choice - 1]

print("\nTotal Cost (Before Tax): ₹", total)
