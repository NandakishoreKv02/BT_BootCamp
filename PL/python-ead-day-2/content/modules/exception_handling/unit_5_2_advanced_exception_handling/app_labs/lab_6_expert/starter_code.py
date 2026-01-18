class ServiceError(Exception):
    pass

def route_request(func):
    """
    TODO:
    1. Try running func(). Return "Success" if ok.
    2. Catch ServiceError as e.
    3. Inspect e.args[0] (the code).
    4. Return "Retry" (503), "Abort" (404), "Refresh" (401), or "Unknown".
    """
    # WRITE CODE HERE
    pass

def main():
    def fail_503(): raise ServiceError(503, "Unavailable")
    print(route_request(fail_503)) # "Retry"

if __name__ == "__main__":
    main()
