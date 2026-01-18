def calculate_with_logging(a, b, logs):
    """
    TODO:
    1. Try a / b.
    2. Catch ZeroDivisionError.
    3. Append "Zero Division Detected" to logs.
    4. Re-raise the exception.
    """
    # WRITE CODE HERE
    pass

def main():
    logs = []
    try:
        calculate_with_logging(10, 0, logs)
    except ZeroDivisionError:
        print("Caught re-raised error!")
        print(f"Logs: {logs}")

if __name__ == "__main__":
    main()
