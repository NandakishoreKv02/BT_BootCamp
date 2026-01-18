import json

DEFAULT_CONFIG = {"mode": "safe", "retries": 3}

def load_config(file_path):
    """
    TODO:
    1. Try to open and json.load(file_path).
    2. Handle FileNotFoundError -> Use defaults.
    3. Handle PermissionError -> Use defaults.
    4. Handle json.JSONDecodeError -> Use defaults.
    5. Return the loaded or default config.
    """
    # WRITE CODE HERE
    pass

def main():
    # You can manually create files to test this logic
    print("Loading config...")
    cfg = load_config("non_existent.json")
    print(f"Loaded: {cfg}")

if __name__ == "__main__":
    main()
