class ConnectionTimeout(Exception): pass
class ServiceUnavailable(Exception): pass

def connect_to_service():
    """
    TODO:
    1. Try to raise ConnectionTimeout("30s limit").
    2. Catch it as 'e'.
    3. Raise ServiceUnavailable("Service is down") FROM e.
    """
    # WRITE CODE HERE
    pass

def main():
    try:
        connect_to_service()
    except ServiceUnavailable as err:
        print(f"Caught: {err}")
        print(f"Caused by: {err.__cause__}")

if __name__ == "__main__":
    main()
