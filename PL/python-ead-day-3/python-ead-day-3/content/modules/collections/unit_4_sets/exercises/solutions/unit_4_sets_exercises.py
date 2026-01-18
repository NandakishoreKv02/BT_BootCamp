"""
Unit 4: Sets - Exercises SOLUTIONS
Content: Complete working implementations for set exercises.
"""

# ============================================================================
# Exercise 1: Set Creation and Deduplication - SOLUTION
# ============================================================================

def exercise_1_starter(items):
    """Convert to set and return count."""
    unique_items = set(items)
    return len(unique_items)


def test_exercise_1():
    """Test cases for Exercise 1"""
    result = exercise_1_starter([1, 2, 2, 3, 3, 3])
    assert result == 3
    result = exercise_1_starter([])
    assert result == 0
    result = exercise_1_starter("abracadabra")
    assert result == 5


# ============================================================================
# Exercise 2: Basic Set Operations - SOLUTION
# ============================================================================

def exercise_2_starter(initial_set, to_add, to_remove):
    """Add and discard."""
    initial_set.add(to_add)
    initial_set.discard(to_remove)
    return initial_set


def test_exercise_2():
    """Test cases for Exercise 2"""
    result = exercise_2_starter({1, 2, 3}, 4, 2)
    assert result == {1, 3, 4}
    result = exercise_2_starter({1, 2}, 3, 99)
    assert result == {1, 2, 3}
    result = exercise_2_starter({1, 2}, 2, 1)
    assert result == {2}


# ============================================================================
# Exercise 3: Union and Intersection - SOLUTION
# ============================================================================

def exercise_3_starter(set_a, set_b):
    """Union and Intersection."""
    u = set_a | set_b
    i = set_a & set_b
    return (u, i)


def test_exercise_3():
    """Test cases for Exercise 3"""
    u, i = exercise_3_starter({1, 2, 3}, {3, 4, 5})
    assert u == {1, 2, 3, 4, 5}
    assert i == {3}
    u, i = exercise_3_starter({1, 2}, {3, 4})
    assert u == {1, 2, 3, 4}
    assert i == set()
    u, i = exercise_3_starter({1, 2, 3}, {1, 2})
    assert u == {1, 2, 3}
    assert i == {1, 2}


# ============================================================================
# Exercise 4: Difference and Symmetric Difference - SOLUTION
# ============================================================================

def exercise_4_starter(set_a, set_b):
    """Difference and Symmetric Difference."""
    d = set_a - set_b
    sd = set_a ^ set_b
    return (d, sd)


def test_exercise_4():
    """Test cases for Exercise 4"""
    d, sd = exercise_4_starter({1, 2, 3}, {3, 4, 5})
    assert d == {1, 2}
    assert sd == {1, 2, 4, 5}
    d, sd = exercise_4_starter({1, 2}, {1, 2})
    assert d == set()
    assert sd == set()
    d, sd = exercise_4_starter({1, 2}, set())
    assert d == {1, 2}
    assert sd == {1, 2}


# ============================================================================
# Exercise 5: Set Comprehensions - SOLUTION
# ============================================================================

def exercise_5_starter(numbers):
    """Filter and square."""
    return {x**2 for x in numbers if x % 2 == 0}


def test_exercise_5():
    """Test cases for Exercise 5"""
    result = exercise_5_starter([1, 2, 3, 4, 5, 6])
    assert result == {4, 16, 36}
    result = exercise_5_starter([1, 3, 5])
    assert result == set()
    result = exercise_5_starter([-2, -4])
    assert result == {4, 16}


# ============================================================================
# Exercise 6: Frozensets - SOLUTION
# ============================================================================

def exercise_6_starter(items):
    """Convert to frozenset."""
    return frozenset(items)


def test_exercise_6():
    """Test cases for Exercise 6"""
    result = exercise_6_starter([1, 2, 3])
    assert isinstance(result, frozenset)
    assert result == frozenset({1, 2, 3})
    result = exercise_6_starter([])
    assert result == frozenset()


# ============================================================================
# Exercise 7: Membership and Subsets - SOLUTION
# ============================================================================

def exercise_7_starter(set_a, set_b, item):
    """Membership and Subsets."""
    in_a = item in set_a
    is_sub = set_b.issubset(set_a) # or set_b <= set_a
    return (in_a, is_sub)


def test_exercise_7():
    """Test cases for Exercise 7"""
    in_a, is_sub = exercise_7_starter({1, 2, 3}, {1, 2}, 1)
    assert in_a is True and is_sub is True
    in_a, is_sub = exercise_7_starter({1, 2}, {1}, 5)
    assert in_a is False and is_sub is True
    in_a, is_sub = exercise_7_starter({1, 2}, {1, 2, 3}, 1)
    assert in_a is True and is_sub is False


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
