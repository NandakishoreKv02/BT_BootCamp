# Lab 1: BMI Calculator & Health Advisor - Tasks

## Task 1: Input Validation Function
Create `get_valid_input(prompt, input_type)`:
- Display the prompt to the user
- Attempt to convert input to the specified type (float or int)
- Use try/except to handle ValueError
- Keep asking until valid input is received
- Return the validated value

## Task 2: BMI Calculation
Create `calculate_bmi(weight, height)`:
- Apply the formula: BMI = weight / (height²)
- Round to 2 decimal places
- Return the BMI value

## Task 3: Category Classification
Create `categorize_bmi(bmi)`:
- Use if/elif/else to determine category
- Return appropriate category string

## Task 4: Health Recommendations
Create `generate_recommendation(category)`:
- Use a dictionary or if/elif to map categories to advice
- Return personalized recommendation string

## Task 5: Report Formatting
Create `display_report(weight, height, bmi, category, recommendation)`:
- Print a well-formatted report using f-strings
- Include visual separators (lines of = or -)
- Display all parameters clearly

## Task 6: Main Orchestrator
Create `main()`:
- Print welcome message
- Call get_valid_input for weight and height
- Call calculate_bmi
- Call categorize_bmi
- Call generate_recommendation
- Call display_report
- Use if __name__ == "__main__": to run main()
