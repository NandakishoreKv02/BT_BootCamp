"""
Lab 2: Appointment Reminder Generator - Starter Code
"""

def generate_reminders(patient_names, time_str):
    """
    Generate the list of reminder messages.
    
    Args:
        patient_names (list): List of strings.
        time_str (str): The common time.
        
    Returns:
        list: List of reminder messages.
    """
    reminders = []
    for name in patient_names:
        reminders.append(f"Reminder: {name}, your appointment is at {time_str}.")
    return reminders

if __name__ == "__main__":
    names = ["Alice Doe", "John Smith"]
    time = "09:30 AM"
    print(generate_reminders(names, time))
