# Lab 4 Tasks

## Task 1: Abstract Notifier
- Create `Notifier(ABC)` with an abstract `send_alert(message, recipient)`.

## Task 2: Concrete Implementations
- Define `EmailNotifier`, `SMSNotifier`, and `PagerNotifier`.
- Each must implement `send_alert` with appropriate formatting.

## Task 3: Polymorphic Loop
In `main()`:
1. Create a list containing one instance of each notifier type.
2. Define a message "Code Blue in ICU".
3. Loop through the list and call `send_alert` on each with different recipients.
4. Print all outputs.
