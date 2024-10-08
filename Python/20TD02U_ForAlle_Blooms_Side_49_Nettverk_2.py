python
class OSIModel:
    def __init__(self):
        self.layers = ["Physical", "Data Link", "Network", "Transport", "Session", "Presentation", "Application"]

    def transmit(self, data):
        print("Transmitting through OSI layers...")
        for layer in reversed(self.layers):
            data = f"{layer} Layer encapsulates data: {data}"
            print(data)
        return data

osi_model = OSIModel()
osi_model.transmit("Hello, World!")