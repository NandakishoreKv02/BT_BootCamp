"""
Unit 3: Dictionaries - Exercises
Concept-focused drills testing dictionary fundamentals.
Module: Collections
"""

# ============================================================================
# Exercise 1: Dictionary Creation and Access
# ============================================================================

def exercise_1_starter():
    """
    Create a dictionary and access values by key.
    
    Objective: Master dictionary creation and key-based access
    
    Requirements:
    - Create a dictionary with 3 key-value pairs: "a": 1, "b": 2, "c": 3
    - Access the value for key "b"
    - Return the value
    
    Args:
        None
    
    Returns:
        int: The value associated with key "b"
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    # Create dict {"a": 1, "b": 2, "c": 3}
    # Access value at key "b"
    # Return it
    
    return {"a": 1, "b": 2, "c": 3}["b"]
    
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_1():
    """Test cases for Exercise 1"""
    
    # Test case 1: Correct value
    result = exercise_1_starter()
    assert result == 2, "Test 1 failed: Expected 2"
    
    # Test case 2: Type check
    assert isinstance(result, int), "Test 2 failed: Result should be an integer"
    
    # Test case 3: Value verification
    assert result > 0, "Test 3 failed: Result should be positive"


# ============================================================================
# Exercise 2: Adding and Updating Items
# ============================================================================

def exercise_2_starter(data):
    """
    Add a new item and update an existing item in a dictionary.
    
    Objective: Master dictionary modification
    
    Requirements:
    - Add a new key "z" with value 99
    - Update the existing key "x" to value 0
    - Return the modified dictionary
    
    Args:
        data (dict): Initial dictionary e.g., {"x": 10, "y": 20}
    
    Returns:
        dict: Modified dictionary
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    # Add key "z" = 99
    # Update key "x" = 0
    # Return dictionary
    
    data["z"] = 99
    data["x"] = 0
    return data
    
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_2():
    """Test cases for Exercise 2"""
    
    # Test case 1: Add and update
    initial = {"x": 10, "y": 20}
    result = exercise_2_starter(initial)
    assert result["z"] == 99, "Test 1 failed: Key 'z' should be 99"
    assert result["x"] == 0, "Test 2 failed: Key 'x' should be 0"
    
    # Test case 2: Preserves other keys
    assert result["y"] == 20, "Test 3 failed: Key 'y' should be unchanged"


# ============================================================================
# Exercise 3: Removing Items
# ============================================================================

def exercise_3_starter(data):
    """
    Remove items from a dictionary.
    
    Objective: Master dictionary item removal
    
    Requirements:
    - Remove the key "temp" using .pop()
    - Return the value that was associated with "temp"
    
    Args:
        data (dict): Dictionary containing "temp" key
    
    Returns:
        The value removed
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    # Use .pop("temp") to remove and get value
    # Return the value
    
    return data.pop("temp")
    
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_3():
    """Test cases for Exercise 3"""
    
    # Test case 1: Basic removal
    data = {"main": 1, "temp": 99}
    result = exercise_3_starter(data)
    assert result == 99, "Test 1 failed: Should return removed value"
    
    # Test case 2: Key removed
    assert "temp" not in data, "Test 2 failed: Key 'temp' should be gone"
    
    # Test case 3: Other keys remain
    assert data["main"] == 1, "Test 3 failed: Other keys should remain"


# ============================================================================
# Exercise 4: Dictionary Methods (keys, values)
# ============================================================================

def exercise_4_starter(data):
    """
    Extract keys and values from a dictionary.
    
    Objective: Master keys() and values() methods
    
    Requirements:
    - Get all keys as a list (convert view to list)
    - Get all values as a list (convert view to list)
    - Return a tuple of (list_of_keys, list_of_values)
    
    Args:
        data (dict): Input dictionary
    
    Returns:
        tuple: ([keys], [values])
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    # Get keys, convert to list
    # Get values, convert to list
    # Return (keys_list, values_list)
    
    return (list(data.keys()), list(data.values()))
    
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_4():
    """Test cases for Exercise 4"""
    
    # Test case 1: Basic keys and values
    data = {"a": 1, "b": 2}
    keys, values = exercise_4_starter(data)
    assert sorted(keys) == ["a", "b"], "Test 1 failed: Keys mismatch"
    assert sorted(values) == [1, 2], "Test 2 failed: Values mismatch"
    
    # Test case 2: Types
    assert isinstance(keys, list), "Test 3 failed: Keys should be a list"
    assert isinstance(values, list), "Test 4 failed: Values should be a list"


