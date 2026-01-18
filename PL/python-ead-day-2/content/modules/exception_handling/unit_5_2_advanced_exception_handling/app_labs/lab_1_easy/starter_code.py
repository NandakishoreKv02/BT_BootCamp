class MockDB:
    def __init__(self):
        self.is_locked = False

def execute_transaction(db, func):
    """
    TODO:
    1. Lock the db.
    2. Try running func().
    3. Finally unlock the db.
    """
    # WRITE CODE HERE
    pass

def main():
    db = MockDB()
    
    # Test Success
    def success(): print("Transaction success")
    execute_transaction(db, success)
    print(f"DB Locked? {db.is_locked}") # Should be False
    
    # Test Failure
    def fail(): raise ValueError("Crash")
    try:
        execute_transaction(db, fail)
    except ValueError:
        print("Caught expected crash")
    print(f"DB Locked? {db.is_locked}") # Should be False

if __name__ == "__main__":
    main()
