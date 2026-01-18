"""
Unit 3.3: Properties and Encapsulation - Exercises
Concept-focused drills testing property decorators, getters, setters, and encapsulation.
"""

# ============================================================================
# Exercise 1: Basic Property with Getter
# ============================================================================

def exercise_1_starter():
    """
    Create a class with a property that returns a private attribute.
    
    Objective: Master basic @property decorator for getters
    
    Requirements:
    - Create a class named 'Container'
    - Initialize with a private attribute '_value' set to 100
    - Create a property 'value' that returns '_value'
    - Return an instance of the class
    
    Returns:
        Instance of Container class with property 'value'
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Container:
        def __init__(self):
            self._value = 100
        @property
        def value(self):
            return self._value
    return Container()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_1():
    """Test cases for Exercise 1"""
    
    # Test case 1: Property returns correct value
    obj = exercise_1_starter()
    assert obj.value == 100, "Property should return 100"
    
    # Test case 2: Private attribute exists
    assert hasattr(obj, '_value'), "Private attribute _value should exist"
    
    # Test case 3: Property is read-only (no setter)
    try:
        obj.value = 200
        assert False, "Should not be able to set value without setter"
    except AttributeError:
        pass  # Expected


# ============================================================================
# Exercise 2: Property with Getter and Setter
# ============================================================================

def exercise_2_starter():
    """
    Create a class with a property that has both getter and setter.
    
    Objective: Master @property with setter decorator
    
    Requirements:
    - Create a class named 'Counter'
    - Initialize with private attribute '_count' set to 0
    - Create property 'count' with getter returning '_count'
    - Create setter for 'count' that updates '_count'
    - Return an instance of the class
    
    Returns:
        Instance of Counter class with readable and writable 'count' property
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Counter:
        def __init__(self):
            self._count = 0
        @property
        def count(self):
            return self._count
        @count.setter
        def count(self, value):
            self._count = value
    return Counter()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_2():
    """Test cases for Exercise 2"""
    
    # Test case 1: Initial value is 0
    obj = exercise_2_starter()
    assert obj.count == 0, "Initial count should be 0"
    
    # Test case 2: Setter works correctly
    obj.count = 5
    assert obj.count == 5, "Count should be 5 after setting"
    
    # Test case 3: Multiple sets work
    obj.count = 10
    obj.count = 15
    assert obj.count == 15, "Count should be 15 after multiple sets"


# ============================================================================
# Exercise 3: Property with Validation
# ============================================================================

def exercise_3_starter():
    """
    Create a class with a property that validates input in the setter.
    
    Objective: Master data validation in property setters
    
    Requirements:
    - Create a class named 'Score'
    - Initialize with private attribute '_points' set to 0
    - Create property 'points' with getter
    - Create setter that only accepts values between 0 and 100 (inclusive)
    - Raise ValueError if value is out of range
    - Return an instance of the class
    
    Returns:
        Instance of Score class with validated 'points' property
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Score:
        def __init__(self):
            self._points = 0
        @property
        def points(self):
            return self._points
        @points.setter
        def points(self, value):
            if not 0 <= value <= 100:
                raise ValueError
            self._points = value
    return Score()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_3():
    """Test cases for Exercise 3"""
    
    # Test case 1: Valid value accepted
    obj = exercise_3_starter()
    obj.points = 75
    assert obj.points == 75, "Valid value should be accepted"
    
    # Test case 2: Boundary values work
    obj.points = 0
    assert obj.points == 0, "Boundary value 0 should work"
    obj.points = 100
    assert obj.points == 100, "Boundary value 100 should work"
    
    # Test case 3: Invalid value raises error
    try:
        obj.points = 150
        assert False, "Should raise ValueError for value > 100"
    except ValueError:
        pass  # Expected


# ============================================================================
# Exercise 4: Read-Only Property (Computed Value)
# ============================================================================

def exercise_4_starter():
    """
    Create a class with a read-only property that computes a value.
    
    Objective: Master read-only properties for computed values
    
    Requirements:
    - Create a class named 'Rectangle'
    - Initialize with 'width' and 'height' (public attributes)
    - Create read-only property 'area' that returns width * height
    - Do NOT create a setter for 'area'
    - Return an instance with width=5, height=10
    
    Returns:
        Instance of Rectangle with computed 'area' property
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        @property
        def area(self):
            return self.width * self.height
    return Rectangle(5, 10)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_4():
    """Test cases for Exercise 4"""
    
    # Test case 1: Area computed correctly
    obj = exercise_4_starter()
    assert obj.area == 50, "Area should be 50 (5 * 10)"
    
    # Test case 2: Area updates when dimensions change
    obj.width = 8
    obj.height = 3
    assert obj.area == 24, "Area should update to 24 (8 * 3)"
    
    # Test case 3: Area is read-only
    try:
        obj.area = 100
        assert False, "Should not be able to set area directly"
    except AttributeError:
        pass  # Expected


