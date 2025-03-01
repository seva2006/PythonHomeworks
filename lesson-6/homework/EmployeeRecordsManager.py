f=open('employees.txt','wt')
def add_employee():
  with open("employees.txt", "a") as file:
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    salary = input("Enter Employee Salary: ")


    file.write(f"{emp_id},{name},{position},{salary}\n")
    print("Employee record added successfully.\n")


def view_employees():
    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No employee records found.\n")
            else:
                print("Employee ID | Name | Position | Salary")
                for line in lines:
                    emp_id, name, position, salary = line.strip().split(',')
                    print(f"{emp_id} | {name} | {position} | {salary}")
    except FileNotFoundError:
        print("No records found. Please add some employee records first.\n")


def search_employee():
    emp_id_to_search = input("Enter Employee ID to search: ")

    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()
            found = False
            for line in lines:
                emp_id, name, position, salary = line.strip().split(',')
                if emp_id == emp_id_to_search:
                    print(f"Employee found: {emp_id} | {name} | {position} | {salary}\n")
                    found = True
                    break
            if not found:
                print("Employee not found.\n")
    except FileNotFoundError:
        print("No records found. Please add some employee records first.\n")



def update_employee():
    emp_id_to_update = input("Enter Employee ID to update: ")
    updated = False

    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()

        with open("employees.txt", "w") as file:
            for line in lines:
                emp_id, name, position, salary = line.strip().split(',')
                if emp_id == emp_id_to_update:
                    print(f"Found employee: {emp_id} | {name} | {position} | {salary}")
                    name = input("Enter new Name (leave blank to keep current): ") or name
                    position = input("Enter new Position (leave blank to keep current): ") or position
                    salary = input("Enter new Salary (leave blank to keep current): ") or salary
                    file.write(f"{emp_id},{name},{position},{salary}\n")
                    updated = True
                    print("Employee record updated.\n")
                else:
                    file.write(line)

        if not updated:
            print("Employee ID not found.\n")
    except FileNotFoundError:
        print("No records found. Please add some employee records first.\n")


def delete_employee():
    emp_id_to_delete = input("Enter Employee ID to delete: ")
    deleted = False

    try:
        with open("employees.txt", "r") as file:
            lines = file.readlines()

        with open("employees.txt", "w") as file:
            for line in lines:
                emp_id, name, position, salary = line.strip().split(',')
                if emp_id == emp_id_to_delete:
                    print(f"Employee record deleted: {emp_id} | {name} | {position} | {salary}")
                    deleted = True
                else:
                    file.write(line)

        if not deleted:
            print("Employee ID not found.\n")
    except FileNotFoundError:
        print("No records found. Please add some employee records first.\n")


def display_menu():
    print("Menu Options:")
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()