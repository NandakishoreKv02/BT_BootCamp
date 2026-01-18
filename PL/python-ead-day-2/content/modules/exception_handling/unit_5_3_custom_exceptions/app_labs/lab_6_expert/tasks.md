# Lab 6 Tasks

## Task 1: The Hierarchy
Define 3 levels of exceptions:
1.  **Level 1**: `HealthNetworkError` (Base for everything).
2.  **Level 2**: `DataStackError` and `ConnectivityError` (Inherit from Level 1).
3.  **Level 3**:
    - `DatabaseLockError` (Inherit from `DataStackError`).
    - `PeerTimeoutError` (Inherit from `ConnectivityError`).

## Task 2: Service Simulation
Implement mock services:
- `db_service()`: Raises `DatabaseLockError("DB Busy")`.
- `api_service()`: Raises `PeerTimeoutError("Remote Lag")`.

## Task 3: The Orchestrator
Implement `sync_system(service_type)`:
- Call `db_service` if type is "database".
- Call `api_service` if type is "network".
- **Handler Strategy**:
    - Catch `DataStackError`: return "Data Layer Failure".
    - Catch `ConnectivityError`: return "Network Layer Failure".
    - Catch `HealthNetworkError`: return "General Platform Failure".
