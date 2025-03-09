class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    def to_file_format(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"


class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self, employee):
        with open(self.filename, "a") as file:
            file.write(employee.to_file_format())
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()
                if not records:
                    print("No employee records found.")
                else:
                    print("\nEmployee Records:")
                    for record in records:
                        print(record.strip())  # Remove newline and print each record
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()
                found = False
                for record in records:
                    if record.startswith(str(employee_id)):
                        print(f"Employee Found:\n{record.strip()}")
                        found = True
                        break
                if not found:
                    print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()

            with open(self.filename, "w") as file:
                updated = False
                for record in records:
                    parts = record.strip().split(",")
                    if parts[0] == str(employee_id):
                        if name:
                            parts[1] = name
                        if position:
                            parts[2] = position
                        if salary:
                            parts[3] = str(salary)
                        file.write(",".join(parts) + "\n")
                        print(f"Employee {employee_id} updated successfully!")
                        updated = True
                    else:
                        file.write(record)
                if not updated:
                    print(f"Employee {employee_id} not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()

            with open(self.filename, "w") as file:
                deleted = False
                for record in records:
                    if record.startswith(str(employee_id)):
                        print(f"Employee {employee_id} deleted successfully!")
                        deleted = True
                    else:
                        file.write(record)

                if not deleted:
                    print(f"Employee {employee_id} not found.")
        except FileNotFoundError:
            print("No employee records found.")


class EmployeeManagementSystem:
    def __init__(self):
        self.manager = EmployeeManager()

    def show_menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.manager.view_all_employees()
            elif choice == '3':
                self.search_employee()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_employee(self):
        try:
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(employee_id, name, position, salary)
            self.manager.add_employee(employee)
        except ValueError:
            print("Invalid input. Salary must be a number.")

    def search_employee(self):
        try:
            employee_id = input("Enter Employee ID to search: ")
            self.manager.search_employee(employee_id)
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")

    def update_employee(self):
        try:
            employee_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name: ")
            position = input("Enter new Position: ")
            salary_input = input("Enter new Salary: ")

            salary = float(salary_input) if salary_input else None
            self.manager.update_employee(employee_id, name or None, position or None, salary)
        except ValueError:
            print("Invalid input. Salary must be a number.")

    def delete_employee(self):
        try:
            employee_id = input("Enter Employee ID to delete: ")
            self.manager.delete_employee(employee_id)
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")


if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.show_menu()
