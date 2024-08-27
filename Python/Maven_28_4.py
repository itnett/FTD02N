python
    class Training:
        def __init__(self, name, date, employee):
            self.name = name
            self.date = date
            self.employee = employee

    trainings = []
    trainings.append(Training("Python Programming", "2024-01-15", "John Doe"))

    for training in trainings:
        print(f"{training.employee} fullførte {training.name} på {training.date}")