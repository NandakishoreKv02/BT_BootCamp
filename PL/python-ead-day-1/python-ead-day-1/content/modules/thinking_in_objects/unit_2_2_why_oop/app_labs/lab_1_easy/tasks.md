# Lab 1 Tasks

## Task 1: Create the Config "Constructor"
Define `make_config(env)`:
- Returns a dictionary representing the Configuration.
- If `env` is "prod":
  - `hospital_name`: "City General"
  - `url`: "https://api.hospital.com"
  - `secure`: True
- If `env` is "test":
  - `hospital_name`: "Mock Hospital"
  - `url`: "http://localhost:8080"
  - `secure`: False

## Task 2: Standardize Data Access
Define `get_connection_info(config)`:
- This function should take the `config` dictionary as an argument.
- Return a formatted string: `"Connecting to [URL] for hospital [NAME] (Secure: [SECURE])"`.

## Task 3: Test Independence
In the `main()` function:
1. Create `prod_env = make_config("prod")`.
2. Create `test_env = make_config("test")`.
3. Call `get_connection_info()` for both environments.
4. Print the results to the console to prove that both objects store their settings independently.
