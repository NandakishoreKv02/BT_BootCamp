"""
Unit 2: Tuples - Exercises SOLUTIONS
Content: Complete working solutions
"""

# ============================================================================
# Exercise 1: Creation and Access - SOLUTION
# ============================================================================

def exercise_1_starter(item1, item2, item3):
    """
    Create a tuple containing the three items and return the second item.
    """
    my_tuple = (item1, item2, item3)
    return (my_tuple, my_tuple[1])


def test_exercise_1():
    """Test cases for Exercise 1"""
    result = exercise_1_starter(10, 20, 30)
    assert result == ((10, 20, 30), 20), "Test 1 failed"
    result = exercise_1_starter("a", "b", "c")
    assert result == (("a", "b", "c"), "b"), "Test 2 failed"


# ============================================================================
# Exercise 2: Unpacking - SOLUTION
# ============================================================================

def exercise_2_starter(data_tuple):
    """
    Unpack a tuple of length 3 into three variables.
    """
    a, b, c = data_tuple
    return a + b + c


def test_exercise_2():
    """Test cases for Exercise 2"""
    result = exercise_2_starter((1, 2, 3))
    assert result == 6, "Test 1 failed"
    result = exercise_2_starter((10, 10, 10))
    assert result == 30, "Test 2 failed"


# ============================================================================
# Exercise 3: Single Item Tuple - SOLUTION
# ============================================================================

def exercise_3_starter(item):
    """
    Create a single-item tuple.
    """
    return (item,)


def test_exercise_3():
    """Test cases for Exercise 3"""
    result = exercise_3_starter(5)
    assert isinstance(result, tuple), "Test 1 failed: Must be tuple"
    assert result == (5,), "Test 2 failed: Value mismatch"
    assert len(result) == 1, "Test 3 failed: Length"


# ============================================================================
# Exercise 4: Tuple Methods (Count/Index) - SOLUTION
# ============================================================================

def exercise_4_starter(data_tuple, target):
    """
    Find index of target and count of target in tuple.
    """
    idx = data_tuple.index(target)
    count = data_tuple.count(target)
    return (idx, count)


def test_exercise_4():
    """Test cases for Exercise 4"""
    data = (1, 2, 3, 2, 2, 4)
    result = exercise_4_starter(data, 2)
    assert result == (1, 3), "Test 1 failed: Index 1, Count 3"
    result = exercise_4_starter((5, 5), 5)
    assert result == (0, 2), "Test 2 failed"


# ============================================================================
# Exercise 5: Immutability Workaround - SOLUTION
# ============================================================================

def exercise_5_starter(data_tuple, new_value):
    """
    'Modify' a tuple by creating a new one with a new value appended.
    """
    return data_tuple + (new_value,)


def test_exercise_5():
    """Test cases for Exercise 5"""
    result = exercise_5_starter((1, 2), 3)
    assert result == (1, 2, 3), "Test 1 failed"
    result = exercise_5_starter((), "a")
    assert result == ("a",), "Test 2 failed"


# ============================================================================
# Main Test Runner
# ============================================================================

if __name__ == "__main__":
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
    test_exercise_5()
    print("All exercises passed!")
