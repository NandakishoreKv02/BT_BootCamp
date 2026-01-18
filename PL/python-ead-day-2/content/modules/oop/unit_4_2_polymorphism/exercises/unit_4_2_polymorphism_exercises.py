"""
Unit 4.2: Polymorphism - Exercises
Drills covering duck typing, overriding, operator overloading, and ABCs.
"""
from abc import ABC, abstractmethod
import math

# ============================================================================
# Exercise 1: Basic Duck Typing
# ============================================================================

def exercise_1_starter():
    """
    Implement classes MP3 and WAV with a play() method.
    
    Requirements:
    - MP3.play() returns "Playing MP3"
    - WAV.play() returns "Playing WAV"
    - play_audio(obj) calls obj.play() and returns the result
    - Return a tuple: (play_audio(MP3()), play_audio(WAV()))
    """
    class MP3:
        def play(self):
            return "Playing MP3"

    class WAV:
        def play(self):
            return "Playing WAV"

    def play_audio(audio_file):
        return audio_file.play()

    return (play_audio(MP3()), play_audio(WAV()))

def test_exercise_1():
    res1, res2 = exercise_1_starter()
    assert res1 == "Playing MP3"
    assert res2 == "Playing WAV"


# ============================================================================
# Exercise 2: Polymorphism with Inheritance
# ============================================================================

def exercise_2_starter():
    """
    Override base class method area().
    
    Requirements:
    - Shape.area() returns 0
    - Rectangle(w, h).area() returns w * h
    - Circle(r).area() returns pi * r^2
    - Return list of areas: [Rectangle(10,5).area(), Circle(3).area()]
    """
    class Shape:
        def area(self): return 0

    class Rectangle(Shape):
        def __init__(self, w, h):
            self.w = w
            self.h = h
        def area(self):
            return self.w * self.h

    class Circle(Shape):
        def __init__(self, r):
            self.r = r
        def area(self):
            return math.pi * self.r ** 2

    return [Rectangle(10, 5).area(), Circle(3).area()]

def test_exercise_2():
    areas = exercise_2_starter()
    assert areas[0] == 50
    assert abs(areas[1] - (math.pi * 9)) < 0.01


# ============================================================================
# Exercise 3: Flexible Data Processing (Duck Typing)
# ============================================================================

def exercise_3_starter():
    """
    Process a list of different objects lacking a common base class.
    
    Requirements:
    - EmailSender.send(msg) -> "Email: {msg}"
    - SMSSender.send(msg) -> "SMS: {msg}"
    - notify_all(senders, msg) -> returns list of their responses
    - Return result of notify_all([EmailSender(), SMSSender()], "Hello")
    """
    class EmailSender:
        def send(self, msg):
            return f"Email: {msg}"
    
    class SMSSender:
        def send(self, msg):
            return f"SMS: {msg}"
    
    def notify_all(senders, msg):
        return [s.send(msg) for s in senders]

    return notify_all([EmailSender(), SMSSender()], "Hello")

def test_exercise_3():
    results = exercise_3_starter()
    assert results == ["Email: Hello", "SMS: Hello"]


# ============================================================================
# Exercise 4: Operator Overloading (Addition)
# ============================================================================

def exercise_4_starter():
    """
    Overload the + operator.
    
    Requirements:
    - CartItem(name, price)
    - CartItem + CartItem returns sum of prices (float)
    - Return result of CartItem("A", 10.0) + CartItem("B", 20.0)
    """
    class CartItem:
        def __init__(self, name, price):
            self.name = name
            self.price = price
        
        def __add__(self, other):
            return self.price + other.price

    return CartItem("A", 10.0) + CartItem("B", 20.0)

def test_exercise_4():
    total = exercise_4_starter()
    assert total == 30.0


# ============================================================================
# Exercise 5: Operator Overloading (Comparison)
# ============================================================================

