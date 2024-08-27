python
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def display_info(self):
            print(f"Name: {self.name}, Position: {self.position}")

    emp1 = Employee("John Doe", "Manager")
    emp1.display_info()