# ============================================================================
# Exercise 5: Private Attributes with Name Mangling
# ============================================================================

def exercise_5_starter():
    """
    Create a class using private attributes with name mangling.
    
    Objective: Understand private attributes (double underscore prefix)
    
    Requirements:
    - Create a class named 'Vault'
    - Initialize with private attribute '__secret' set to "hidden"
    - Create property 'secret' that returns '__secret'
    - Do NOT create a setter (read-only)
    - Return an instance of the class
    
    Returns:
        Instance of Vault with private '__secret' attribute
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Vault:
        def __init__(self):
            self.__secret = "hidden"
        @property
        def secret(self):
            return self.__secret
    return Vault()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_5():
    """Test cases for Exercise 5"""
    
    # Test case 1: Property returns secret value
    obj = exercise_5_starter()
    assert obj.secret == "hidden", "Property should return 'hidden'"
    
    # Test case 2: Direct access to __secret fails
    try:
        _ = obj.__secret
        assert False, "Direct access to __secret should fail"
    except AttributeError:
        pass  # Expected
    
    # Test case 3: Name-mangled attribute exists
    assert hasattr(obj, '_Vault__secret'), "Name-mangled attribute should exist"


# ============================================================================
# Exercise 6: Multiple Properties with Different Access Levels
# ============================================================================

def exercise_6_starter():
    """
    Create a class with public, protected, and private attributes.
    
    Objective: Master different access level conventions
    
    Requirements:
    - Create a class named 'Account'
    - Public attribute: 'name' (no underscore)
    - Protected attribute: '_balance' with property getter/setter
    - Private attribute: '__pin' with property getter only
    - Initialize: name="User", _balance=1000, __pin="1234"
    - Return an instance of the class
    
    Returns:
        Instance of Account with mixed access levels
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Account:
        def __init__(self):
            self.name = "User"
            self._balance = 1000
            self.__pin = "1234"
        @property
        def balance(self):
            return self._balance
        @balance.setter
        def balance(self, value):
            self._balance = value
        @property
        def pin(self):
            return self.__pin
    return Account()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_6():
    """Test cases for Exercise 6"""
    
    # Test case 1: Public attribute accessible
    obj = exercise_6_starter()
    assert obj.name == "User", "Public name should be 'User'"
    obj.name = "Admin"
    assert obj.name == "Admin", "Public name should be modifiable"
    
    # Test case 2: Protected balance via property
    assert obj.balance == 1000, "Balance should be 1000"
    obj.balance = 1500
    assert obj.balance == 1500, "Balance should be modifiable via property"
    
    # Test case 3: Private pin is read-only
    assert obj.pin == "1234", "Pin should be '1234'"
    try:
        obj.pin = "5678"
        assert False, "Pin should be read-only"
    except AttributeError:
        pass  # Expected


# ============================================================================
# Exercise 7: Property with Type Validation
# ============================================================================

def exercise_7_starter():
    """
    Create a class with a property that validates data type.
    
    Objective: Master type checking in property setters
    
    Requirements:
    - Create a class named 'Config'
    - Initialize with private attribute '_timeout' set to 30
    - Create property 'timeout' with getter
    - Create setter that only accepts integers
    - Raise TypeError if non-integer is provided
    - Return an instance of the class
    
    Returns:
        Instance of Config with type-validated 'timeout' property
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Config:
        def __init__(self):
            self._timeout = 30
        @property
        def timeout(self):
            return self._timeout
        @timeout.setter
        def timeout(self, value):
            if not isinstance(value, int):
                raise TypeError
            self._timeout = value
    return Config()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_7():
    """Test cases for Exercise 7"""
    
    # Test case 1: Integer accepted
    obj = exercise_7_starter()
    obj.timeout = 60
    assert obj.timeout == 60, "Integer should be accepted"
    
    # Test case 2: Float rejected
    try:
        obj.timeout = 30.5
        assert False, "Float should be rejected"
    except TypeError:
        pass  # Expected
    
    # Test case 3: String rejected
    try:
        obj.timeout = "30"
        assert False, "String should be rejected"
    except TypeError:
        pass  # Expected


# ============================================================================
# Exercise 8: Property with Complex Validation
# ============================================================================

def exercise_8_starter():
    """
    Create a class with a property that has multiple validation rules.
    
    Objective: Master complex validation logic in setters
    
    Requirements:
    - Create a class named 'User'
    - Initialize with private attribute '_age' set to 18
    - Create property 'age' with getter
    - Create setter with validations:
      * Must be an integer (raise TypeError if not)
      * Must be between 0 and 150 inclusive (raise ValueError if not)
    - Return an instance of the class
    
    Returns:
        Instance of User with multi-validated 'age' property
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class User:
        def __init__(self):
            self._age = 18
        @property
        def age(self):
            return self._age
        @age.setter
        def age(self, value):
            if not isinstance(value, int):
                raise TypeError
            if not 0 <= value <= 150:
                raise ValueError
            self._age = value
    return User()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_8():
    """Test cases for Exercise 8"""
    
    # Test case 1: Valid age accepted
    obj = exercise_8_starter()
    obj.age = 25
    assert obj.age == 25, "Valid age should be accepted"
    
    # Test case 2: Type validation
    try:
        obj.age = "25"
        assert False, "String should raise TypeError"
    except TypeError:
        pass  # Expected
    
    # Test case 3: Range validation
    try:
        obj.age = 200
        assert False, "Age > 150 should raise ValueError"
    except ValueError:
        pass  # Expected


