"""
Unit 3.4: Special Methods (Dunder Methods) - Exercises
Concept-focused drills for Python special methods.
"""

# ============================================================================
# Exercise 1: Basic __str__ Method
# ============================================================================

def exercise_1_starter():
    """
    Create a class with a __str__ method.
    
    Objective: Implement user-friendly string representation
    
    Requirements:
    - Create class 'Item' with __init__(self, name, value)
    - Implement __str__ returning "Name: {name}, Value: {value}"
    - Return an instance with name="Widget", value=42
    
    Returns:
        Instance of Item class
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Item:
        def __init__(self, name, value):
            self.name = name
            self.value = value
        def __str__(self):
            return f"Name: {self.name}, Value: {self.value}"
    return Item("Widget", 42)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_1():
    """Test cases for Exercise 1"""
    obj = exercise_1_starter()
    
    # Test case 1: str() returns correct format
    assert str(obj) == "Name: Widget, Value: 42", "str() format incorrect"
    
    # Test case 2: print() uses __str__
    assert "Widget" in str(obj), "Name not in string"
    
    # Test case 3: Attributes exist
    assert obj.name == "Widget", "name attribute missing"
    assert obj.value == 42, "value attribute missing"


# ============================================================================
# Exercise 2: Basic __repr__ Method
# ============================================================================

def exercise_2_starter():
    """
    Create a class with a __repr__ method.
    
    Objective: Implement developer-friendly representation
    
    Requirements:
    - Create class 'Record' with __init__(self, id, status)
    - Implement __repr__ returning "Record(id='...', status='...')"
    - Return an instance with id="R001", status="active"
    
    Returns:
        Instance of Record class
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Record:
        def __init__(self, id, status):
            self.id = id
            self.status = status
        def __repr__(self):
            return f"Record(id='{self.id}', status='{self.status}')"
    return Record("R001", "active")
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_2():
    """Test cases for Exercise 2"""
    obj = exercise_2_starter()
    
    # Test case 1: repr() returns correct format
    assert repr(obj) == "Record(id='R001', status='active')", "repr() format incorrect"
    
    # Test case 2: Contains class name
    assert "Record" in repr(obj), "Class name not in repr"
    
    # Test case 3: Contains attribute values
    assert "R001" in repr(obj) and "active" in repr(obj), "Values not in repr"


# ============================================================================
# Exercise 3: __str__ and __repr__ Together
# ============================================================================

def exercise_3_starter():
    """
    Create a class with both __str__ and __repr__.
    
    Objective: Implement distinct user and developer representations
    
    Requirements:
    - Create class 'Product' with __init__(self, sku, name, price)
    - __str__: "Product: {name} (${price})"
    - __repr__: "Product('{sku}', '{name}', {price})"
    - Return instance: sku="SKU001", name="Laptop", price=999.99
    
    Returns:
        Instance of Product class
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Product:
        def __init__(self, sku, name, price):
            self.sku = sku
            self.name = name
            self.price = price
        def __str__(self):
            return f"Product: {self.name} (${self.price})"
        def __repr__(self):
            return f"Product('{self.sku}', '{self.name}', {self.price})"
    return Product("SKU001", "Laptop", 999.99)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_3():
    """Test cases for Exercise 3"""
    obj = exercise_3_starter()
    
    # Test case 1: str() is user-friendly
    assert str(obj) == "Product: Laptop ($999.99)", "str() format incorrect"
    
    # Test case 2: repr() is developer-friendly
    assert repr(obj) == "Product('SKU001', 'Laptop', 999.99)", "repr() format incorrect"
    
    # Test case 3: Both methods defined
    assert str(obj) != repr(obj), "str and repr should be different"


# ============================================================================
# Exercise 4: __len__ Method
# ============================================================================

def exercise_4_starter():
    """
    Create a class that supports len().
    
    Objective: Make object work with len() function
    
    Requirements:
    - Create class 'Playlist' with empty _songs list
    - Implement add(song) to append songs
    - Implement __len__ returning count of songs
    - Add 3 songs and return the instance
    
    Returns:
        Playlist instance with 3 songs
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Playlist:
        def __init__(self):
            self._songs = []
        def add(self, song):
            self._songs.append(song)
        def __len__(self):
            return len(self._songs)
    p = Playlist()
    p.add("Song1")
    p.add("Song2")
    p.add("Song3")
    return p
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_4():
    """Test cases for Exercise 4"""
    obj = exercise_4_starter()
    
    # Test case 1: len() returns correct count
    assert len(obj) == 3, "len() should return 3"
    
    # Test case 2: Empty playlist
    class Playlist:
        def __init__(self):
            self._songs = []
        def add(self, song):
            self._songs.append(song)
        def __len__(self):
            return len(self._songs)
    
    empty = Playlist()
    assert len(empty) == 0, "Empty playlist should have len 0"
    
    # Test case 3: After adding
    empty.add("Song")
    assert len(empty) == 1, "After add, len should be 1"