# ============================================================================
# Exercise 5: Safe Access with .get()
# ============================================================================

def exercise_5_starter(data, key):
    """
    Safely access dictionary values using .get().
    
    Objective: Master .get() method for safe access
    
    Requirements:
    - Use .get() to access the key
    - If key is missing, return "Not Found" (default value)
    - Do NOT use if/else or try/except
    
    Args:
        data (dict): Input dictionary
        key (str): Key to look up
    
    Returns:
        Value or "Not Found"
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    # Use data.get(key, default)
    
    return data.get(key, "Not Found")
    
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_5():
    """Test cases for Exercise 5"""
    
    # Test case 1: Key exists
    data = {"a": 100}
    assert exercise_5_starter(data, "a") == 100, "Test 1 failed: Should return value"
    
    # Test case 2: Key missing
    assert exercise_5_starter(data, "b") == "Not Found", "Test 2 failed: Should return default"
    
    # Test case 3: Empty dict
    assert exercise_5_starter({}, "a") == "Not Found", "Test 3 failed: Empty dict should return default"


# ============================================================================
# Exercise 6: Dictionary Comprehension
# ============================================================================

def exercise_6_starter(numbers):
    """
    Create a dictionary using comprehension.
    
    Objective: Master dictionary comprehensions
    
    Requirements:
    - Create a dict where keys are numbers from the list
    - Values are the square of the keys
    - Only include numbers greater than 2
    - Return the dictionary
    
    Args:
        numbers (list): List of integers
    
    Returns:
        dict: {n: n**2 for n in numbers if n > 2}
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    # Use dict comprehension: {k: v for k in list if condition}
    
    return {n: n**2 for n in numbers if n > 2}
    
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_6():
    """Test cases for Exercise 6"""
    
    # Test case 1: Filtering and mapping
    data = [1, 2, 3, 4]
    result = exercise_6_starter(data)
    assert result == {3: 9, 4: 16}, "Test 1 failed: Should be {3: 9, 4: 16}"
    
    # Test case 2: All filtered out
    assert exercise_6_starter([1, 2]) == {}, "Test 2 failed: Should be empty"
    
    # Test case 3: Check keys
    assert 2 not in result, "Test 3 failed: 2 should be excluded"


# ============================================================================
# Exercise 7: Nested Dictionaries
# ============================================================================

def exercise_7_starter():
    """
    Create and access a nested dictionary structure.
    
    Objective: Master nested dictionary access
    
    Requirements:
    - Create a nested dict: {"group1": {"id": 1}, "group2": {"id": 2}}
    - Access the "id" value inside "group2"
    - Return that id
    
    Args:
        None
    
    Returns:
        int: The id form group2
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    # Create dict
    # Access dict["group2"]["id"]
    # Return it
    
    return {"group1": {"id": 1}, "group2": {"id": 2}}["group2"]["id"]
    
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_7():
    """Test cases for Exercise 7"""
    
    # Test case 1: Correct value
    result = exercise_7_starter()
    assert result == 2, "Test 1 failed: Expected 2"
    
    # Test case 2: Type check
    assert isinstance(result, int), "Test 2 failed: Result should be int"
    
    # Test case 3: Comparison
    assert result != 1, "Test 3 failed: Should not match group1 id"


# ============================================================================
# If running as script, run tests
# ============================================================================

if __name__ == "__main__":
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
    test_exercise_5()
    test_exercise_6()
    test_exercise_7()
    print("All exercises passed!")