# ============================================================================
# Exercise 9: Property with Dependent Values
# ============================================================================

def exercise_9_starter():
    """
    Create a class where one property depends on another.
    
    Objective: Master properties that interact with each other
    
    Requirements:
    - Create a class named 'Temperature'
    - Initialize with private attribute '_celsius' set to 0
    - Create property 'celsius' with getter/setter
    - Create read-only property 'fahrenheit' that computes: (celsius * 9/5) + 32
    - Return an instance of the class
    
    Returns:
        Instance of Temperature with dependent properties
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Temperature:
        def __init__(self):
            self._celsius = 0
        @property
        def celsius(self):
            return self._celsius
        @celsius.setter
        def celsius(self, value):
            self._celsius = value
        @property
        def fahrenheit(self):
            return (self._celsius * 9/5) + 32
    return Temperature()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_9():
    """Test cases for Exercise 9"""
    
    # Test case 1: Fahrenheit computed from celsius
    obj = exercise_9_starter()
    assert obj.fahrenheit == 32, "0C should be 32F"
    
    # Test case 2: Fahrenheit updates when celsius changes
    obj.celsius = 100
    assert obj.fahrenheit == 212, "100C should be 212F"
    
    # Test case 3: Fahrenheit is read-only
    try:
        obj.fahrenheit = 100
        assert False, "Fahrenheit should be read-only"
    except AttributeError:
        pass  # Expected


# ============================================================================
# Exercise 10: Property Deleter
# ============================================================================

def exercise_10_starter():
    """
    Create a class with a property that includes a deleter.
    
    Objective: Master the @property.deleter decorator
    
    Requirements:
    - Create a class named 'Cache'
    - Initialize with private attribute '_data' set to "cached"
    - Create property 'data' with getter returning '_data'
    - Create setter for 'data'
    - Create deleter that sets '_data' to None
    - Return an instance of the class
    
    Returns:
        Instance of Cache with deletable 'data' property
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Cache:
        def __init__(self):
            self._data = "cached"
        @property
        def data(self):
            return self._data
        @data.setter
        def data(self, value):
            self._data = value
        @data.deleter
        def data(self):
            self._data = None
    return Cache()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_10():
    """Test cases for Exercise 10"""
    
    # Test case 1: Initial value correct
    obj = exercise_10_starter()
    assert obj.data == "cached", "Initial data should be 'cached'"
    
    # Test case 2: Setter works
    obj.data = "new data"
    assert obj.data == "new data", "Setter should update data"
    
    # Test case 3: Deleter sets to None
    del obj.data
    assert obj.data is None, "Deleter should set data to None"


# ============================================================================
# If running as script, run tests
# ============================================================================

if __name__ == "__main__":
    test_exercise_1()
    print("✓ Exercise 1 passed")
    
    test_exercise_2()
    print("✓ Exercise 2 passed")
    
    test_exercise_3()
    print("✓ Exercise 3 passed")
    
    test_exercise_4()
    print("✓ Exercise 4 passed")
    
    test_exercise_5()
    print("✓ Exercise 5 passed")
    
    test_exercise_6()
    print("✓ Exercise 6 passed")
    
    test_exercise_7()
    print("✓ Exercise 7 passed")
    
    test_exercise_8()
    print("✓ Exercise 8 passed")
    
    test_exercise_9()
    print("✓ Exercise 9 passed")
    
    test_exercise_10()
    print("✓ Exercise 10 passed")
    
    print("\n" + "="*50)
    print("All exercises passed! 🎉")
    print("="*50)
