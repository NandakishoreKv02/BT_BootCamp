"""
Unit 2: Tuples - Exercises
Concept-focused drills testing tuple fundamentals.
"""

# ============================================================================
# Exercise 1: Creation and Access
# ============================================================================

def exercise_1_starter(item1, item2, item3):
    """
    Create a tuple containing the three items and return the second item.
    
    Objective: Tuple creation and indexing.
    
    Requirements:
    - Create a tuple `my_tuple` with the 3 args
    - Return a tuple: (my_tuple, second_item)
    
    Args:
        item1, item2, item3: Items to pack
    
    Returns:
        (full_tuple, item_at_index_1)
    """
    # WRITE CODE HERE
    my_tuple = (item1, item2, item3)
    return (my_tuple, my_tuple[1])
    # END OF YOUR CODE


def test_exercise_1():
    """Test cases for Exercise 1"""
    result = exercise_1_starter(10, 20, 30)
    assert result == ((10, 20, 30), 20), "Test 1 failed"
    result = exercise_1_starter("a", "b", "c")
    assert result == (("a", "b", "c"), "b"), "Test 2 failed"


# ============================================================================
# Exercise 2: Unpacking
# ============================================================================

def exercise_2_starter(data_tuple):
    """
    Unpack a tuple of length 3 into three variables.
    
    Objective: Tuple unpacking.
    
    Requirements:
    - Unpack `data_tuple` into variables `a`, `b`, `c`
    - Return their sum (assuming numbers)
    
    Args:
        data_tuple: Tuple of 3 numbers
    
    Returns:
        Sum of elements
    """
    # WRITE CODE HERE
    a, b, c = data_tuple
    return a + b + c
    # END OF YOUR CODE


def test_exercise_2():
    """Test cases for Exercise 2"""
    result = exercise_2_starter((1, 2, 3))
    assert result == 6, "Test 1 failed"
    result = exercise_2_starter((10, 10, 10))
    assert result == 30, "Test 2 failed"


# ============================================================================
# Exercise 3: Single Item Tuple
# ============================================================================

def exercise_3_starter(item):
    """
    Create a single-item tuple.
    
    Objective: Syntax for single-element tuples.
    
    Requirements:
    - Return a tuple containing only `item`
    - Verify it is a tuple, not just the item
    
    Args:
        item: Any data
    
    Returns:
        Tuple
    """
    # WRITE CODE HERE
    return (item,)
    # END OF YOUR CODE


def test_exercise_3():
    """Test cases for Exercise 3"""
    result = exercise_3_starter(5)
    assert isinstance(result, tuple), "Test 1 failed: Must be tuple"
    assert result == (5,), "Test 2 failed: Value mismatch"
    assert len(result) == 1, "Test 3 failed: Length"


# ============================================================================
# Exercise 4: Tuple Methods (Count/Index)
# ============================================================================

def exercise_4_starter(data_tuple, target):
    """
    Find index of target and count of target in tuple.
    
    Objective: .index() and .count() methods.
    
    Requirements:
    - Return (index_of_first_occurrence, count_total)
    - If target not found, .index() raises Error -> Handle this? 
      Standard exercise: assume it exists for index, or catch? 
      Let's assume it exists for this basic drill.
    
    Args:
        data_tuple: Tuple to search
        target: Item to find (guaranteed to exist at least once)
    
    Returns:
        (int, int)
    """
    # WRITE CODE HERE
    return (data_tuple.index(target), data_tuple.count(target))
    # END OF YOUR CODE


def test_exercise_4():
    """Test cases for Exercise 4"""
    data = (1, 2, 3, 2, 2, 4)
    result = exercise_4_starter(data, 2)
    assert result == (1, 3), "Test 1 failed: Index 1, Count 3"
    result = exercise_4_starter((5, 5), 5)
    assert result == (0, 2), "Test 2 failed"


# ============================================================================
# Exercise 5: Immutability Workaround
# ============================================================================

def exercise_5_starter(data_tuple, new_value):
    """
    'Modify' a tuple by creating a new one with a new value appended.
    
    Objective: Concatenation to simulate modification.
    
    Requirements:
    - Return a new tuple consisting of `data_tuple` + `new_value`
    
    Args:
        data_tuple: Original tuple
        new_value: Item to append
    
    Returns:
        New larger tuple
    """
    # WRITE CODE HERE
    return data_tuple + (new_value,)
    # END OF YOUR CODE


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
