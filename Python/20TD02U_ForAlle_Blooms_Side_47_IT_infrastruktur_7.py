python
      import matplotlib.pyplot as plt

      # Simulerte sikkerhetsdata
      devices = ['Camera', 'Thermostat', 'Light', 'Router']
      vulnerabilities = [5, 3, 2, 8]

      plt.bar(devices, vulnerabilities)
      plt.xlabel('IoT Devices')
      plt.ylabel('Number of Vulnerabilities')
      plt.title('IoT Device Vulnerability Analysis')
      plt.show()