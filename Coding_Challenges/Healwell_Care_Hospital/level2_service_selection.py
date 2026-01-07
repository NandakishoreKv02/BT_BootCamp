# Level 2: Display Services and Select

services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]

name = input("Enter patient name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: ")
contact = input("Enter contact number: ")

print("\nAvailable Services:")
for i in range(len(services)):
    print(i + 1, ".", services[i])

choices = list(map(int, input("Select services (space separated): ").split()))

selected_services = []
for choice in choices:
    selected_services.append(services[choice - 1])

print("\nSelected Services:", selected_services)