# ============================================================================
# Exercise 5: __getitem__ Method
# ============================================================================

def exercise_5_starter():
    """
    Create a class that supports indexing with [].
    
    Objective: Enable obj[index] syntax
    
    Requirements:
    - Create class 'TaskList' with _tasks list
    - Initialize with ["Task A", "Task B", "Task C"]
    - Implement __getitem__(self, index)
    - Return the instance
    
    Returns:
        TaskList instance with 3 tasks
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class TaskList:
        def __init__(self):
            self._tasks = ["Task A", "Task B", "Task C"]
        def __getitem__(self, index):
            return self._tasks[index]
    return TaskList()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_5():
    """Test cases for Exercise 5"""
    obj = exercise_5_starter()
    
    # Test case 1: Positive index
    assert obj[0] == "Task A", "obj[0] should be 'Task A'"
    
    # Test case 2: Another index
    assert obj[1] == "Task B", "obj[1] should be 'Task B'"
    
    # Test case 3: Negative index
    assert obj[-1] == "Task C", "obj[-1] should be 'Task C'"


# ============================================================================
# Exercise 6: __setitem__ Method
# ============================================================================

def exercise_6_starter():
    """
    Create a class that supports index assignment.
    
    Objective: Enable obj[index] = value syntax
    
    Requirements:
    - Create class 'Grid' with _cells list of 9 None values
    - Implement __getitem__(self, index)
    - Implement __setitem__(self, index, value)
    - Return the instance
    
    Returns:
        Grid instance
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Grid:
        def __init__(self):
            self._cells = [None] * 9
        def __getitem__(self, index):
            return self._cells[index]
        def __setitem__(self, index, value):
            self._cells[index] = value
    return Grid()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_6():
    """Test cases for Exercise 6"""
    obj = exercise_6_starter()
    
    # Test case 1: Initial value is None
    assert obj[0] is None, "Initial cells should be None"
    
    # Test case 2: Setting a value
    obj[0] = "X"
    assert obj[0] == "X", "After setting, obj[0] should be 'X'"
    
    # Test case 3: Setting another value
    obj[4] = "O"
    assert obj[4] == "O", "obj[4] should be 'O'"


# ============================================================================
# Exercise 7: __contains__ Method
# ============================================================================

