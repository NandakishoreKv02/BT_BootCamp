from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        print()
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        address=Address()
        emp.emp_id=input("Enter Employee ID: ")
        emp.name=input("Enter Employee Name: ")
        emp.gender=input("Enter Employee Gender: ")
        address.address1=input("Enter Address1: ")
        address.address2=input("Enter Address2: ")
        address.city=input("Enter City: ")
        address.pincode=input("Enter Pincode: ")
        emp.address=address

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
         print(f"Employee Id : {emp.emp_id}")
         print(f"Employee Name : {emp.name}")
         print(f"Employee Gender : {emp.gender}")

         print("Employee Address : --------------")
         print(f"Address 1 : {emp.address.address1}")
         print(f"Address 2 : {emp.address.address2}")
         print(f"City : {emp.address.city}")
         print(f"PinCode : {emp.address.pincode}")
         print("----------------------------------")
        

if __name__ == "__main__":
    Program.main([])
