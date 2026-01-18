class ClinicError(Exception):
    pass

class SchedulingError(ClinicError):
    pass

class BillingError(ClinicError):
    pass

def book_appointment(patient, time):
    """
    TODO:
    If time is "night", raise SchedulingError.
    Else return "Appointment Confirmed".
    """
    # WRITE CODE HERE
    pass

def collect_payment(amount):
    """
    TODO:
    If amount < 0, raise BillingError.
    Else return "Payment Received".
    """
    # WRITE CODE HERE
    pass

def run_clinic_op(op_func, *args):
    """
    TODO:
    1. Try logic.
    2. Catch ClinicError (base class).
    3. Return string representation of the error.
    """
    # WRITE CODE HERE
    pass

def main():
    print(run_clinic_op(book_appointment, "Alice", "night"))
    print(run_clinic_op(collect_payment, -10))
    print(run_clinic_op(book_appointment, "Bob", "morning"))

if __name__ == "__main__":
    main()
