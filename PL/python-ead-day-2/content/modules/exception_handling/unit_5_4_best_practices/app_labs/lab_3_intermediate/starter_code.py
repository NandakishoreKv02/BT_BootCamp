class MockHospitalLogger:
    def __init__(self):
        self.logs = []
        self.tracebacks_captured = 0

    def log_exception(self, message):
        """Simulates logging.exception()"""
        self.logs.append(f"EXCEPTION: {message}")
        self.tracebacks_captured += 1

def safe_api_call(api_func, logger):
    """
    TODO:
    1. Try running api_func().
    2. Catch ConnectionError.
    3. Use logger.log_exception("API Error occurred").
    """
    # WRITE CODE HERE
    pass

def main():
    logger = MockHospitalLogger()
    def fail(): raise ConnectionError("Timeout")
    
    safe_api_call(fail, logger)
    print(logger.logs)
    print(f"Tracebacks captured: {logger.tracebacks_captured}")

if __name__ == "__main__":
    main()
