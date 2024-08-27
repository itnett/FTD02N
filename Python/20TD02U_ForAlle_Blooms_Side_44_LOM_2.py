python
  import matplotlib.pyplot as plt

  budsjett = [100000, 120000, 130000]
  faktisk = [95000, 115000, 135000]

  plt.plot(budsjett, label='Budsjett')
  plt.plot(faktisk, label='Faktisk')
  plt.legend()
  plt.title('Økonomisk Avviksanalyse')
  plt.show()