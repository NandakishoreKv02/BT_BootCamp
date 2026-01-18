# Lab 4: Resilient Vital Sign Batch Processor - Tasks

## Task 1: Initialize
Create an empty list called `results`.

## Task 2: Robust Loop
Start a `for` loop to iterate through the input list.

## Task 3: Error Trapping
Put the conversion `int(signal)` inside a `try` block.

## Task 4: Logging and Continuity
In the `except ValueError:` block:
- Print exactly: `Skipping corrupt signal: [signal]`.
- Use `continue` (though it's implicit at the end of the loop, it's good practice here).

## Task 5: Collect and Return
Append successful integers to `results` and return the list after the loop completes.
