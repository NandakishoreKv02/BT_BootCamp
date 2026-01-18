def calculate_avg_vitals_bloated(total, count):
    """
    STAY AWAY FROM THIS STYLE.
    It catches everything and wraps too much code.
    """
    try:
        print("Calculating heartbeat average...")
        avg = total / count
        print(f"Calculation successful: {avg}")
        return avg
    except Exception:
        print("An error occurred")
        return None

def calculate_avg_vitals_clean(total, count):
    """
    TODO: Refactor using Best Practices:
    1. Only put the division (total / count) in the try block.
    2. Catch only ZeroDivisionError.
    3. Return 0 on ZeroDivisionError.
    4. Move the print("Calculation successful") logic AFTER the try block.
    """
    # WRITE CODE HERE
    pass

def main():
    print(calculate_avg_vitals_clean(100, 5))
    print(calculate_avg_vitals_clean(100, 0))

if __name__ == "__main__":
    main()
