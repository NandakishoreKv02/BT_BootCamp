"""
Unit 3.1: Classes and Objects - Exercises
Concept-focused drills testing implementation of OOP fundamentals.
"""

# ============================================================================
# Exercise 1: Basic Class Definition & Instantiation
# ============================================================================

def exercise_1_starter():
    """
    Define a class named 'SimpleClass' and create an instance of it.
    
    Objective: Master basic class definition and object creation.
    
    Requirements:
    - Define a class named 'SimpleClass' (it can have a 'pass' statement).
    - Create an instance of 'SimpleClass' and assign it to a variable named 'obj'.
    - Return 'obj'.
    
    Returns:
        An instance of SimpleClass.
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class SimpleClass:
        pass
    obj = SimpleClass()
    return obj
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_1():
    """Test cases for Exercise 1"""
    result = exercise_1_starter()
    
    # Test case 1: Check if result is an instance of SimpleClass
    assert result.__class__.__name__ == "SimpleClass", "Test 1 failed: Result must be an instance of SimpleClass"
    
    # Test case 2: Check if it's an object
    assert isinstance(result, object), "Test 2 failed: Result must be an object"
    
    # Test case 3: Check if identity is unique (different calls create different objects)
    result2 = exercise_1_starter()
    assert result is not result2, "Test 3 failed: Every call should return a new instance"


# ============================================================================
# Exercise 2: The __init__ Constructor
# ============================================================================

def exercise_2_starter(val_a, val_b):
    """
    Define a class 'DataContainer' that initializes with two values.
    
    Objective: Master attribute initialization using the constructor.
    
    Requirements:
    - Define a class 'DataContainer'.
    - Implement the '__init__' method to accept 'a' and 'b'.
    - Store them as instance variables 'self.a' and 'self.b'.
    - Return an instance created with 'val_a' and 'val_b'.
    
    Args:
        val_a: First value to store
        val_b: Second value to store
    
    Returns:
        A DataContainer object
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class DataContainer:
        def __init__(self, a, b):
            self.a = a
            self.b = b
    return DataContainer(val_a, val_b)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_2():
    """Test cases for Exercise 2"""
    
    # Test case 1: Basic integrity
    result = exercise_2_starter(10, 20)
    assert result.a == 10 and result.b == 20, "Test 1 failed: Attributes 'a' and 'b' not correctly initialized"
    
    # Test case 2: Different types
    result = exercise_2_starter("hello", [1, 2])
    assert result.a == "hello" and result.b == [1, 2], "Test 2 failed: Attributes should handle any data type"
    
    # Test case 3: Positive/Negative variance
    result = exercise_2_starter(-5, 0)
    assert result.a == -5 and result.b == 0, "Test 3 failed: Attributes not correctly stored"


# ============================================================================
# Exercise 3: Instance Variables and self
# ============================================================================

