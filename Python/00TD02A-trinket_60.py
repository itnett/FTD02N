python
   import numpy as np

   # Definere matrisene
   A = np.array([[2, 1], [1, -1]])
   b = np.array([10, 2])

   # Løse matriselikningen Ax = b
   x = np.linalg.solve(A, b)
   print(f"Løsning: {x}")