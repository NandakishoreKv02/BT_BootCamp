"""
Lab 1: Emergency Room Queue - Starter Code
"""

def arrive_patient(queue, name):
    """Add a patient to the end of the queue."""
    queue.append(name)

def see_next_patient(queue):
    """Remove and return the first patient in line."""
    if queue:
        return queue.pop(0)
    return None

def get_queue_length(queue):
    """Return how many patients are waiting."""
    return len(queue)

if __name__ == "__main__":
    er_queue = []
    arrive_patient(er_queue, "Alice")
    arrive_patient(er_queue, "Bob")
    print(f"Waiting: {get_queue_length(er_queue)}")
    print(f"Seeing: {see_next_patient(er_queue)}")
    print(f"Seeing: {see_next_patient(er_queue)}")
