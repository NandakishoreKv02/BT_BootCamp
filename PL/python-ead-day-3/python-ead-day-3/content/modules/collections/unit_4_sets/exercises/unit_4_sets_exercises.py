"""
Unit 4: Sets - Exercises
Concept-focused drills testing implementation of set fundamentals.
"""

# ============================================================================
# Exercise 1: Set Creation and Deduplication
# ============================================================================

def exercise_1_starter(items):
    """
    Convert an iterable to a set and return the number of unique elements.
    
    Objective: Master set creation and automatic deduplication.
    
    Requirements:
    - Convert `items` to a set.
    - Return the count of unique elements in that set.
    
    Args:
        items: An iterable (list, tuple, etc.)
    
    Returns:
        Integer count of unique items.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return len(set(items))
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_1():
    """Test cases for Exercise 1"""
    
    # Test case 1: List with duplicates
    result = exercise_1_starter([1, 2, 2, 3, 3, 3])
    assert result == 3, f"Failed for [1, 2, 2, 3, 3, 3]. Expected 3, got {result}"
    
    # Test case 2: Empty list
    result = exercise_1_starter([])
    assert result == 0, f"Failed for empty list. Expected 0, got {result}"
    
    # Test case 3: String (unique characters)
    result = exercise_1_starter("abracadabra")
    assert result == 5, f"Failed for 'abracadabra'. Expected 5, got {result}"


# ============================================================================
# Exercise 2: Basic Set Operations (Add and Discard)
# ============================================================================

def exercise_2_starter(initial_set, to_add, to_remove):
    """
    Perform add and discard operations on a set.
    
    Objective: Master basic set modification methods.
    
    Requirements:
    - Add `to_add` to the set.
    - Remove `to_remove` from the set safely (don't raise error if missing).
    - Return the modified set.
    
    Args:
        initial_set: The starting set.
        to_add: Item to add.
        to_remove: Item to discard.
    
    Returns:
        The modified set.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    initial_set.add(to_add)
    initial_set.discard(to_remove)
    return initial_set
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_2():
    """Test cases for Exercise 2"""
    
    # Test case 1: Normal add and remove
    result = exercise_2_starter({1, 2, 3}, 4, 2)
    assert result == {1, 3, 4}, "Failed for normal add/remove"
    
    # Test case 2: Discarding non-existent item
    result = exercise_2_starter({1, 2}, 3, 99)
    assert result == {1, 2, 3}, "Failed: Should handle missing item safely"
    
    # Test case 3: Adding existing item
    result = exercise_2_starter({1, 2}, 2, 1)
    assert result == {2}, "Failed: Adding existing item should not change set"


# ============================================================================
# Exercise 3: Union and Intersection
# ============================================================================

def exercise_3_starter(set_a, set_b):
    """
    Calculate the union and intersection of two sets.
    
    Objective: Master Venn diagram logic using operators.
    
    Requirements:
    - Return a tuple containing: (union_result, intersection_result)
    - Use symbolic operators (`|` and `&`).
    
    Args:
        set_a: First set.
        set_b: Second set.
    
    Returns:
        Tuple of (set_union, set_intersection).
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return (set_a | set_b, set_a & set_b)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_3():
    """Test cases for Exercise 3"""
    
    # Test case 1: Overlapping sets
    u, i = exercise_3_starter({1, 2, 3}, {3, 4, 5})
    assert u == {1, 2, 3, 4, 5}, "Union failed"
    assert i == {3}, "Intersection failed"
    
    # Test case 2: Disjoint sets
    u, i = exercise_3_starter({1, 2}, {3, 4})
    assert u == {1, 2, 3, 4}, "Union failed (disjoint)"
    assert i == set(), "Intersection failed (disjoint)"
    
    # Test case 3: One set is subset
    u, i = exercise_3_starter({1, 2, 3}, {1, 2})
    assert u == {1, 2, 3}, "Union failed (subset)"
    assert i == {1, 2}, "Intersection failed (subset)"


# ============================================================================
# Exercise 4: Difference and Symmetric Difference
# ============================================================================

def exercise_4_starter(set_a, set_b):
    """
    Calculate the difference (A - B) and symmetric difference of two sets.
    
    Objective: Master directional and mutual exclusion operations.
    
    Requirements:
    - Return a tuple: (difference_result, symmetric_diff_result)
    - Use symbolic operators (`-` and `^`).
    
    Args:
        set_a: First set.
        set_b: Second set.
    
    Returns:
        Tuple of (set_difference, set_symmetric_difference).
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return (set_a - set_b, set_a ^ set_b)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_4():
    """Test cases for Exercise 4"""
    
    # Test case 1: Mixed overlap
    d, sd = exercise_4_starter({1, 2, 3}, {3, 4, 5})
    assert d == {1, 2}, "Difference failed"
    assert sd == {1, 2, 4, 5}, "Symmetric difference failed"
    
    # Test case 2: Identical sets
    d, sd = exercise_4_starter({1, 2}, {1, 2})
    assert d == set(), "Difference failed (identical)"
    assert sd == set(), "Symmetric difference failed (identical)"
    
    # Test case 3: Empty second set
    d, sd = exercise_4_starter({1, 2}, set())
    assert d == {1, 2}, "Difference failed (empty)"
    assert sd == {1, 2}, "Symmetric difference failed (empty)"


# ============================================================================
# Exercise 5: Set Comprehensions
# ============================================================================

def exercise_5_starter(numbers):
    """
    Use a set comprehension to filter even numbers and square them.
    
    Objective: Master set comprehension syntax.
    
    Requirements:
    - Filter for even numbers only.
    - Square each number.
    - Must return a set (not a list).
    
    Args:
        numbers: List of integers.
    
    Returns:
        Set of squared even numbers.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return {n**2 for n in numbers if n % 2 == 0}
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_5():
    """Test cases for Exercise 5"""
    
    # Test case 1: Normal numerical list
    result = exercise_5_starter([1, 2, 3, 4, 5, 6])
    assert result == {4, 16, 36}, f"Failed. Expected {{4, 16, 36}}, got {result}"
    
    # Test case 2: All odd numbers
    result = exercise_5_starter([1, 3, 5])
    assert result == set(), "Failed for all odd numbers"
    
    # Test case 3: Negative numbers
    result = exercise_5_starter([-2, -4])
    assert result == {4, 16}, "Failed for negative evens"


# ============================================================================
# Exercise 6: Frozensets
# ============================================================================

def exercise_6_starter(items):
    """
    Create a frozenset and attempt to return it.
    
    Objective: Understand immutable sets.
    
    Requirements:
    - Convert `items` to a frozenset.
    - Return the resulting frozenset.
    
    Args:
        items: An iterable.
    
    Returns:
        A frozenset object.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return frozenset(items)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_6():
    """Test cases for Exercise 6"""
    
    # Test case 1: Basic conversion
    result = exercise_6_starter([1, 2, 3])
    assert isinstance(result, frozenset), "Result must be a frozenset"
    assert result == frozenset({1, 2, 3}), "Values mismatch"
    
    # Test case 2: Verify immutability (logical check)
    result = exercise_6_starter([1])
    try:
        result.add(2)
        assert False, "Should have raised AttributeError"
    except AttributeError:
        pass # Expected
    
    # Test case 3: Empty frozenset
    result = exercise_6_starter([])
    assert result == frozenset(), "Failed for empty input"


# ============================================================================
# Exercise 7: Membership and Subsets
# ============================================================================

def exercise_7_starter(set_a, set_b, item):
    """
    Check membership of an item in set_a, and check if set_b is a subset of set_a.
    
    Objective: Master boolean set checks.
    
    Requirements:
    - Return a tuple: (is_item_in_a, is_b_subset_of_a)
    
    Args:
        set_a: Main set.
        set_b: Potential subset.
        item: Item to check membership.
    
    Returns:
        Tuple of (bool, bool).
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    return (item in set_a, set_b <= set_a)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_7():
    """Test cases for Exercise 7"""
    
    # Test case 1: True for both
    in_a, is_sub = exercise_7_starter({1, 2, 3}, {1, 2}, 1)
    assert in_a is True and is_sub is True, "Failed basic case"
    
    # Test case 2: Item not in, but subset true
    in_a, is_sub = exercise_7_starter({1, 2}, {1}, 5)
    assert in_a is False and is_sub is True, "Failed item check"
    
    # Test case 3: Item in, but subset false
    in_a, is_sub = exercise_7_starter({1, 2}, {1, 2, 3}, 1)
    assert in_a is True and is_sub is False, "Failed subset check"


# ============================================================================
# Main Test Runner
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
