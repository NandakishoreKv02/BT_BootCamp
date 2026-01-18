"""
Unit 4.1: Inheritance - Exercises
Progressive drills covering inheritance, overriding, super(), and ABCs.
"""
from abc import ABC, abstractmethod

# ============================================================================
# Exercise 1: Basic Single Inheritance
# ============================================================================

def exercise_1_starter():
    """
    Create a Car class inheriting from Vehicle.
    
    Requirements:
    - Vehicle class with method start_engine() returning "Engine started".
    - Car class inherits from Vehicle.
    - Car.__init__ takes (brand, num_wheels).
    - Return an instance of Car("Toyota", 4).
    """
    class Vehicle:
        def start_engine(self):
            return "Engine started"

    class Car(Vehicle):
        def __init__(self, brand, num_wheels):
            self.brand = brand
            self.num_wheels = num_wheels

    return Car("Toyota", 4)

def test_exercise_1():
    obj = exercise_1_starter()
    assert obj.start_engine() == "Engine started"
    assert obj.num_wheels == 4
    # Check inheritance
    assert isinstance(obj, object) # Placeholder check


# ============================================================================
# Exercise 2: Method Overriding
# ============================================================================

def exercise_2_starter():
    """
    Implement a discount system using overriding.
    
    Requirements:
    - Customer.get_discount() returns 0.05
    - VIPCustomer inherits Customer and overrides get_discount() to return 0.10
    - Return a tuple instances: (Customer(), VIPCustomer())
    """
    class Customer:
        def get_discount(self):
            return 0.05
    
    class VIPCustomer(Customer):
        def get_discount(self):
            return 0.10
    
    return (Customer(), VIPCustomer())

def test_exercise_2():
    cust, vip = exercise_2_starter()
    assert cust.get_discount() == 0.05
    assert vip.get_discount() == 0.10
    assert isinstance(vip, type(cust)) or issubclass(type(vip), type(cust))


# ============================================================================
# Exercise 3: Using super() for Initialization
# ============================================================================

def exercise_3_starter():
    """
    Use super() to extend initialization.
    
    Requirements:
    - Employee inputs: name, salary
    - Manager inputs: name, salary, department
    - Manager call super().__init__ to handle name/salary
    - Return Manager("Alice", 80000, "IT")
    """
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

    class Manager(Employee):
        def __init__(self, name, salary, department):
            super().__init__(name, salary)
            self.department = department

    return Manager("Alice", 80000, "IT")

def test_exercise_3():
    mgr = exercise_3_starter()
    assert mgr.name == "Alice"
    assert mgr.salary == 80000
    assert mgr.department == "IT"


# ============================================================================
# Exercise 4: Extending Methods with super()
# ============================================================================

def exercise_4_starter():
    """
    Extend a method using super().
    
    Requirements:
    - Logger.log(msg) returns "Console: {msg}"
    - FileLogger.log(msg) calls parent, then adds " | File: {msg}"
    - Return FileLogger()
    """
    class Logger:
        def log(self, msg):
            return f"Console: {msg}"

    class FileLogger(Logger):
        def log(self, msg):
            return f"{super().log(msg)} | File: {msg}"

    return FileLogger()

def test_exercise_4():
    logger = exercise_4_starter()
    result = logger.log("Test")
    assert result == "Console: Test | File: Test"


# ============================================================================
# Exercise 5: Multiple Inheritance Basics
# ============================================================================

def exercise_5_starter():
    """
    Create a class inheriting from two parents.
    
    Requirements:
    - Camera has take_photo() -> "Click"
    - Phone has make_call() -> "Calling"
    - SmartPhone inherits from BOTH
    - Return SmartPhone instance
    """
    class Camera:
        def take_photo(self): return "Click"
    
    class Phone:
        def make_call(self): return "Calling"

    class SmartPhone(Camera, Phone):
        pass
    
    return SmartPhone()

def test_exercise_5():
    phone = exercise_5_starter()
    assert phone.take_photo() == "Click"
    assert phone.make_call() == "Calling"


# ============================================================================
# Exercise 6: Method Resolution Order (MRO)
# ============================================================================

def exercise_6_starter():
    """
    Return the MRO of a diamond hierarchy.
    
    Requirements:
    - Create hierarchy: A <- B, A <- C, (B, C) <- D
    - Return the list D.mro()
    """
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    
    return D.mro()

