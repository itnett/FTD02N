python
   import numpy as np
   import time
   
   array = np.random.randint(0, 1000000, size=1000000)
   start_time = time.time()
   np.sort(array)
   print("NumPy sort time:", time.time() - start_time)