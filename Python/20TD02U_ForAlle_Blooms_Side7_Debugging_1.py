python
   import pdb

   def addisjon(a, b):
       pdb.set_trace()  # Start en debugger her
       return a + b

   resultat = addisjon(5, 3)
   print(resultat)