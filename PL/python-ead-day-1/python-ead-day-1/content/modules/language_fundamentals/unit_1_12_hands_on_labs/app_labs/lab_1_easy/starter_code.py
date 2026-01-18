"""
Lab 1: BMI Calculator & Health Advisor - Starter Code
"""

def get_valid_input(prompt, input_type):
    """
    Get and validate user input.
    
    Args:
        prompt (str): Message to display to user
        input_type (type): Type to convert to (float or int)
    
    Returns:
        Validated input of specified type
    """
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")


def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value rounded to 2 decimal places
    """
    return round(weight / (height ** 2), 2)


def categorize_bmi(bmi):
    """
    Categorize BMI according to WHO standards.
    
    Args:
        bmi (float): BMI value
    
    Returns:
        str: Category name
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def generate_recommendation(category):
    """
    Generate health recommendation based on category.
    
    Args:
        category (str): BMI category
    
    Returns:
        str: Health recommendation
    """
    recommendations = {
        "Underweight": "Consider consulting a nutritionist to gain weight healthily.",
        "Normal Weight": "Great! Maintain your healthy lifestyle.",
        "Overweight": "Consider a balanced diet and regular exercise.",
        "Obese": "Consult a healthcare provider for a personalized weight management plan."
    }
    return recommendations.get(category, "Consult a healthcare provider.")


def display_report(weight, height, bmi, category, recommendation):
    """
    Display formatted health assessment report.
    
    Args:
        weight (float): Weight in kg
        height (float): Height in m
        bmi (float): Calculated BMI
        category (str): BMI category
        recommendation (str): Health advice
    """
    print("\n" + "="*50)
    print("BMI HEALTH ASSESSMENT REPORT")
    print("="*50)
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi}")
    print(f"Category: {category}")
    print("-"*50)
    print(f"Recommendation: {recommendation}")
    print("="*50)


def main():
    """Main program orchestrator."""
    print("Welcome to BMI Calculator & Health Advisor")
    weight = get_valid_input("Enter your weight (kg): ", float)
    height = get_valid_input("Enter your height (m): ", float)
    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    recommendation = generate_recommendation(category)
    display_report(weight, height, bmi, category, recommendation)


if __name__ == "__main__":
    # main()  # Uncomment when ready to test
    pass
