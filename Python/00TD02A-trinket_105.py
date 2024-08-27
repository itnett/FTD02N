python
   import numpy as np

   angle = 30
   opposite = 5
   adjacent = opposite / np.tan(np.radians(angle))
   print(f"For en vinkel på 30 grader og motstående side på 5, er tilstøtende side: {adjacent}")