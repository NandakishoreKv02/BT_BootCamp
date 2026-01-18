"""
Unit 3: Dictionaries - Exercises SOLUTIONS
Complete solutions for all dictionary exercises.
Module: Collections
"""

# ============================================================================
# Exercise 1: Dictionary Creation and Access - SOLUTION
# ============================================================================

def exercise_1_starter():
    """Create a dictionary and access values by key."""
    # Create dict
    data = {"a": 1, "b": 2, "c": 3}
    
    # Access value at key "b"
    value = data["b"]
    
    return value


def test_exercise_1():
    """Test cases for Exercise 1"""
    result = exercise_1_starter()
    assert result == 2, "Test 1 failed"
    assert isinstance(result, int), "Test 2 failed"
    assert result > 0, "Test 3 failed"
    print("✓ Exercise 1 passed")


# ============================================================================
# Exercise 2: Adding and Updating Items - SOLUTION
# ============================================================================

def exercise_2_starter(data):
    """Add a new item and update an existing item."""
    # Add key "z"
    data["z"] = 99
    
    # Update key "x"
    data["x"] = 0
    
    return data


def test_exercise_2():
    """Test cases for Exercise 2"""
    initial = {"x": 10, "y": 20}
    result = exercise_2_starter(initial)
    assert result["z"] == 99, "Test 1 failed"
    assert result["x"] == 0, "Test 2 failed"
    assert result["y"] == 20, "Test 3 failed"
    print("✓ Exercise 2 passed")


# ============================================================================
# Exercise 3: Removing Items - SOLUTION
# ============================================================================

def exercise_3_starter(data):
    """Remove items from a dictionary."""
    # Use .pop() to remove and get value
    removed_value = data.pop("temp")
    
    return removed_value


def test_exercise_3():
    """Test cases for Exercise 3"""
    data = {"main": 1, "temp": 99}
    result = exercise_3_starter(data)
    assert result == 99, "Test 1 failed"
    assert "temp" not in data, "Test 2 failed"
    assert data["main"] == 1, "Test 3 failed"
    print("✓ Exercise 3 passed")


# ============================================================================
# Exercise 4: Dictionary Methods (keys, values) - SOLUTION
# ============================================================================

def exercise_4_starter(data):
    """Extract keys and values from a dictionary."""
    # Get keys and convert to list
    keys_list = list(data.keys())
    
    # Get values and convert to list
    values_list = list(data.values())
    
    return (keys_list, values_list)


def test_exercise_4():
    """Test cases for Exercise 4"""
    data = {"a": 1, "b": 2}
    keys, values = exercise_4_starter(data)
    assert sorted(keys) == ["a", "b"], "Test 1 failed"
    assert sorted(values) == [1, 2], "Test 2 failed"
    assert isinstance(keys, list), "Test 3 failed"
    assert isinstance(values, list), "Test 4 failed"
    print("✓ Exercise 4 passed")


# ============================================================================
# Exercise 5: Safe Access with .get() - SOLUTION
# ============================================================================

def exercise_5_starter(data, key):
    """Safely access dictionary values using .get()."""
    # Use data.get(key, default)
    result = data.get(key, "Not Found")
    
    return result


def test_exercise_5():
    """Test cases for Exercise 5"""
    data = {"a": 100}
    assert exercise_5_starter(data, "a") == 100, "Test 1 failed"
    assert exercise_5_starter(data, "b") == "Not Found", "Test 2 failed"
    assert exercise_5_starter({}, "a") == "Not Found", "Test 3 failed"
    print("✓ Exercise 5 passed")


# ============================================================================
# Exercise 6: Dictionary Comprehension - SOLUTION
# ============================================================================

def exercise_6_starter(numbers):
    """Create a dictionary using comprehension."""
    # Dict comprehension: {k: v for k in list if condition}
    result = {n: n**2 for n in numbers if n > 2}
    
    return result


def test_exercise_6():
    """Test cases for Exercise 6"""
    data = [1, 2, 3, 4]
    result = exercise_6_starter(data)
    assert result == {3: 9, 4: 16}, "Test 1 failed"
    assert exercise_6_starter([1, 2]) == {}, "Test 2 failed"
    assert 2 not in result, "Test 3 failed"
    print("✓ Exercise 6 passed")


# ============================================================================
# Exercise 7: Nested Dictionaries - SOLUTION
# ============================================================================

def exercise_7_starter():
    """Create and access a nested dictionary structure."""
    # Create structure
    data = {
        "group1": {"id": 1},
        "group2": {"id": 2}
    }
    
    # Access nested value
    group2_id = data["group2"]["id"]
    
    return group2_id


def test_exercise_7():
    """Test cases for Exercise 7"""
    result = exercise_7_starter()
    assert result == 2, "Test 1 failed"
    assert isinstance(result, int), "Test 2 failed"
    assert result != 1, "Test 3 failed"
    print("✓ Exercise 7 passed")


# ============================================================================
# Run all tests
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Unit 3: Dictionaries - Exercises SOLUTIONS")
    print("=" * 80)
    
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
    test_exercise_5()
    test_exercise_6()
    test_exercise_7()
    
    print("\n" + "=" * 80)
    print("All exercises passed!")
    print("=" * 80)
