queue = ["Alice", "Bob", "Emergency", "Alice", "Charlie", "Emergency"]

alice_count = queue.count("Alice")
emergency_index = queue.index("Emergency")
is_john_present = "John" in queue
second_emergency_index = queue.index("Emergency", emergency_index + 1)

print(f"Alice Count: {alice_count}")
print(f"First Emergency: {emergency_index}")
print(f"Is John there? {is_john_present}")
print(f"Second Emergency: {second_emergency_index}")
