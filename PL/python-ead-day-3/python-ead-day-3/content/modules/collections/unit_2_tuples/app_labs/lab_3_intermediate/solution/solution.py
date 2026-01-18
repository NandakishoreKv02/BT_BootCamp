from collections import namedtuple

LabResult = namedtuple("LabResult", ["test_name", "value", "unit"])

glucose_test = LabResult("Glucose", 95, "mg/dL")

print(f"Test: {glucose_test.test_name}")
print(f"Result: {glucose_test.value} {glucose_test.unit}")
