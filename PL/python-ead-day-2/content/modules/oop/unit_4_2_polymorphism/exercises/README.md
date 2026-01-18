# Unit 4.2: Polymorphism - Exercises

## Overview

This unit contains 10 progressive exercises covering Python polymorphism concepts, including duck typing, method overriding, operator overloading, and Abstract Base Classes (ABCs).

**File**: `unit_4_2_polymorphism_exercises.py`

---

## Exercise List

### Exercise 1: Basic Duck Typing
**Objective**: Implement a function that works with any object having a specific method.

**Description**: Create a function `play_audio` that accepts any object with a `play()` method. Create two classes `MP3` and `WAV` that implement `play()`.

**Inputs/Outputs**:
- Input: `MP3` or `WAV` instance.
- Output: "Playing MP3" or "Playing WAV".

**Requirements**:
- Classes `MP3` and `WAV` must have `play()`.
- Function `play_audio(file)` calls `file.play()`.

**Hints**:
1. **Hint 1**: The function doesn't check types.
2. **Hint 2**: Just define the method `play(self)` in both classes.
3. **See Solution**: Check solution file.

---

### Exercise 2: Polymorphism with Inheritance
**Objective**: Override a base method to provide specific implementation.

**Description**: Create a `Shape` base class with `area()`. Create `Rectangle` and `Circle` subclasses that override `area()`.

**Inputs/Outputs**:
- `Rectangle(10, 5).area()` -> 50
- `Circle(3).area()` -> ~28.27

**Requirements**:
- Base `Shape.area()` can satisfy with pass or raise error.
- Subclasses must implement the logic.
- A list of shapes [Rect, Circle] should be iterable calling `.area()`.

**Hints**:
1. **Hint 1**: `class Child(Parent):`.
2. **Hint 2**: Override means defining the function with the same name.
3. **See Solution**: Check solution file.

---

### Exercise 3: Flexible Data Processing (Duck Typing)
**Objective**: Process a list of different objects that share a method signature.

**Description**: You have `EmailSender` and `SMSSender`. Both have `send(msg)`. Write a function `notify_all` that takes a list of senders and a message, and calls `send` on all of them.

**Inputs/Outputs**:
- Input: `[EmailSender(), SMSSender()]`, "Hello"
- Output: Returns list of strings ["Email: Hello", "SMS: Hello"]

**Requirements**:
- `EmailSender.send` returns "Email: {msg}".
- `SMSSender.send` returns "SMS: {msg}".
- `notify_all` iterates and collects results.

**Hints**:
1. **Hint 1**: Loop through the list.
2. **Hint 2**: Call `item.send(msg)` on each iteration.
3. **See Solution**: Check solution file.

---

### Exercise 4: Operator Overloading (Addition)
**Objective**: Customizing the `+` operator.

**Description**: Create a `CartItem` class with `name` and `price`. Allow two `CartItem`s to be added together to return the total price.

**Inputs/Outputs**:
- `CartItem("Apple", 1.0) + CartItem("Banana", 2.0)` -> 3.0

**Requirements**:
- Implement `__add__(self, other)`.
- Return `self.price + other.price`.

**Hints**:
1. **Hint 1**: `def __add__(self, other):`.
2. **Hint 2**: Access `other.price`.
3. **See Solution**: Check solution file.

---

### Exercise 5: Operator Overloading (Comparison)
**Objective**: Customizing comparison operators (`>`, `<`).

**Description**: Create a `Student` class with `grade`. Allow comparing students directly: `student1 > student2` based on grade.

**Inputs/Outputs**:
- `Student(90) > Student(80)` -> True

**Requirements**:
- Implement `__gt__` (greater than).
- Implement `__lt__` (less than).

**Hints**:
1. **Hint 1**: `def __gt__(self, other):`.
2. **Hint 2**: Return boolean result of grade comparison.
3. **See Solution**: Check solution file.

---

### Exercise 6: String Representation Polymorphism
**Objective**: Customizing `str()` and `repr()`.

**Description**: Create a `Book` class. `str(book)` should be user-friendly ("Title by Author"). `repr(book)` should be developer-friendly ("Book(title='...', author='...')").

**Inputs/Outputs**:
- `str(Book("1984", "Orwell"))` -> "1984 by Orwell"
- `repr(Book("1984", "Orwell"))` -> "Book(title='1984', author='Orwell')"

**Requirements**:
- Implement `__str__` and `__repr__`.

**Hints**:
1. **Hint 1**: `__str__` is for users, `__repr__` for debugging.
2. **Hint 2**: Use f-strings.
3. **See Solution**: Check solution file.

---

### Exercise 7: Abstract Base Classes (Enforcing Interfaces)
**Objective**: Use ABC to enforce a contract.

**Description**: Create an abstract `PaymentMethod` with abstract `pay(amount)`. Implement `CreditCard` and `PayPal`.

**Inputs/Outputs**:
- `CreditCard().pay(100)` -> "Paid 100 via CC"
- `PaymentMethod()` -> TypeError

**Requirements**:
- Inherit `ABC`. Decorate `pay` with `@abstractmethod`.
- Subclasses must implement `pay`.

**Hints**:
1. **Hint 1**: `from abc import ABC, abstractmethod`.
2. **Hint 2**: Abstract classes cannot be instantiated.
3. **See Solution**: Check solution file.

---

### Exercise 8: Length Polymorphism
**Objective**: Customizing `len()` behavior.

**Description**: Create a `Playlist` class that holds a list of songs. `len(playlist)` should return the number of songs.

**Inputs/Outputs**:
- `len(Playlist(["A", "B", "C"]))` -> 3

**Requirements**:
- Implement `__len__`.
- It should return the length of the internal list.

**Hints**:
1. **Hint 1**: `def __len__(self):`.
2. **Hint 2**: Delegate to `len(self.songs)`.
3. **See Solution**: Check solution file.

---

### Exercise 9: Callable Objects
**Objective**: Making objects behave like functions.

**Description**: Create a `Multiplier` class initialized with a factor `k`. Calling the instance `m(5)` should return `5 * k`.

**Inputs/Outputs**:
- `double = Multiplier(2)`
- `double(10)` -> 20

**Requirements**:
- Implement `__call__(self, value)`.

**Hints**:
1. **Hint 1**: The `__call__` method makes the object callable.
2. **Hint 2**: Like a function, it can take arguments.
3. **See Solution**: Check solution file.

---

### Exercise 10: Complete Polymorphic System (Healthcare)
**Objective**: Integrate inheritance, polymorphism, and overriding.

**Description**: Create a `Medication` system.
- Base `Medication` has `name` and `administer()`.
- `Pill` overrides `administer()` -> "Swallow {name}".
- `Injection` overrides `administer()` -> "Inject {name}".
- Write a function `give_meds(patient_name, meds_list)` that prints actions.

**Inputs/Outputs**:
- List includes Pill and Injection.
- Function returns list of action strings.

**Requirements**:
- Polymorphic iteration over `meds_list`.
- `administer()` called on each.

**Hints**:
1. **Hint 1**: No type checking needed in `give_meds` loop.
2. **Hint 2**: Returns formatted strings.
3. **See Solution**: Check solution file.
