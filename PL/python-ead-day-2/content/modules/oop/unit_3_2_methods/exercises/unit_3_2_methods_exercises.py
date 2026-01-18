"""
Unit 3.2: Methods - Exercises
Concept-focused drills testing instance, class, and static methods in Python.
"""

# ============================================================================
# Exercise 1: Basic Instance Method
# ============================================================================

def exercise_1_starter():
    """
    Define a class 'Tracker' with an instance variable 'total' initialized to 0.
    Implement an instance method 'add(self, value)' that updates 'total'.
    
    Objective: Master basic instance methods and 'self' state modification.
    
    Requirements:
    - Initial 'total' must be 0.
    - 'add(value)' must increment 'total' by the given value.
    - Return the Tracker instance itself (for chaining).
    
    Returns:
        The Tracker class definition.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Tracker:
        def __init__(self):
            self.total = 0
        def add(self, value):
            self.total += value
            return self
    return Tracker
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================

def test_exercise_1():
    """Test cases for Exercise 1"""
    Tracker = exercise_1_starter()
    t = Tracker()
    
    # Test case 1: Initial state
    assert t.total == 0, "Test 1 failed: Initial total should be 0"
    
    # Test case 2: Single update
    t.add(10)
    assert t.total == 10, "Test 2 failed: Total after add(10) should be 10"
    
    # Test case 3: Chaining and multiple updates
    t.add(5).add(5)
    assert t.total == 20, "Test 3 failed: Total after add(5).add(5) should be 20"


# ============================================================================
# Exercise 2: Class Method as a Factory
# ============================================================================

def exercise_2_starter():
    """
    Define a class 'Converter' with an __init__ that sets 'value'.
    Implement a @classmethod 'from_string(cls, s)' that converts a string to float.
    
    Objective: Master @classmethod for alternative constructors.
    
    Requirements:
    - __init__ sets self.value.
    - from_string(s) must return a new instance of the class.
    
    Returns:
        The Converter class definition.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Converter:
        def __init__(self, value):
            self.value = value
        @classmethod
        def from_string(cls, s):
            return cls(float(s))
    return Converter
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================

def test_exercise_2():
    """Test cases for Exercise 2"""
    Converter = exercise_2_starter()
    
    # Test case 1: Standard init
    c1 = Converter(10.5)
    assert c1.value == 10.5, "Test 1 failed: Standard init not working"
    
    # Test case 2: Class method factory
    c2 = Converter.from_string("20.5")
    assert isinstance(c2, Converter), "Test 2 failed: from_string should return instance"
    assert c2.value == 20.5, "Test 2 failed: Value from string conversion incorrect"
    
    # Test case 3: Class method identity
    assert c2.__class__ is Converter, "Test 3 failed: Instance should belong to Converter"


# ============================================================================
# Exercise 3: Static Method Utility
# ============================================================================

def exercise_3_starter():
    """
    Define a class 'Validator' with a @staticmethod 'is_positive(n)'.
    
    Objective: Master @staticmethod for independent utility logic.
    
    Requirements:
    - is_positive(n) should return True if n > 0, False otherwise.
    - Method must not take 'self' or 'cls'.
    
    Returns:
        The Validator class definition.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Validator:
        @staticmethod
        def is_positive(n):
            return n > 0
    return Validator
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================

def test_exercise_3():
    """Test cases for Exercise 3"""
    Validator = exercise_3_starter()
    
    # Test case 1: Positive number
    assert Validator.is_positive(10) is True, "Test 1 failed: 10 is positive"
    
    # Test case 2: Negative number
    assert Validator.is_positive(-5) is False, "Test 2 failed: -5 is not positive"
    
    # Test case 3: Zero
    assert Validator.is_positive(0) is False, "Test 3 failed: 0 is not positive"


# ============================================================================
# Exercise 4: Method with Default Arguments
# ============================================================================

def exercise_4_starter():
    """
    Define a class 'Formatter' with an instance method 'wrap(self, text, char="*")'.
    
    Objective: Master alternative to overloading using default arguments.
    
    Requirements:
    - wrap(text, char) should return the text surrounded by the character.
    - Default 'char' must be "*".
    
    Returns:
        The Formatter class definition.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Formatter:
        def wrap(self, text, char="*"):
            return char + text + char
    return Formatter
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================