def exercise_3_starter(name_str):
    """
    Define a class 'Labeler' that stores a name and provides a method to get it.
    
    Objective: Implement instance variables using 'self'.
    
    Requirements:
    - Define a class 'Labeler'.
    - __init__ should accept 'text' and store it as 'self.text'.
    - Create a method 'get_text(self)' that returns 'self.text'.
    - Instantiate with 'name_str' and return the instance.
    
    Args:
        name_str: String value to store
    
    Returns:
        Labeler instance
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Labeler:
        def __init__(self, text):
            self.text = text
        def get_text(self):
            return self.text
    return Labeler(name_str)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_3():
    """Test cases for Exercise 3"""
    
    # Test case 1: Check attribute existence
    result = exercise_3_starter("Alpha")
    assert hasattr(result, "text"), "Test 1 failed: Instance must have 'text' attribute"
    
    # Test case 2: Check method functionality
    assert result.get_text() == "Alpha", "Test 2 failed: get_text() should return 'Alpha'"
    
    # Test case 3: Different instance
    result2 = exercise_3_starter("Beta")
    assert result2.get_text() == "Beta", "Test 3 failed: get_text() should return 'Beta'"


# ============================================================================
# Exercise 4: Class Variables vs Instance Variables
# ============================================================================

def exercise_4_starter():
    """
    Define a class 'Counter' with a shared class variable and a unique instance variable.
    
    Objective: Differentiate between shared and unique state.
    
    Requirements:
    - Define a class 'Counter'.
    - Add a class variable 'kind' set to "Generic".
    - __init__ should accept a value 'v' and store it as 'self.v'.
    - Create two instances: one with v=1, one with v=2.
    - Return a tuple of (instance1, instance2).
    
    Returns:
        Tuple of (Counter, Counter)
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Counter:
        kind = "Generic"
        def __init__(self, v):
            self.v = v
    return (Counter(1), Counter(2))
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_4():
    """Test cases for Exercise 4"""
    instances = exercise_4_starter()
    c1, c2 = instances
    
    # Test case 1: Class variable shared
    assert c1.kind == "Generic" and c2.kind == "Generic", "Test 1 failed: Both instances should see class variable 'kind'"
    
    # Test case 2: Instance variables unique
    assert c1.v == 1 and c2.v == 2, "Test 2 failed: Instances should have unique 'v' values"
    
    # Test case 3: Class variable is on the class
    assert "kind" in c1.__class__.__dict__, "Test 3 failed: 'kind' should be defined at the class level"


# ============================================================================
# Exercise 5: Creating Multiple Instances
# ============================================================================

def exercise_5_starter(num_instances):
    """
    Generate a list of unique objects.
    
    Objective: Practice creating multiple instances programmatically.
    
    Requirements:
    - Define a class 'Item' with __init__ that stores an 'item_id'.
    - Use a loop to create 'num_instances' instances, each with its index (0 to n-1) as item_id.
    - Return the list of objects.
    
    Args:
        num_instances: Integer count
        
    Returns:
        List of Item objects
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Item:
        def __init__(self, item_id):
            self.item_id = item_id
    return [Item(i) for i in range(num_instances)]
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_5():
    """Test cases for Exercise 5"""
    
    # Test case 1: List length
    result = exercise_5_starter(3)
    assert len(result) == 3, "Test 1 failed: Should return 3 instances"
    
    # Test case 2: Value sequence
    assert [obj.item_id for obj in result] == [0, 1, 2], "Test 2 failed: item_id sequence incorrect"
    
    # Test case 3: Empty request
    assert exercise_5_starter(0) == [], "Test 3 failed: Should return empty list for 0"


# ============================================================================
# Exercise 6: Object Identity and Equality
# ============================================================================

def exercise_6_starter():
    """
    Demonstrate identity vs equality.
    
    Objective: Master the 'is' and '==' operators for custom classes.
    
    Requirements:
    - Define a class 'Box' with __init__(self, size).
    - Create 'box1' with size=10.
    - Create 'box2' with size=10.
    - Assign 'box3' to 'box1'.
    - Return a tuple of (box1 is box2, box1 is box3, box1 == box2).
    
    Returns:
        Tuple: (bool, bool, bool)
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Box:
        def __init__(self, size):
            self.size = size
    box1 = Box(10)
    box2 = Box(10)
    box3 = box1
    return (box1 is box2, box1 is box3, box1 == box2)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_6():
    """Test cases for Exercise 6"""
    result = exercise_6_starter()
    
    # Test case 1: box1 is box2
    assert result[0] is False, "Test 1 failed: Separate instances are NOT identical ('is' should be False)"
    
    # Test case 2: box1 is box3
    assert result[1] is True, "Test 2 failed: References to same object ARE identical ('is' should be True)"
    
    # Test case 3: box1 == box2
    # By default, custom classes use identity for ==, so this should also be False
    assert result[2] is False, "Test 3 failed: By default, '==' checks identity for custom objects"


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
    print("All exercises passed!")
