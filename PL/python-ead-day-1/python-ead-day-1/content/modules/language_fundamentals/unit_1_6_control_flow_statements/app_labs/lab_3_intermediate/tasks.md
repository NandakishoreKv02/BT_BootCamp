# Lab 3: Vital Sign Monitor - Tasks

## Task 1: Setup
Create an index variable `i` starting at 0.

## Task 2: While Condition
Construct a `while` loop that runs as long as:
1. `i` is less than the length of the `readings` list.
2. The current reading `readings[i]` is OUTSIDE the 60-100 range (either `< 60` or `> 100`).

## Task 3: Increment
Inside the loop, increment `i` by 1.

## Task 4: Final Check
After the loop:
- If `i` reached the end and no stable reading was found, return `None`.
- Otherwise, return the reading at `readings[i]` that broke the loop.