def exercise_7_starter():
    """
    Create a class that supports the 'in' operator.
    
    Objective: Enable 'item in container' syntax
    
    Requirements:
    - Create class 'Basket' with empty _items list
    - Implement add(item) method
    - Implement __contains__(self, item)
    - Add "apple" and "banana", return instance
    
    Returns:
        Basket instance with 2 items
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Basket:
        def __init__(self):
            self._items = []
        def add(self, item):
            self._items.append(item)
        def __contains__(self, item):
            return item in self._items
    b = Basket()
    b.add("apple")
    b.add("banana")
    return b
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_7():
    """Test cases for Exercise 7"""
    obj = exercise_7_starter()
    
    # Test case 1: Item exists
    assert "apple" in obj, "'apple' should be in basket"
    
    # Test case 2: Another item exists
    assert "banana" in obj, "'banana' should be in basket"
    
    # Test case 3: Item doesn't exist
    assert "orange" not in obj, "'orange' should not be in basket"


# ============================================================================
# Exercise 8: __eq__ Method
# ============================================================================

def exercise_8_starter():
    """
    Create a class with custom equality.
    
    Objective: Define equality based on attribute, not memory
    
    Requirements:
    - Create class 'Entity' with entity_id attribute
    - Implement __eq__ comparing entity_id values
    - Return NotImplemented for non-Entity comparisons
    - Return two instances: id="E001" and id="E001"
    
    Returns:
        Tuple of (entity1, entity2) both with id="E001"
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Entity:
        def __init__(self, entity_id):
            self.entity_id = entity_id
        def __eq__(self, other):
            if not isinstance(other, Entity):
                return NotImplemented
            return self.entity_id == other.entity_id
    return (Entity("E001"), Entity("E001"))
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_8():
    """Test cases for Exercise 8"""
    e1, e2 = exercise_8_starter()
    
    # Test case 1: Same ID means equal
    assert e1 == e2, "Entities with same ID should be equal"
    
    # Test case 2: Different instances
    assert e1 is not e2, "Should be different instances"
    
    # Test case 3: Comparison with non-Entity
    assert (e1 == "E001") == NotImplemented or not (e1 == "E001"), \
        "Comparison with string should return NotImplemented or False"


# ============================================================================
# Exercise 9: __lt__ for Sorting
# ============================================================================

def exercise_9_starter():
    """
    Create a class that can be sorted.
    
    Objective: Enable sorting with sorted()
    
    Requirements:
    - Create class 'Priority' with level (int) and name (str)
    - Implement __lt__ comparing by level (lower = higher priority)
    - Return list of 3 Priority objects: levels 3, 1, 2
    
    Returns:
        List of Priority instances
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Priority:
        def __init__(self, level, name):
            self.level = level
            self.name = name
        def __lt__(self, other):
            return self.level < other.level
    return [Priority(3, "Low"), Priority(1, "High"), Priority(2, "Med")]
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_9():
    """Test cases for Exercise 9"""
    priorities = exercise_9_starter()
    
    # Test case 1: Can be sorted
    sorted_p = sorted(priorities)
    assert sorted_p[0].level == 1, "First after sort should have level 1"
    
    # Test case 2: Order is correct
    assert sorted_p[1].level == 2, "Second should have level 2"
    assert sorted_p[2].level == 3, "Third should have level 3"
    
    # Test case 3: Comparison works
    assert priorities[1] < priorities[0], "Level 1 < Level 3"


# ============================================================================
# Exercise 10: __eq__ and __hash__ Together
# ============================================================================

def exercise_10_starter():
    """
    Create a hashable class with custom equality.
    
    Objective: Make objects usable in sets and as dict keys
    
    Requirements:
    - Create class 'Tag' with tag_id and label
    - Implement __eq__ based on tag_id
    - Implement __hash__ based on tag_id
    - Return two instances with same tag_id but different labels
    
    Returns:
        Tuple of (tag1, tag2) with same tag_id
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Tag:
        def __init__(self, tag_id, label):
            self.tag_id = tag_id
            self.label = label
        def __eq__(self, other):
            if not isinstance(other, Tag):
                return NotImplemented
            return self.tag_id == other.tag_id
        def __hash__(self):
            return hash(self.tag_id)
    return (Tag("T1", "Label1"), Tag("T1", "Label2"))
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_10():
    """Test cases for Exercise 10"""
    t1, t2 = exercise_10_starter()
    
    # Test case 1: Equal by ID
    assert t1 == t2, "Tags with same ID should be equal"
    
    # Test case 2: Same hash
    assert hash(t1) == hash(t2), "Equal objects must have equal hashes"
    
    # Test case 3: Can be used in set
    tag_set = {t1, t2}
    assert len(tag_set) == 1, "Set should have only 1 element (duplicates removed)"


