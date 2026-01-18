class HealthNetworkError(Exception): pass
class DataStackError(HealthNetworkError): pass
class ConnectivityError(HealthNetworkError): pass
class DatabaseLockError(DataStackError): pass
class PeerTimeoutError(ConnectivityError): pass

def db_service():
    """TODO: Raise DatabaseLockError."""
    pass

def api_service():
    """TODO: Raise PeerTimeoutError."""
    pass

def sync_system(service_type):
    """
    TODO:
    1. Try running requested service.
    2. Catch DataStackError -> "Data Layer Failure".
    3. Catch ConnectivityError -> "Network Layer Failure".
    4. Catch HealthNetworkError -> "General Platform Failure".
    """
    # WRITE CODE HERE
    pass

def main():
    print(sync_system("database")) # Data Layer Failure
    print(sync_system("network")) # Network Layer Failure

if __name__ == "__main__":
    main()
