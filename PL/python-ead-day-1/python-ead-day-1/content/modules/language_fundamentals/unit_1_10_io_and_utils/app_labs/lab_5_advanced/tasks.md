# Lab 5: Patient Electronic Archive - Tasks

## Task 1: The Input function
Inside `archive_patient`, use `input()` to collect 3 strings: `mrn`, `name`, and `diagnosis`.

## Task 2: Functional Abstraction
To make this testable, define a helper function `write_record_to_disk(mrn, name, diagnosis)`.

## Task 3: File Creation
Inside the helper, open a file using `f"{mrn}.txt"` in write (`'w'`) mode.

## Task 4: Multiline Writing
Write the three required labels and values. Ensure each line ends with a newline.

## Task 5: Integration
Call `write_record_to_disk` from within `archive_patient`.
