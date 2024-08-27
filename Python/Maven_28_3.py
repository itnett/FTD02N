python
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

    class Department:
        def __init__(self, name):
            self.name = name
            self.employees = []

        def add_employee(self, employee):
            self.employees.append(employee)

        def display_structure(self):
            print(f"Avdeling: {self.name}")
            for emp in self.employees:
                print(f" - {emp.name}, {emp.position}")

    # Eksempelbruk
    it_department = Department("IT")
    it_department.add_employee(Employee("John Doe", "Manager"))
    it_department.add_employee(Employee("Jane Smith", "Developer"))

    it_department.display_structure()