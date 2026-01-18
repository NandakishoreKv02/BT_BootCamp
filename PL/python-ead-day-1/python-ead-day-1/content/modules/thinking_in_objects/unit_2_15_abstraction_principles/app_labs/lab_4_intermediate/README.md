---
title: "The Multi-Channel Notifier"
type: app_lab
module: thinking_in_objects
unit: unit_2_15_abstraction_principles
lab_number: 4
difficulty: intermediate
use_case: abstract-communication
domain: healthcare
order: 4
duration_hours: 2
tags:
  topics: ["abc", "polymorphism", "notification-systems"]
---

# Lab 4: The Multi-Channel Notifier

**Module**: Thinking in Objects
**Objective**: Use abstraction to create a notification system that can send alerts via multiple channels (Email, SMS, Pager) through a unified interface.
**Difficulty**: Intermediate
**Context**: Emergency Communications

## Problem Statement
A hospital needs to notify staff about emergencies. Different staff members prefer different notification methods. You must create an abstract `Notifier` class with a `send_alert` method, and then implement three concrete notifiers: `EmailNotifier`, `SMSNotifier`, and `PagerNotifier`.

## Requirements
1.  **Abstract Base**:
    - Class `Notifier(ABC)`.
    - `@abstractmethod send_alert(self, message, recipient)`.
2.  **Concrete Classes**:
    - `EmailNotifier.send_alert()`: Returns "Email to {recipient}: {message}".
    - `SMSNotifier.send_alert()`: Returns "SMS to {recipient}: {message}".
    - `PagerNotifier.send_alert()`: Returns "Page to {recipient}: {message}".
3.  **Polymorphic Usage**:
    - Store all three notifiers in a list.
    - Loop through the list and call `send_alert` on each.

## Expected Output
```text
Broadcasting Emergency Code Blue...
Email to staff@hospital.com: Code Blue in ICU
SMS to +1-555-0199: Code Blue in ICU
Page to Dr. Smith: Code Blue in ICU
```
