python
   import cProfile

   def slow_function():
       for _ in range(1000000):
           pass

   cProfile.run('slow_function()')