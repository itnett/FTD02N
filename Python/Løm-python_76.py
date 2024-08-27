python
     class LeadershipStyle:
         def __init__(self, name, description):
             self.name = name
             self.description = description

     democratic = LeadershipStyle('Democratic', 'Decisions are made with input from team members')
     autocratic = LeadershipStyle('Autocratic', 'Decisions are made solely by the leader')

     styles = [democratic, autocratic]

     for style in styles:
         print(f"Style: {style.name}, Description: {style.description}")