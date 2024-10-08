python
     # test_oop_med_biblioteker.py
     from oop_med_biblioteker import DataAnalyzer

     def test_mean():
         data = [1, 2, 3, 4, 5]
         analyzer = DataAnalyzer(data)
         assert analyzer.mean() == 3

     def test_median():
         data = [1, 2, 3, 4, 5]
         analyzer = DataAnalyzer(data)
         assert analyzer.median() == 3

     def test_std_dev():
         data = [1, 2, 3, 4, 5]
         analyzer = DataAnalyzer(data)
         assert analyzer.std_dev() == np.std(data)