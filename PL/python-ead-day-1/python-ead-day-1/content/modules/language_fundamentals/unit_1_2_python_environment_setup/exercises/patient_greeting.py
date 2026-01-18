import sys
def greet_patient(patient_name, doctor_name):
    return f"Hello {patient_name}, Dr. {doctor_name} will see you shortly."

if __name__ == "__main__":
    message = greet_patient(sys.argv[1], sys.argv[2])
    #message = greet_patient("John Doe", "Smith")
    print(message)