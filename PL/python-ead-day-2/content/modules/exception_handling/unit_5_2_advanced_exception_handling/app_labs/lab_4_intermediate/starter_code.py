def fetch_data(primary_func, backup_func):
    """
    TODO:
    1. Try primary. Return if success.
    2. Except ValueError -> Try backup. Return if success.
    3. Except ValueError -> Raise RuntimeError("All sources failed").
    """
    # WRITE CODE HERE
    pass

def main():
    def fail(): raise ValueError("Down")
    def success(): return "Data"

    print(fetch_data(success, fail)) # Data
    try:
        fetch_data(fail, fail)
    except RuntimeError as e:
        print(e) # All sources failed

if __name__ == "__main__":
    main()
