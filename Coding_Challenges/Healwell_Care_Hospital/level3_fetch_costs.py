# Level 3: Fetch Costs of Selected Services

services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

print("\nAvailable Services:")
for i in range(len(services)):
    print(i + 1, ".", services[i])

choices = list(map(int, input("Select services: ").split()))

selected_services = []
selected_costs = []

for choice in choices:
    selected_services.append(services[choice - 1])
    selected_costs.append(costs[choice - 1])

print("\nSelected Services:", selected_services)
print("Selected Costs:", selected_costs)
