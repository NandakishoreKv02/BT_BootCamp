"""
Unit 5: Collection Selection Guide - SOLUTIONS
"""

# ============================================================================
# Exercise 1: Search Optimization
# ============================================================================

def exercise_1_starter(large_list, search_items):
    search_set = set(large_list)
    return sum(1 for item in search_items if item in search_set)

def test_exercise_1():
    data = [1, 2, 3, 4, 5]
    targets = [2, 5, 99]
    result = exercise_1_starter(data, targets)
    assert result == 2
    result = exercise_1_starter([], [1, 2])
    assert result == 0

# ============================================================================
# Exercise 2: Memory Optimization
# ============================================================================

def exercise_2_starter(items_list):
    return tuple(items_list)

def test_exercise_2():
    data = [1, 2, 3]
    result = exercise_2_starter(data)
    assert isinstance(result, tuple)
    assert result == (1, 2, 3)

# ============================================================================
# Exercise 3: Deduplication with Sorting
# ============================================================================

def exercise_3_starter(data_with_duplicates):
    unique = set(data_with_duplicates)
    result = list(unique)
    result.sort()
    return result

def test_exercise_3():
    data = [3, 1, 2, 3, 1]
    result = exercise_3_starter(data)
    assert result == [1, 2, 3]

# ============================================================================
# Exercise 4: Parallel Data Mapping
# ============================================================================

def exercise_4_starter(keys, values):
    return dict(zip(keys, values))

def test_exercise_4():
    k = ["a", "b", "c"]
    v = [1, 2, 3]
    result = exercise_4_starter(k, v)
    assert result == {"a": 1, "b": 2, "c": 3}

# ============================================================================
# Exercise 5: Grouping Unique Values
# ============================================================================

def exercise_5_starter(words):
    return {len(word) for word in words}

def test_exercise_5():
    words = ["cat", "dog", "apple", "cat"]
    result = exercise_5_starter(words)
    assert result == {3, 5}

# ============================================================================
# Exercise 6: Verifying Hashability
# ============================================================================

def exercise_6_starter(item):
    try:
        temp_set = {item}
        return True
    except TypeError:
        return False

def test_exercise_6():
    assert exercise_6_starter("hello") is True
    assert exercise_6_starter([1, 2]) is False
    assert exercise_6_starter((1, 2)) is True

# ============================================================================
# Exercise 7: The Selection Helper
# ============================================================================

def exercise_7_starter(needs_order, needs_uniqueness, needs_key_lookup):
    if needs_key_lookup:
        return "dict"
    if needs_uniqueness:
        return "set"
    return "list"

def test_exercise_7():
    assert exercise_7_starter(False, False, True) == "dict"
    assert exercise_7_starter(True, True, False) == "set"
    assert exercise_7_starter(True, False, False) == "list"

if __name__ == "__main__":
    test_exercise_1()
    test_exercise_2()
    test_exercise_3()
    test_exercise_4()
    test_exercise_5()
    test_exercise_6()
    test_exercise_7()
    print("All Unit 5 exercises passed!")
