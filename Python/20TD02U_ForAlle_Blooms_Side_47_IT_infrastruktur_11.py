python
      def evaluate_scalability(num_devices):
          if num_devices <= 100:
              return "Small Scale"
          elif num_devices <= 1000:
              return "Medium Scale"
          else:
              return "Large Scale"

      devices = 500
      print(f"Scale: {evaluate_scalability(devices)}")