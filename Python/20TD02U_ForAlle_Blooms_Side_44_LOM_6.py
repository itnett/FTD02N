python
  import matplotlib.pyplot as plt

  segmenter = {
      "Segment A": {"Alder": [25, 30, 35], "Inntekt": [50000, 60000, 70000]},
      "Segment B": {"Alder": [40, 45, 50], "Inntekt": [80000, 90000, 100000]},
  }

  def visualiser_segmenter(segmenter):
      for segment, data in segmenter.items():
          plt.scatter(data["A

lder"], data["Inntekt"], label=segment)
      plt.xlabel("Alder")
      plt.ylabel("Inntekt")
      plt.legend()
      plt.show()

  visualiser_segmenter(segmenter)