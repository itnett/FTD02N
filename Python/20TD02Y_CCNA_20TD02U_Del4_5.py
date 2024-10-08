python
     # oop_med_biblioteker.py
     import numpy as np

     class DataAnalyzer:
         def __init__(self, data):
             self.data = np.array(data)

         def mean(self):
             return np.mean(self.data)

         def median(self):
             return np.median(self.data)

         def std_dev(self):
             return np.std(self.data)

     if __name__ == "__main__":
         data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
         analyzer = DataAnalyzer(data)
         print(f"Mean: {analyzer.mean()}")
         print(f"Median: {analyzer.median()}")
         print(f"Standard Deviation: {analyzer.std_dev()}")