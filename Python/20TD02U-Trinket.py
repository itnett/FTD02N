python
class Robot:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move_forward(self, steps):
        self.position += steps
        return self.position

    def move_backward(self, steps):
        self.position -= steps
        return self.position

    def status(self):
        return f"Robot {self.name} is at position {self.position}"

# Eksempel på bruk
robot1 = Robot("Robo1")
print(robot1.status())  # Forventet: Robot Robo1 is at position 0
robot1.move_forward(10)
print(robot1.status())  # Forventet: Robot Robo1 is at position 10
robot1.move_backward(5)
print(robot1.status())  # Forventet: Robot Robo1 is at position 5