study_data = ("Project-X", [10, 20, 30])

try:
    study_data[1] = [40, 50]
except TypeError as e:
    print(f"Caught expected error: {e}")

study_data[1].append(40)
print(f"Modified Study Data: {study_data}")
