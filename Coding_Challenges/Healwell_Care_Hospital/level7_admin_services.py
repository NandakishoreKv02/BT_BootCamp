# Level 7: Admin Configuration

services = []
costs = []

n = int(input("Enter number of services: "))

for i in range(n):
    service = input("Enter service name: ")
    cost = int(input("Enter cost: "))
    services.append(service)
    costs.append(cost)

print("\nServices Configured Successfully")
for i in range(n):
    print(services[i], "₹", costs[i])
