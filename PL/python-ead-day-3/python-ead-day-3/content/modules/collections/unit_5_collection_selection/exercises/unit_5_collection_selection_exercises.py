"""
Unit 5: Collection Selection Guide - Exercises
Concept-focused drills testing implementation and selection of collections.
"""

# ============================================================================
# Exercise 1: Search Optimization (List to Set)
# ============================================================================

def exercise_1_starter(large_list, search_items):
    """
    Given a large list and a list of items to search for, verify presence efficiently.
    
    Objective: Master performance optimization via set conversion.
    
    Requirements:
    - Convert `large_list` to a set for fast lookup.
    - Return a count of how many `search_items` were found in the collection.
    
    Args:
        large_list: List containing 1000s of items.
        search_items: List of target items to find.
    
    Returns:
        int: Total number of matches.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    s = set(large_list)
    return sum(1 for item in search_items if item in s)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_1():
    """Test cases for Exercise 1"""
    data = [1, 2, 3, 4, 5]
    targets = [2, 5, 99]
    result = exercise_1_starter(data, targets)
    assert result == 2, f"Failed basic check. Expected 2, got {result}"
    
    result = exercise_1_starter([], [1, 2])
    assert result == 0, "Failed empty list check."


# ============================================================================
# Exercise 2: Memory Optimization (Safety)
# ============================================================================

def exercise_2_starter(items_list):
    """
    Convert a mutable list into an immutable structure to prevent further changes.
    
    Objective: Understand data safety and memory efficiency.
    
    Requirements:
    - Convert `items_list` to a tuple.
    - Return the resulting tuple.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return tuple(items_list)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_2():
    """Test cases for Exercise 2"""
    data = [1, 2, 3]
    result = exercise_2_starter(data)
    assert isinstance(result, tuple), "Result must be a tuple"
    assert result == (1, 2, 3), "Values mismatch"


# ============================================================================
# Exercise 3: Deduplication with Sorting
# ============================================================================

def exercise_3_starter(data_with_duplicates):
    """
    Remove duplicates and return the items sorted in ascending order.
    
    Objective: Combine set uniqueness with list ordering.
    
    Requirements:
    - Use a set for deduplication.
    - Convert back to a list and sort.
    - Return sorted list.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return sorted(set(data_with_duplicates))
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_3():
    """Test cases for Exercise 3"""
    data = [3, 1, 2, 3, 1]
    result = exercise_3_starter(data)
    assert result == [1, 2, 3], "Failed deduplication or sorting"
    assert isinstance(result, list), "Result must be a list"


# ============================================================================
# Exercise 4: Parallel Data Mapping
# ============================================================================

def exercise_4_starter(keys, values):
    """
    Map two lists of equal length into a single lookup table.
    
    Objective: Master dictionary creation from parallel sequences.
    
    Requirements:
    - Pair elements from `keys` and `values`.
    - Return a dictionary where keys map to values.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return dict(zip(keys, values))
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_4():
    """Test cases for Exercise 4"""
    k = ["a", "b", "c"]
    v = [1, 2, 3]
    result = exercise_4_starter(k, v)
    assert result == {"a": 1, "b": 2, "c": 3}, "Dict mapping failed"


# ============================================================================
# Exercise 5: Grouping Unique Values
# ============================================================================

def exercise_5_starter(words):
    """
    Find unique lengths of words present in a list.
    
    Objective: Use Set Comprehension.
    
    Requirements:
    - Return a set of lengths (integers) for all words in the input.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return {len(word) for word in words}
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_5():
    """Test cases for Exercise 5"""
    words = ["cat", "dog", "apple", "cat"]
    result = exercise_5_starter(words)
    assert result == {3, 5}, "Failed to find unique lengths"
    assert isinstance(result, set)


# ============================================================================
# Exercise 6: Verifying Hashability
# ============================================================================

def exercise_6_starter(item):
    """
    Verify if an item can be used as a set element (is hashable).
    
    Objective: Understand constraints of collection types.
    
    Requirements:
    - Try to add `item` to a temporary set.
    - Return True if successful, False if a TypeError occurs.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    try:
        {item}
        return True
    except TypeError:
        return False
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_6():
    """Test cases for Exercise 6"""
    assert exercise_6_starter("hello") is True, "String should be hashable"
    assert exercise_6_starter([1, 2]) is False, "List should not be hashable"
    assert exercise_6_starter((1, 2)) is True, "Tuple should be hashable"


# ============================================================================
# Exercise 7: The Selection Helper
# ============================================================================

def exercise_7_starter(needs_order, needs_uniqueness, needs_key_lookup):
    """
    Recommend a collection type based on requirements.
    
    Objective: Internalize the selection logic.
    
    Requirements:
    - If `needs_key_lookup` is True -> return "dict"
    - If `needs_uniqueness` is True -> return "set"
    - If `needs_order` is True -> return "list"
    - Default -> return "list"
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    if needs_key_lookup:
        return "dict"
    if needs_uniqueness:
        return "set"
    return "list"
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_7():
    """Test cases for Exercise 7"""
    assert exercise_7_starter(False, False, True) == "dict"
    assert exercise_7_starter(True, True, False) == "set" # Uniqueness prioritized over order
    assert exercise_7_starter(True, False, False) == "list"


# ============================================================================
# Main Runner
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
