python
   import numpy as np

   # Definere et datasett
   data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   # Beregne gjennomsnitt, median og standardavvik
   mean = np.mean(data)
   median = np.median(data)
   std_dev = np.std(data)
   print(f"Gjennomsnitt: {mean}, Median: {median}, Standardavvik: {std_dev}")