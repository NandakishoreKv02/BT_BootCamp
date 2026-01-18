"""
Unit 5.3: Custom Exceptions - Exercises
"""

# ============================================================================
# Exercise 1: Basic Definition
# ============================================================================

# TODO: Define InvalidStateError
class InvalidStateError(Exception):
    pass

def check_state(state):
    """
    If state == "STOPPED", raise InvalidStateError.
    """
    # WRITE CODE HERE
    if state == "STOPPED":
        raise InvalidStateError()

def test_basic_definition():
    try:
        check_state("STOPPED")
        assert False, "Should have raised InvalidStateError"
    except Exception as e:
        # Check class name match
        assert type(e).__name__ == "InvalidStateError"


# ============================================================================
# Exercise 2: Custom Message
# ============================================================================

# TODO: Define ValidationFailure
class ValidationFailure(Exception):
    pass

def validate_length(text, min_len):
    """
    If len(text) < min_len, raise ValidationFailure(f"Text too short: {len(text)} < {min_len}")
    """
    # WRITE CODE HERE
    if len(text) < min_len:
        raise ValidationFailure(f"Text too short: {len(text)} < {min_len}")

def test_custom_message():
    try:
        validate_length("Hi", 5)
        assert False
    except Exception as e:
        assert str(e) == "Text too short: 2 < 5"


# ============================================================================
# Exercise 3: Exception Attributes
# ============================================================================

# TODO: Define HttpError with self.code
class HttpError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code

def fake_fetch(url):
    """
    If url == "bad", raise HttpError(404, "Not Found")
    """
    # WRITE CODE HERE
    if url == "bad":
        raise HttpError(404, "Not Found")

def test_exception_attributes():
    try:
        fake_fetch("bad")
    except Exception as e:
        # Check custom attribute
        if hasattr(e, 'code'):
            assert e.code == 404
        else:
            assert False, "Missing 'code' attribute"


# ============================================================================
# Exercise 4: Inheritance Hierarchy
# ============================================================================

# TODO: Define AppError, AuthError, AccessDeniedError
class AppError(Exception):
    pass

class AuthError(AppError):
    pass

class AccessDeniedError(AppError):
    pass

def login(user):
    """
    If user == "guest", raise AuthError.
    If user == "banned", raise AccessDeniedError.
    """
    # WRITE CODE HERE
    if user == "guest":
        raise AuthError()
    if user == "banned":
        raise AccessDeniedError()

def test_hierarchy():
    # Test catching base class
    caught = False
    try:
        login("guest")
    except Exception as e: # We can't reference AppError yet if not defined
        # We'll rely on the class name for the exercise test validation
        # In real code, you'd catch AppError
        if type(e).__name__ in ["AuthError", "AccessDeniedError"]:
            caught = True
    assert caught


# ============================================================================
# Exercise 5: Calling Super
# ============================================================================

# TODO: Define DetailedError calling super().__init__
class DetailedError(Exception):
    def __init__(self, msg, details):
        super().__init__(msg)
        self.details = details

def create_detailed_error():
    """
    Raise DetailedError("Boom", {"reason": "testing"})
    """
    # WRITE CODE HERE
    # Just defining the class is enough, this helper is for running it
    raise DetailedError("Boom", {"reason": "testing"})

def test_calling_super():
    try:
        # This assumes DetailedError is defined
        # We need a dynamic check if class exists
        if 'DetailedError' not in globals(): return # Skip if not implemented
        raise globals()['DetailedError']("Boom", {"reason": "test"})
    except Exception as e:
        assert str(e) == "Boom"
        assert e.details["reason"] == "test"


# ============================================================================
# Exercise 6: Catching Specifics
# ============================================================================

def handle_login_attempt(user):
    """
    Call login(user) (from Ex 4).
    Catch AuthError -> return "Auth Failed"
    Catch AccessDeniedError -> return "Access Denied"
    Catch AppError -> return "Generic"
    """
    # WRITE CODE HERE
    try:
        login(user)
    except AuthError:
        return "Auth Failed"
    except AccessDeniedError:
        return "Access Denied"
    except AppError:
        return "Generic"

def test_catching_specifics():
    # Only run if classes exist
    if 'AuthError' not in globals(): return 
    assert handle_login_attempt("guest") == "Auth Failed"
    assert handle_login_attempt("banned") == "Access Denied"


# ============================================================================
# Exercise 7: Re-raising Custom
# ============================================================================

# TODO: Define ParseError
class ParseError(Exception):
    pass

def safe_parse(text):
    """
    Try int(text). Except ValueError -> raise ParseError from e.
    """
    # WRITE CODE HERE
    try:
        return int(text)
    except ValueError as e:
        raise ParseError() from e

def test_reraise_custom():
    try:
        safe_parse("abc")
    except Exception as e:
        assert type(e).__name__ == "ParseError"
        assert isinstance(e.__cause__, ValueError)


# ============================================================================
# Exercise 8: String Representation
# ============================================================================

# TODO: Define UserError with __str__ override
class UserError(Exception):
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __str__(self):
        return f"Error for User {self.user_id}"

def raise_user_error():
    # Raise UserError(123)
    raise UserError(123)

def test_str_representation():
    try:
        # if UserError not defined, skip
        if 'UserError' not in globals(): return
        raise globals()['UserError'](123)
    except Exception as e:
        assert str(e) == "Error for User 123"


if __name__ == "__main__":
    tests = [
        test_basic_definition, test_custom_message, test_exception_attributes,
        test_hierarchy, test_calling_super, test_catching_specifics,
        test_reraise_custom, test_str_representation
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
