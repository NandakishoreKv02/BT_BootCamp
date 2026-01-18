"""
Unit 5.2: Advanced Exception Handling - Exercises
"""

# ============================================================================
# Exercise 1: The Finally Block
# ============================================================================

def process_and_clean(data, flags_dict):
    """
    Check if data is a list. If not, raise TypeError.
    In finally, set flags_dict['cleaned'] = True.
    """
    # TODO: Implement try-finally
    # WRITE CODE HERE
    try:
        if not isinstance(data, list):
            raise TypeError()
    finally:
        flags_dict['cleaned'] = True

def test_process_and_clean():
    flags = {"cleaned": False}
    try:
        process_and_clean("not list", flags)
    except TypeError:
        pass
    assert flags["cleaned"] is True
    
    flags["cleaned"] = False
    process_and_clean([], flags)
    assert flags["cleaned"] is True


# ============================================================================
# Exercise 2: Re-raising Exceptions
# ============================================================================

def log_and_rethrow(func, log_list):
    """
    Run func().
    Except ValueError: append "Logging Error" to log_list, then RE-RAISE.
    """
    # TODO: Implement re-raise
    # WRITE CODE HERE
    try:
        func()
    except ValueError:
        log_list.append("Logging Error")
        raise

def test_log_and_rethrow():
    logs = []
    def fail(): raise ValueError("Boom")
    
    try:
        log_and_rethrow(fail, logs)
        assert False, "Should have re-raised"
    except ValueError:
        assert logs == ["Logging Error"]


# ============================================================================
# Exercise 3: Exception Chaining
# ============================================================================

def connect_db():
    """
    Simulate TimeoutError.
    Catch it and raise RuntimeError("DB Failed") FROM the timeout error.
    """
    # TODO: Implement chaining
    # WRITE CODE HERE
    try:
        raise TimeoutError()
    except TimeoutError as e:
        raise RuntimeError("DB Failed") from e

def test_connect_db():
    try:
        connect_db()
    except RuntimeError as e:
        assert str(e) == "DB Failed"
        assert isinstance(e.__cause__, TimeoutError)


# ============================================================================
# Exercise 4: Nested Try-Except
# ============================================================================

def redundant_fetch(primary_ok, backup_ok):
    """
    Outer: try primary. If fails (ValueError),
    Inner: try backup. If fails (ValueError), return "All Failed".
    If primary succeeds, return "Primary".
    If backup succeeds, return "Backup".
    (Simulate failure by checking the bool args and raising ValueError manually)
    """
    def fetch_primary():
        if not primary_ok: raise ValueError()
        
    def fetch_backup():
        if not backup_ok: raise ValueError()
        
    # TODO: Implement nested structure
    # WRITE CODE HERE
    try:
        fetch_primary()
        return "Primary"
    except ValueError:
        try:
            fetch_backup()
            return "Backup"
        except ValueError:
            return "All Failed"

def test_redundant_fetch():
    assert redundant_fetch(True, True) == "Primary"
    assert redundant_fetch(False, True) == "Backup"
    assert redundant_fetch(False, False) == "All Failed"


# ============================================================================
# Exercise 5: Context Manager (File)
# ============================================================================

def read_file_safe(path):
    """
    Use 'with open(...)'. Read and return content.
    Catch FileNotFoundError -> return None.
    """
    # TODO: Implement with statement
    # WRITE CODE HERE
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return None

def test_read_file_safe():
    # Write a temp file
    with open("temp.txt", "w") as f: f.write("hello")
    try:
        assert read_file_safe("temp.txt") == "hello"
        assert read_file_safe("missing.txt") is None
    finally:
        import os
        if os.path.exists("temp.txt"): os.remove("temp.txt")


# ============================================================================
# Exercise 6: Inspecting Exception Objects
# ============================================================================

def get_error_code(func):
    """
    Run func(). Catch ValueError.
    Return the first arg of the exception (e.args[0]).
    If no error, return None.
    """
    # TODO: Access exception args
    # WRITE CODE HERE
    try:
        func()
        return None
    except ValueError as e:
        return e.args[0]

def test_get_error_code():
    def fail(): raise ValueError(404)
    assert get_error_code(fail) == 404
    
    def success(): pass
    assert get_error_code(success) is None


# ============================================================================
# Exercise 7: Try-Except-Else-Finally
# ============================================================================

def full_flow(val, log_list):
    """
    Try: 10 / val.
    Except ZeroDivisionError: return "Error".
    Else: return "Success".
    Finally: append "Done" to log_list.
    """
    # TODO: Implement full flow
    # WRITE CODE HERE
    try:
        10 / val
    except ZeroDivisionError:
        return "Error"
    else:
        return "Success"
    finally:
        log_list.append("Done")

def test_full_flow():
    logs = []
    assert full_flow(2, logs) == "Success"
    assert logs == ["Done"]
    
    logs = []
    assert full_flow(0, logs) == "Error"
    assert logs == ["Done"]


# ============================================================================
# Exercise 8: Catching Custom Errors
# ============================================================================

class MyError(Exception): pass

def trigger_and_catch():
    """
    Raise MyError. Catch it and return "Caught Custom".
    """
    # TODO: Raise and catch custom
    # WRITE CODE HERE
    try:
        raise MyError()
    except MyError:
        return "Caught Custom"

def test_trigger_and_catch():
    assert trigger_and_catch() == "Caught Custom"


if __name__ == "__main__":
    tests = [
        test_process_and_clean, test_log_and_rethrow, test_connect_db,
        test_redundant_fetch, test_read_file_safe, test_get_error_code,
        test_full_flow, test_trigger_and_catch
    ]
    
    passed = 0
    for t in tests:
        try:
            t()
            passed += 1
            print(f"PASS: {t.__name__}")
        except AssertionError as e:
            print(f"FAIL: {t.__name__} - {e}")
        except Exception as e:
            print(f"ERROR: {t.__name__} - {e}")
            
    print(f"\nResult: {passed}/{len(tests)} passed.")
