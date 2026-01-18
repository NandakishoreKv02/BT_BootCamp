"""
Unit 1: Lists - Exercises
Concept-focused drills testing list fundamentals.
"""

# ============================================================================
# Exercise 1: List Creation and Indexing
# ============================================================================

def exercise_1_starter(items):
    """
    Create a list from items and return the first and last elements.
    
    Objective: Master list creation and index access
    
    Requirements:
    - Accept any iterable (convert to list if needed)
    - Return a tuple of (first_item, last_item)
    - Handle empty list by returning (None, None)
    
    Args:
        items: An iterable (list, tuple, string, etc.)
    
    Returns:
        Tuple of (first_element, last_element) or (None, None)
    """
    # WRITE CODE HERE
    lst = list(items)
    return (lst[0], lst[-1]) if lst else (None, None)
    # END OF YOUR CODE


def test_exercise_1():
    """Test cases for Exercise 1"""
    result = exercise_1_starter([1, 2, 3])
    assert result == (1, 3), "Test 1 failed: Expected (1, 3)"
    
    result = exercise_1_starter([42])
    assert result == (42, 42), "Test 2 failed: Expected (42, 42)"
    
    result = exercise_1_starter([])
    assert result == (None, None), "Test 3 failed: Expected (None, None)"


# ============================================================================
# Exercise 2: List Slicing
# ============================================================================

def exercise_2_starter(items, start, end):
    """
    Return a slice of items from start index to end index (exclusive).
    
    Objective: Master list slicing syntax
    
    Requirements:
    - Return a new list using slicing [start:end]
    - If indices are out of bounds, Python slicing handles it gracefully (return what you can)
    
    Args:
        items: List to slice
        start: Start index
        end: End index
    
    Returns:
        Sliced list
    """
    # WRITE CODE HERE
    return items[start:end]
    # END OF YOUR CODE


def test_exercise_2():
    """Test cases for Exercise 2"""
    data = [10, 20, 30, 40, 50]
    result = exercise_2_starter(data, 1, 4)
    assert result == [20, 30, 40], "Test 1 failed: Slice [1:4]"
    
    result = exercise_2_starter(data, 0, 2)
    assert result == [10, 20], "Test 2 failed: Slice [0:2]"
    
    result = exercise_2_starter(data, 0, 100)
    assert result == [10, 20, 30, 40, 50], "Test 3 failed: Full slice"


# ============================================================================
# Exercise 3: List Methods (Append and Remove)
# ============================================================================

def exercise_3_starter(initial_list, to_add, to_remove):
    """
    Modify a list by adding and removing items.
    
    Objective: Master list mutating methods
    
    Requirements:
    - Append `to_add` to the end
    - Remove the first occurrence of `to_remove` (if it exists)
    - Return the modified list
    
    Args:
        initial_list: Starting list
        to_add: Item to append
        to_remove: Item to remove
    
    Returns:
        Modified list
    """
    # WRITE CODE HERE
    initial_list.append(to_add)
    if to_remove in initial_list:
        initial_list.remove(to_remove)
    return initial_list
    # END OF YOUR CODE


def test_exercise_3():
    """Test cases for Exercise 3"""
    result = exercise_3_starter([1, 2, 3], 4, 2)
    assert result == [1, 3, 4], "Test 1 failed: Add 4 remove 2"
    
    result = exercise_3_starter([1, 2, 3], 5, 99)
    assert result == [1, 2, 3, 5], "Test 2 failed: Remove non-existent"
    
    result = exercise_3_starter([1, 2, 2], 3, 2)
    assert result == [1, 2, 3], "Test 3 failed: Remove first occurrence only"


# ============================================================================
# Exercise 4: List Comprehension - Filtering
# ============================================================================

def exercise_4_starter(numbers, threshold):
    """
    Filter numbers strictly greater than threshold.
    
    Objective: Master list comprehension filtering
    
    Requirements:
    - Use list comprehension
    - Return list of numbers > threshold
    
    Args:
        numbers: List of int
        threshold: int to compare against
    
    Returns:
        Filtered list
    """
    # WRITE CODE HERE
    return [x for x in numbers if x > threshold]
    # END OF YOUR CODE


def test_exercise_4():
    """Test cases for Exercise 4"""
    data = [1, 5, 10, 15]
    result = exercise_4_starter(data, 5)
    assert result == [10, 15], "Test 1 failed: > 5"
    
    result = exercise_4_starter(data, 20)
    assert result == [], "Test 2 failed: Empty result"
    
    result = exercise_4_starter([1, 2], 0)
    assert result == [1, 2], "Test 3 failed: All pass"


# ============================================================================
# Exercise 5: List Comprehension - Transformation
# ============================================================================

def exercise_5_starter(numbers):
    """
    Square each number in the list.
    
    Objective: Master list comprehension transformation
    
    Requirements:
    - Return new list where each item x is x*x
    
    Args:
        numbers: List of int
    
    Returns:
        Transformed list
    """
    # WRITE CODE HERE
    return [x * x for x in numbers]
    # END OF YOUR CODE


def test_exercise_5():
    """Test cases for Exercise 5"""
    result = exercise_5_starter([1, 2, 3])
    assert result == [1, 4, 9], "Test 1 failed: Squares"
    
    result = exercise_5_starter([])
    assert result == [], "Test 2 failed: Empty"
    
    result = exercise_5_starter([-2])
    assert result == [4], "Test 3 failed: Negative square"


# ============================================================================
# Exercise 6: Sorting Lists
# ============================================================================

def exercise_6_starter(numbers):
    """
    Return a sorted version of the list without modifying original.
    
    Objective: Master sorted() vs .sort()
    
    Requirements:
    - Use `sorted()` function (or copy then sort)
    - Do NOT modify the input list
    - Return the sorted list
    
    Args:
        numbers: List of numbers
    
    Returns:
        Sorted list
    """
    # WRITE CODE HERE
    return sorted(numbers)
    # END OF YOUR CODE


def test_exercise_6():
    """Test cases for Exercise 6"""
    original = [3, 1, 2]
    result = exercise_6_starter(original)
    assert result == [1, 2, 3], "Test 1 failed: Sorted"
    assert original == [3, 1, 2], "Test 2 failed: Original modified"
    
    result = exercise_6_starter([])
    assert result == [], "Test 3 failed: Empty"


# ============================================================================
# Exercise 7: Membership Checking
# ============================================================================

def exercise_7_starter(items, target):
    """
    Check if target is in items and count occurrences.
    
    Objective: Master 'in' operator and .count()
    
    Requirements:
    - Return a tuple: (is_present_bool, count_int)
    
    Args:
        items: List to search
        target: Item to find
    
    Returns:
        (bool, int)
    """
    # WRITE CODE HERE
    return (target in items, items.count(target))
    # END OF YOUR CODE


def test_exercise_7():
    """Test cases for Exercise 7"""
    data = ["a", "b", "a", "c"]
    
    result = exercise_7_starter(data, "a")
    assert result == (True, 2), "Test 1 failed: a"
    
    result = exercise_7_starter(data, "z")
    assert result == (False, 0), "Test 2 failed: z"
    
    result = exercise_7_starter([], "x")
    assert result == (False, 0), "Test 3 failed: empty"


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
