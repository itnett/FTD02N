python
   import time
   
   array = list(np.random.randint(0, 1000000, size=1000000))
   start_time = time.time()
   array.sort()
   print("Built-in sort time:", time.time() - start_time)