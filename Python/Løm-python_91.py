python
     class MarketSegment:
         def __init__(self, name, characteristics):
             self.name = name
             self.characteristics = characteristics

     segment = MarketSegment('Young Professionals', ['Age 25-35', 'High Income', 'Urban'])
     print(f"Segment: {segment.name}, Characteristics: {', '.join(segment.characteristics)}")