python
   # Trigonometri i rettvinklede trekanter
   import numpy as np

   angle = 30  # grader
   opposite = 5  # lengden av den motstående siden
   adjacent = opposite / np.tan(np.radians(angle))
   print(f"For en vinkel på {angle} grader og motstående side på {opposite}, er tilstøtende side: {adjacent}")