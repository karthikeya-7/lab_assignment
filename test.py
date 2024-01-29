class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        print("Employee ID\tName\tAge\tSalary")
        print("-" * 40)
        for employee in self.employees:
            print(employee)

    def sort_table(self, key):
        self.employees = sorted(self.employees, key=lambda x: getattr(x, key.lower()))

    def get_user_choice(self):
        print("\nSort by:")
        print("1. Age")
        print("2. Name")
        print("3. Salary")
        choice = input("Enter your choice (1/2/3): ")
        return choice.lower()


if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    employee_table = EmployeeTable(employees_data)

    while True:
        employee_table.display_table()
        sorting_choice = employee_table.get_user_choice()

        if sorting_choice in ("1", "2", "3"):
            employee_table.sort_table(sorting_choice)
        else:
            print("Invalid choice. Exiting.")
            break
