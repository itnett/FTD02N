python
     class Organization:
         def __init__(self, name):
             self.name = name
             self.values = []

         def add_value(self, value):
             self.values.append(value)

     org = Organization('Tech Innovators')
     org.add_value('Innovation')
     org.add_value('Collaboration')
     org.add_value('Integrity')

     print(f"{org.name} values: {', '.join(org.values)}")