python
   import objgraph

   def leaky_function():
       global _leaky_list
       _leaky_list = []
       for _ in range(10000):
           _leaky_list.append(object())

   leaky_function()
   objgraph.show_most_common_types()