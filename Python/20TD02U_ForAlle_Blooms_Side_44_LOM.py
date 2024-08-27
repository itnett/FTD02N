python
  strategier = {
      "Sosiale Medier": {"Mål": 10000, "Resultat": 12000},
      "Epostmarkedsføring": {"Mål": 5000, "Resultat": 4500},
  }

  def visualiser_strategi(strategier):
      for strategi, data i strategier.items():
          plt.bar(strategi, data["Resultat"], label=f'Resultat: {data["Resultat"]} (Mål: {data["Mål"]})')
      plt.title('Strategisk Måloppnåelse')
      plt.legend()
      plt.show()

  visualiser_strategi(strategier)