def exercise_5_starter():
    """
    Overload > and < operators.
    
    Requirements:
    - Student(grade)
    - s1 > s2 based on grade
    - s1 < s2 based on grade
    - Return tuple: (Student(90) > Student(80), Student(70) < Student(80))
    """
    class Student:
        def __init__(self, grade):
            self.grade = grade
            
        def __gt__(self, other):
            return self.grade > other.grade
        
        def __lt__(self, other):
            return self.grade < other.grade

    return (Student(90) > Student(80), Student(70) < Student(80))

def test_exercise_5():
    res1, res2 = exercise_5_starter()
    assert res1 is True
    assert res2 is True


# ============================================================================
# Exercise 6: String Representation Polymorphism
# ============================================================================

def exercise_6_starter():
    """
    Implement __str__ and __repr__.
    
    Requirements:
    - Book(title, author)
    - str(book) -> "{title} by {author}"
    - repr(book) -> "Book(title='{title}', author='{author}')"
    - Return tuple: (str(b), repr(b)) for Book("1984", "Orwell")
    """
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
            
        def __str__(self):
            return f"{self.title} by {self.author}"
        
        def __repr__(self):
            return f"Book(title='{self.title}', author='{self.author}')"

    b = Book("1984", "Orwell")
    return (str(b), repr(b))

def test_exercise_6():
    s, r = exercise_6_starter()
    assert s == "1984 by Orwell"
    assert "Book(title='1984'" in r


# ============================================================================
# Exercise 7: Abstract Base Classes
# ============================================================================

def exercise_7_starter():
    """
    Enforce interface with ABC.
    
    Requirements:
    - PaymentMethod is ABC with abstract pay(amount)
    - CreditCard.pay(amount) -> "CC: {amount}"
    - Return CreditCard().pay(100)
    """
    class PaymentMethod(ABC):
        @abstractmethod
        def pay(self, amount):
            pass
    
    class CreditCard(PaymentMethod):
        def pay(self, amount):
            return f"CC: {amount}"
    
    return CreditCard().pay(100)

def test_exercise_7():
    res = exercise_7_starter()
    assert res == "CC: 100"


# ============================================================================
# Exercise 8: Length Polymorphism
# ============================================================================

def exercise_8_starter():
    """
    Implement __len__.
    
    Requirements:
    - Playlist(songs_list)
    - len(playlist) returns count of songs
    - Return len(Playlist(["A", "B", "C"]))
    """
    class Playlist:
        def __init__(self, songs):
            self.songs = songs
            
        def __len__(self):
            return len(self.songs)

    return len(Playlist(["A", "B", "C"]))

def test_exercise_8():
    count = exercise_8_starter()
    assert count == 3


# ============================================================================
# Exercise 9: Callable Objects
# ============================================================================

def exercise_9_starter():
    """
    Implement __call__.
    
    Requirements:
    - Multiplier(factor)
    - instance(val) returns val * factor
    - Return Multiplier(3)(10)
    """
    class Multiplier:
        def __init__(self, factor):
            self.factor = factor
            
        def __call__(self, value):
            return value * self.factor

    return Multiplier(3)(10)

def test_exercise_9():
    res = exercise_9_starter()
    assert res == 30


# ============================================================================
# Exercise 10: Complete Polymorphic System
# ============================================================================

def exercise_10_starter():
    """
    Healthcare polymorphic iteration.
    
    Requirements:
    - Medication base class with administer() -> "Generic"
    - Pill(name) overrides -> "Swallow {name}"
    - Injection(name) overrides -> "Inject {name}"
    - give_meds(meds) iterates and calls administer()
    - Return result of give_meds([Pill("Aspirin"), Injection("Insulin")])
    """
    class Medication:
        def __init__(self, name):
            self.name = name
        def administer(self):
            return "Generic"
    
    class Pill(Medication):
        def administer(self):
            return f"Swallow {self.name}"
    
    class Injection(Medication):
        def administer(self):
            return f"Inject {self.name}"
    
    def give_meds(meds):
        return [m.administer() for m in meds]
        
    return give_meds([Pill("Aspirin"), Injection("Insulin")])

def test_exercise_10():
    results = exercise_10_starter()
    assert results == ["Swallow Aspirin", "Inject Insulin"]


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
