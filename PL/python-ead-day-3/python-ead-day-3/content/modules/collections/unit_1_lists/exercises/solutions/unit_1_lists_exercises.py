"""
Unit 1: Lists - Exercises SOLUTIONS
Content: Complete working solutions
"""

# ============================================================================
# Exercise 1: List Creation and Indexing - SOLUTION
# ============================================================================

def exercise_1_starter(items):
    """Create list, return first and last."""
    items_list = list(items)
    if not items_list:
        return (None, None)
    return (items_list[0], items_list[-1])


def test_exercise_1():
    """Test cases for Exercise 1"""
    result = exercise_1_starter([1, 2, 3])
    assert result == (1, 3), "Test 1 failed"
    result = exercise_1_starter([42])
    assert result == (42, 42), "Test 2 failed"
    result = exercise_1_starter([])
    assert result == (None, None), "Test 3 failed"


# ============================================================================
# Exercise 2: List Slicing - SOLUTION
# ============================================================================

def exercise_2_starter(items, start, end):
    """Return slice."""
    return items[start:end]


def test_exercise_2():
    """Test cases for Exercise 2"""
    data = [10, 20, 30, 40, 50]
    result = exercise_2_starter(data, 1, 4)
    assert result == [20, 30, 40], "Test 1 failed"
    result = exercise_2_starter(data, 0, 2)
    assert result == [10, 20], "Test 2 failed"
    result = exercise_2_starter(data, 0, 100)
    assert result == [10, 20, 30, 40, 50], "Test 3 failed"


# ============================================================================
# Exercise 3: List Methods - SOLUTION
# ============================================================================

def exercise_3_starter(initial_list, to_add, to_remove):
    """Modify list (Append/Remove)."""
    initial_list.append(to_add)
    if to_remove in initial_list:
        initial_list.remove(to_remove)
    return initial_list


def test_exercise_3():
    """Test cases for Exercise 3"""
    result = exercise_3_starter([1, 2, 3], 4, 2)
    assert result == [1, 3, 4], "Test 1 failed"
    result = exercise_3_starter([1, 2, 3], 5, 99)
    assert result == [1, 2, 3, 5], "Test 2 failed"
    result = exercise_3_starter([1, 2, 2], 3, 2)
    assert result == [1, 2, 3], "Test 3 failed"


# ============================================================================
# Exercise 4: Filtering - SOLUTION
# ============================================================================

def exercise_4_starter(numbers, threshold):
    """Filter > threshold."""
    return [x for x in numbers if x > threshold]


def test_exercise_4():
    """Test cases for Exercise 4"""
    data = [1, 5, 10, 15]
    result = exercise_4_starter(data, 5)
    assert result == [10, 15], "Test 1 failed"
    result = exercise_4_starter(data, 20)
    assert result == [], "Test 2 failed"
    result = exercise_4_starter([1, 2], 0)
    assert result == [1, 2], "Test 3 failed"


# ============================================================================
# Exercise 5: Transformation - SOLUTION
# ============================================================================

def exercise_5_starter(numbers):
    """Square numbers."""
    return [x**2 for x in numbers]


def test_exercise_5():
    """Test cases for Exercise 5"""
    result = exercise_5_starter([1, 2, 3])
    assert result == [1, 4, 9], "Test 1 failed"
    result = exercise_5_starter([])
    assert result == [], "Test 2 failed"
    result = exercise_5_starter([-2])
    assert result == [4], "Test 3 failed"


# ============================================================================
# Exercise 6: Sorting - SOLUTION
# ============================================================================

def exercise_6_starter(numbers):
    """Sorted copy."""
    return sorted(numbers)


def test_exercise_6():
    """Test cases for Exercise 6"""
    original = [3, 1, 2]
    result = exercise_6_starter(original)
    assert result == [1, 2, 3], "Test 1 failed"
    assert original == [3, 1, 2], "Test 2 failed"
    result = exercise_6_starter([])
    assert result == [], "Test 3 failed"


# ============================================================================
# Exercise 7: Membership - SOLUTION
# ============================================================================

def exercise_7_starter(items, target):
    """Tuple (exists, count)."""
    exists = target in items
    count = items.count(target)
    return (exists, count)


def test_exercise_7():
    """Test cases for Exercise 7"""
    data = ["a", "b", "a", "c"]
    result = exercise_7_starter(data, "a")
    assert result == (True, 2), "Test 1 failed"
    result = exercise_7_starter(data, "z")
    assert result == (False, 0), "Test 2 failed"
    result = exercise_7_starter([], "x")
    assert result == (False, 0), "Test 3 failed"


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