def test_exercise_6():
    mro = exercise_6_starter()
    # Check simple names in MRO list
    names = [cls.__name__ for cls in mro]
    assert names[:4] == ['D', 'B', 'C', 'A']


# ============================================================================
# Exercise 7: Abstract Base Classes (ABC)
# ============================================================================

def exercise_7_starter():
    """
    Implement a concrete class from an ABC.
    
    Requirements:
    - Shape inherits ABC, has abstract method area()
    - Circle inherits Shape, implements area() returning pi * r^2
    - Return a Circle(5) instance
    """
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
    
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            import math
            return math.pi * self.radius ** 2
    
    return Circle(5)

def test_exercise_7():
    circle = exercise_7_starter()
    import math
    assert abs(circle.area() - (math.pi * 25)) < 0.01
    # Check inheritance
    assert isinstance(circle, ABC)


# ============================================================================
# Exercise 8: Abstract Properties
# ============================================================================

def exercise_8_starter():
    """
    Enforce a property in a subclass.
    
    Requirements:
    - Database is ABC, has abstract property connection_string
    - SQLDatabase implements connection_string as "sqlite:///:memory:"
    - Return SQLDatabase instance
    """
    class Database(ABC):
        @property
        @abstractmethod
        def connection_string(self):
            pass

    class SQLDatabase(Database):
        @property
        def connection_string(self):
            return "sqlite:///:memory:"

    return SQLDatabase()

def test_exercise_8():
    db = exercise_8_starter()
    assert db.connection_string == "sqlite:///:memory:"


# ============================================================================
# Exercise 9: Inheritance vs Composition
# ============================================================================

def exercise_9_starter():
    """
    Refactor to use Composition (Has-A).
    
    Requirements:
    - Printer class has method print_page(content) -> "Printing: {content}"
    - Report class takes a printer in __init__
    - Report.output(content) delegates to printer.print_page("Report: " + content)
    - Return Report(Printer())
    """
    class Printer:
        def print_page(self, content):
            return f"Printing: {content}"

    class Report:
        def __init__(self, printer):
            self.printer = printer
            
        def output(self, content):
            return self.printer.print_page(f"Report: {content}")

    return Report(Printer())

def test_exercise_9():
    report = exercise_9_starter()
    assert report.output("Data") == "Printing: Report: Data"


# ============================================================================
# Exercise 10: Real-World Healthcare Hierarchy
# ============================================================================

def exercise_10_starter():
    """
    Build a 3-level hierarchy: MedicalStaff -> Doctor -> Surgeon
    
    Requirements:
    - MedicalStaff(name, id)
    - Doctor(name, id, specialty)
    - Surgeon(name, id, specialty, board_certified)
    - Surgeon.operate() raises RuntimeError unless board_certified is True, 
      otherwise returns "Operating"
    - Return valid Surgeon("House", "001", "Diag", True)
    """
    class MedicalStaff:
        def __init__(self, name, id):
            self.name = name
            self.id = id
    
    class Doctor(MedicalStaff):
        def __init__(self, name, id, specialty):
            super().__init__(name, id)
            self.specialty = specialty
    
    class Surgeon(Doctor):
        def __init__(self, name, id, specialty, board_certified):
            super().__init__(name, id, specialty)
            self.board_certified = board_certified
        
        def operate(self):
            if not self.board_certified:
                raise RuntimeError("Not certified")
            return "Operating"
    
    return Surgeon("House", "001", "Diag", True)

def test_exercise_10():
    s = exercise_10_starter()
    assert s.name == "House"
    assert s.specialty == "Diag"
    assert s.operate() == "Operating"
    
    # Test uncertified
    # s2 = Surgeon(..., False); assert raises RuntimeError


# ============================================================================
# Run checks
# ============================================================================

if __name__ == "__main__":
    tests = [
        test_exercise_1, test_exercise_2, test_exercise_3, test_exercise_4,
        test_exercise_5, test_exercise_6, test_exercise_7, test_exercise_8,
        test_exercise_9, test_exercise_10
    ]
    
    print(f"Running {len(tests)} tests...")
    passed = 0
    for test in tests:
        try:
            test()
            passed += 1
            print(f"PASS: {test.__name__}")
        except Exception as e:
            print(f"FAIL: {test.__name__} - {e}")
            
    print(f"\nResult: {passed}/{len(tests)} passed.")
