python
  kampanjer = [
      {"navn": "Sommerkampanje", "målgruppe": "Segment A", "budsjett": 10000},
      {"navn": "Vinterkampanje", "målgruppe": "Segment B", "budsjett": 20000},
  ]

  def kjør_kampanje(kampanje):
      print(f"Kjører kampanje: {kampanje['navn']} for målgruppe {kampanje['målgruppe']} med budsjett {kampanje['budsjett']}")

  for kampanje in kampanjer:
      kjør_kampanje(kampanje)