def test_exercise_4():
    """Test cases for Exercise 4"""
    Formatter = exercise_4_starter()
    f = Formatter()
    
    # Test case 1: Using default
    assert f.wrap("hi") == "*hi*", "Test 1 failed: Default char '*' not used"
    
    # Test case 2: Providing char
    assert f.wrap("hi", "#") == "#hi#", "Test 2 failed: Custom char '#' not used"
    
    # Test case 3: Empty text
    assert f.wrap("", "-") == "--", "Test 3 failed: Empty text should be '--'"


# ============================================================================
# Exercise 5: Return Values vs Side Effects
# ============================================================================

def exercise_5_starter():
    """
    Define a class 'Buffer' that stores a list 'items'.
    Implement:
    1. 'add(self, item)': Side effect - appends to list, returns None.
    2. 'clear(self)': Side effect - empties list, returns count of items removed.
    
    Objective: Distinguish between side effects and return values.
    
    Requirements:
    - add(item) must append to self.items.
    - clear() must empty self.items and return the length BEFORE clearing.
    
    Returns:
        The Buffer class definition.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Buffer:
        def __init__(self):
            self.items = []
        def add(self, item):
            self.items.append(item)
        def clear(self):
            count = len(self.items)
            self.items = []
            return count
    return Buffer
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================

def test_exercise_5():
    """Test cases for Exercise 5"""
    Buffer = exercise_5_starter()
    b = Buffer()
    b.items = []
    
    # Test case 1: Side effect of add
    res_add = b.add("a")
    assert res_add is None, "Test 1 failed: add() should return None"
    assert b.items == ["a"], "Test 1 failed: items should contain 'a'"
    
    # Test case 2: Side effect and return value of clear
    b.add("b")
    count = b.clear()
    assert count == 2, "Test 2 failed: clear() should return removed count (2)"
    assert b.items == [], "Test 2 failed: items should be empty after clear()"
    
    # Test case 3: Clear empty
    assert b.clear() == 0, "Test 3 failed: clearing empty buffer should return 0"


# ============================================================================
# Exercise 6: Class-Level Coordination via 'cls'
# ============================================================================

def exercise_6_starter():
    """
    Define a class 'Registry' with a class variable 'entries' (list).
    Implement a @classmethod 'add_entry(cls, value)'.
    
    Objective: Master 'cls' for interacting with class-level state.
    
    Requirements:
    - 'entries' must be a list shared by all instances.
    - add_entry(value) must append the value to the class variable 'entries'.
    
    Returns:
        The Registry class definition.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Registry:
        entries = []
        @classmethod
        def add_entry(cls, value):
            cls.entries.append(value)
    return Registry
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================

def test_exercise_6():
    """Test cases for Exercise 6"""
    Registry = exercise_6_starter()
    # Reset entries for testing
    Registry.entries = []
    
    # Test case 1: Add via class
    Registry.add_entry(1)
    assert Registry.entries == [1], "Test 1 failed: Entry 1 not found in class variable"
    
    # Test case 2: Shared state check
    r1 = Registry()
    r2 = Registry()
    assert r1.entries is r2.entries, "Test 2 failed: entries list should be shared"
    
    # Test case 3: Add via instance
    r1.add_entry(2)
    assert Registry.entries == [1, 2], "Test 3 failed: Entry 2 added via instance not in class variable"


# ============================================================================
# Execution Flow
# ============================================================================

if __name__ == "__main__":
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
    test_exercise_5()
    test_exercise_6()
    print("All exercises passed!")