# ============================================================================
# Exercise 11: __call__ Method
# ============================================================================

def exercise_11_starter():
    """
    Create a callable object.
    
    Objective: Make instance callable like a function
    
    Requirements:
    - Create class 'Multiplier' with factor attribute
    - Implement __call__(self, value) returning value * factor
    - Return instance with factor=3
    
    Returns:
        Multiplier instance with factor 3
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Multiplier:
        def __init__(self, factor):
            self.factor = factor
        def __call__(self, value):
            return value * self.factor
    return Multiplier(3)
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_11():
    """Test cases for Exercise 11"""
    mult = exercise_11_starter()
    
    # Test case 1: Can be called
    assert mult(10) == 30, "mult(10) should return 30"
    
    # Test case 2: Different value
    assert mult(5) == 15, "mult(5) should return 15"
    
    # Test case 3: Has factor attribute
    assert mult.factor == 3, "factor should be 3"


# ============================================================================
# Exercise 12: Complete Protocol Implementation
# ============================================================================

def exercise_12_starter():
    """
    Create a fully-featured collection class.
    
    Objective: Combine multiple special methods
    
    Requirements:
    - Create class 'Inventory' with _items dict {name: quantity}
    - __len__: Number of unique items
    - __getitem__(name): Get quantity by name
    - __setitem__(name, qty): Set quantity
    - __contains__(name): Check if item exists
    - __iter__: Iterate over item names
    - __repr__: "Inventory({item_count} items)"
    - Initialize with {"apple": 10, "banana": 5}
    
    Returns:
        Inventory instance
    """
    # ========================================================================
    # WRITE CODE HERE
    # ========================================================================
    class Inventory:
        def __init__(self):
            self._items = {"apple": 10, "banana": 5}
        def __len__(self):
            return len(self._items)
        def __getitem__(self, name):
            return self._items[name]
        def __setitem__(self, name, qty):
            self._items[name] = qty
        def __contains__(self, name):
            return name in self._items
        def __iter__(self):
            return iter(self._items)
        def __repr__(self):
            return f"Inventory({len(self._items)} items)"
    return Inventory()
    # ========================================================================
    # END OF YOUR CODE
    # ========================================================================


def test_exercise_12():
    """Test cases for Exercise 12"""
    inv = exercise_12_starter()
    
    # Test case 1: len() works
    assert len(inv) == 2, "Should have 2 items"
    
    # Test case 2: getitem works
    assert inv["apple"] == 10, "apple quantity should be 10"
    
    # Test case 3: setitem works
    inv["orange"] = 7
    assert inv["orange"] == 7, "orange quantity should be 7"
    
    # Test case 4: contains works
    assert "apple" in inv, "apple should be in inventory"
    assert "grape" not in inv, "grape should not be in inventory"
    
    # Test case 5: iter works
    items = list(inv)
    assert "apple" in items and "banana" in items, "Should iterate over items"
    
    # Test case 6: repr works
    assert "Inventory" in repr(inv), "repr should contain 'Inventory'"


# ============================================================================
# Run all tests
# ============================================================================

if __name__ == "__main__":
    tests = [
        ("Exercise 1", test_exercise_1),
        ("Exercise 2", test_exercise_2),
        ("Exercise 3", test_exercise_3),
        ("Exercise 4", test_exercise_4),
        ("Exercise 5", test_exercise_5),
        ("Exercise 6", test_exercise_6),
        ("Exercise 7", test_exercise_7),
        ("Exercise 8", test_exercise_8),
        ("Exercise 9", test_exercise_9),
        ("Exercise 10", test_exercise_10),
        ("Exercise 11", test_exercise_11),
        ("Exercise 12", test_exercise_12),
    ]
    
    for name, test_func in tests:
        try:
            test_func()
            print(f"✓ {name} passed")
        except AssertionError as e:
            print(f"✗ {name} failed: {e}")
        except Exception as e:
            print(f"✗ {name} error: {e}")
    
    print("\n" + "="*50)
    print("Exercise testing complete!")
    print("="*50)
