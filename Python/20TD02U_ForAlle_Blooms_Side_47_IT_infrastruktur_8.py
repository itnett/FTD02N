python
      import numpy as np

      sensor1 = np.array([22.5, 22.7, 22.4, 22.6])
      sensor2 = np.array([22.4, 22.6, 22.5, 22.7])
      diff = sensor1 - sensor2
      print(f"Mean difference: {np.mean(diff)}")