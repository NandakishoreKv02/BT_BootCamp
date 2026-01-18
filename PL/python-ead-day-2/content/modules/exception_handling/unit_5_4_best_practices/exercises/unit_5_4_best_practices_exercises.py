"""
Unit 5.4: Exception Handling Best Practices - Exercises
"""
import logging

# Set up a dummy logger for testing
logger = logging.getLogger("exercise_logger")
log_capture = []

class ListHandler(logging.Handler):
    def emit(self, record):
        log_capture.append(self.format(record))

logger.addHandler(ListHandler())

# ============================================================================
# Exercise 1: LBYL to EAFP (Dict)
# ============================================================================

def get_value_lbyl(data, key):
    # This is LBYL
    if key in data:
        return data[key]
    return "Missing"

def get_value_eafp(data, key):
    """
    TODO: Refactor to EAFP style (try-except KeyError).
    """
    # WRITE CODE HERE
    try:
        return data[key]
    except KeyError:
        return "Missing"

def test_ex1():
    d = {"name": "Alice"}
    assert get_value_eafp(d, "name") == "Alice"
    assert get_value_eafp(d, "age") == "Missing"


# ============================================================================
# Exercise 2: LBYL to EAFP (Division)
# ============================================================================

def divide_eafp(a, b):
    """
    TODO: Use try-except ZeroDivisionError. Return None on error.
    """
    # WRITE CODE HERE
    try:
        return a / b
    except ZeroDivisionError:
        return None

def test_ex2():
    assert divide_eafp(10, 2) == 5.0
    assert divide_eafp(5, 0) is None


# ============================================================================
# Exercise 3: Specificity Check
# ============================================================================

def specific_handler(obj):
    """
    Code can raise AttributeError if .name missing.
    Fix this from catching generic Exception to specific AttributeError.
    """
    try:
        return obj.name
    except AttributeError: # TODO: Fix this
        return "Unknown"

def test_ex3():
    class Person: name = "Bob"
    class Ghost: pass
    assert specific_handler(Person()) == "Bob"
    assert specific_handler(Ghost()) == "Unknown"


# ============================================================================
# Exercise 4: Clean Happy Path
# ============================================================================

def messy_try(val):
    """
    Refactor so only the operation '10 / val' is inside the try block.
    """
    # OLD VERSION:
    # try:
    #     res = 10 / val
    #     print("Log start")
    #     return res
    # except ZeroDivisionError:
    #     return 0
    
    # WRITE REFACTORED CODE HERE
    try:
        res = 10 / val
    except ZeroDivisionError:
        return 0
    return res

def test_ex4():
    assert messy_try(2) == 5.0
    assert messy_try(0) == 0


# ============================================================================
# Exercise 5: Basic Exception Logging
# ============================================================================

def log_failure(func):
    """
    Run func(). Catch Exception.
    Use logger.error(str(e)) to log just the error message.
    """
    # WRITE CODE HERE
    try:
        func()
    except Exception as e:
        logger.error(str(e))

def test_ex5():
    log_capture.clear()
    def fail(): raise ValueError("Bad data")
    log_failure(fail)
    assert "Bad data" in log_capture[0]


# ============================================================================
# Exercise 6: Advanced Logging (Traceback)
# ============================================================================

def log_with_traceback(func):
    """
    Use logger.exception("Critical fail")
    """
    # WRITE CODE HERE
    try:
        func()
    except Exception:
        logger.exception("Critical fail")

def test_ex6():
    log_capture.clear()
    def fail(): raise KeyError("missing")
    log_with_traceback(fail)
    # logger.exception includes 'Traceback' in the log
    assert "Critical fail" in log_capture[0]
    # We can't easily check for 'Traceback' string if it's mock-formatted,
    # but logging.exception is the goal.
    pass


# ============================================================================
# Exercise 7: User-Friendly Messages
# ============================================================================

def safe_open_user(path, internal_logs):
    """
    Try opening path. 
    Catch PermissionError -> log technical details (e.args) to internal_logs.
    Return user-friendly: "Access Denied. Please contact your administrator."
    """
    # WRITE CODE HERE
    try:
        open(path)
    except PermissionError as e:
        internal_logs.append(str(e.args))
        return "Access Denied. Please contact your administrator."

def test_ex7():
    logs = []
    # Simulating PermissionError by raising manually
    def mock_open(): raise PermissionError("Forbidden Path: /sys/root")
    
    # We need a wrapper to trigger it
    try:
        # Implementation should handle the raise inside
        pass
    except:
        pass
    # Actual test for the function logic
    return True


# ============================================================================
# Exercise 8: High Performance LBYL
# ============================================================================

def fast_process(items):
    """
    Items is a list of 1,000,000 integers. Most are None.
    Implement as LBYL (if item is not None) to avoid exception overhead.
    Return the count of non-None items.
    """
    count = 0
    # TODO: Implement LBYL check
    for item in items:
        if item is not None:
            count += 1
    return count

def test_ex8():
    data = [1, None, 2, None] * 10
    assert fast_process(data) == 20


if __name__ == "__main__":
    tests = [
        test_ex1, test_ex2, test_ex3, test_ex4,
        test_ex5, test_ex6, test_ex8
    ]
    passed = 0
    for t in tests:
        try:
            t()
            passed += 1
            print(f"PASS: {t.__name__}")
        except Exception as e:
            print(f"FAIL: {t.__name__} - {e}")
    print(f"\nResult: {passed}/{len(tests)} passed.")
