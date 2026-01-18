"""
Unit 5.1: Exception Basics - Exercises
"""

# ============================================================================
# Exercise 1: Basic Try-Except
# ============================================================================

def safe_divide(a, b):
    """
    Return a / b.
    If ZeroDivisionError occurs, return None.
    """
    # TODO: Implement try-except
    # WRITE CODE HERE
    try:
        return a / b
    except ZeroDivisionError:
        return None

def test_safe_divide():
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(5, 0) is None


# ============================================================================
# Exercise 2: Catching Multiple Exceptions
# ============================================================================

def parse_age(age_input):
    """
    Convert age_input to an integer.
    Catch ValueError (e.g. "abc") and TypeError (e.g. None).
    Return -1 if error occurs.
    """
    # TODO: Implement parsing with error handling
    # WRITE CODE HERE
    try:
        return int(age_input)
    except (ValueError, TypeError):
        return -1

def test_parse_age():
    assert parse_age("25") == 25
    assert parse_age("abc") == -1
    assert parse_age(None) == -1


# ============================================================================
# Exercise 3: Accessing Exception Details
# ============================================================================

def get_key(data, key):
    """
    Return data[key].
    If KeyError, catch as 'e' and return str(e).
    """
    # TODO: Catch and return error message
    # WRITE CODE HERE
    try:
        return data[key]
    except KeyError as e:
        return str(e)

def test_get_key():
    d = {"name": "Alice"}
    assert get_key(d, "name") == "Alice"
    # str(KeyError('age')) returns "'age'" (with quotes)
    assert "'age'" in get_key(d, "age")


# ============================================================================
# Exercise 4: The Else Clause
# ============================================================================

def validate_and_process(data):
    """
    Try converting data to list(data).
    Except TypeError: return "Invalid Type".
    Else: return len(list_data).
    """
    # TODO: Use try-except-else
    # WRITE CODE HERE
    try:
        list_data = list(data)
    except TypeError:
        return "Invalid Type"
    else:
        return len(list_data)

def test_validate_and_process():
    assert validate_and_process([1, 2]) == 2
    assert validate_and_process("abc") == 3
    assert validate_and_process(123) == "Invalid Type"


# ============================================================================
# Exercise 5: Exception Hierarchy (LookupError)
# ============================================================================

def safe_lookup(container, index_or_key):
    """
    Try accessing container[index_or_key].
    Catch LookupError (handles both Index/Key errors).
    Return "Not Found" if caught.
    """
    # TODO: Catch LookupError
    # WRITE CODE HERE
    try:
        return container[index_or_key]
    except LookupError:
        return "Not Found"

def test_safe_lookup():
    assert safe_lookup([1, 2], 5) == "Not Found"      # IndexError
    assert safe_lookup({"a": 1}, "b") == "Not Found"  # KeyError
    assert safe_lookup([1, 2], 0) == 1


# ============================================================================
# Exercise 6: Catching bare Exception
# ============================================================================

def catch_all(func):
    """
    Execute func().
    Catch 'Exception' (generic).
    Return "Caught Error" if exception occurs.
    Return "Success" otherwise.
    """
    # TODO: Implement generic catch
    # WRITE CODE HERE
    try:
        func()
        return "Success"
    except Exception:
        return "Caught Error"

def test_catch_all():
    def fail(): raise ValueError()
    def success(): return 1
    
    assert catch_all(fail) == "Caught Error"
    assert catch_all(success) == "Success"


# ============================================================================
# Exercise 7: Nested Try-Except
# ============================================================================

def complex_process(dict_list, list_index, dict_key):
    """
    Outer try: Access dict_list[list_index]. Except IndexError -> "Bad Index".
    Inner try: Access item[dict_key]. Except KeyError -> "Bad Key".
    Return value if successful.
    """
    # TODO: Implement nested try-except
    # WRITE CODE HERE
    try:
        item = dict_list[list_index]
    except IndexError:
        return "Bad Index"
    try:
        return item[dict_key]
    except KeyError:
        return "Bad Key"

def test_complex_process():
    data = [{"name": "A"}, {"name": "B"}]
    assert complex_process(data, 0, "name") == "A"
    assert complex_process(data, 5, "name") == "Bad Index"
    assert complex_process(data, 0, "age") == "Bad Key"


# ============================================================================
# Exercise 8: Handling Attribute Errors
# ============================================================================

def get_status(obj):
    """
    Return obj.status.
    Catch AttributeError -> "Unknown Status".
    """
    # TODO: Safe attribute access
    # WRITE CODE HERE
    try:
        return obj.status
    except AttributeError:
        return "Unknown Status"

def test_get_status():
    class User:
        status = "Active"
    class Guest:
        pass
        
    assert get_status(User()) == "Active"
    assert get_status(Guest()) == "Unknown Status"


if __name__ == "__main__":
    tests = [
        test_safe_divide, test_parse_age, test_get_key, test_validate_and_process,
        test_safe_lookup, test_catch_all, test_complex_process, test_get_status
    ]
    
    passed = 0
    for t in tests:
        try:
            t()
            passed += 1
            print(f"PASS: {t.__name__}")
        except AssertionError:
            print(f"FAIL: {t.__name__}")
        except Exception as e:
            print(f"ERROR: {t.__name__} - {e}")
            
    print(f"\nResult: {passed}/{len(tests)} passed.")
