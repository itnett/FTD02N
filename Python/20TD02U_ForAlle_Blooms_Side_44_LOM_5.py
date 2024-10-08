python
  kandidater = [
      {"navn": "Kandidat A", "erfaring": 5, "ferdigheter": ["Python", "Ledelse"]},
      {"navn": "Kandidat B", "erfaring": 2, "ferdigheter": ["Java"]},
  ]

  def screen_kandidater(kandidater, krav):
      kvalifiserte = [k for k in kandidater if all(f in k["ferdigheter"] for f in krav)]
      return kvalifiserte

  krav = ["Python", "Ledelse"]
  kvalifiserte = screen_kandidater(kandidater, krav)
  print(f"Kvalifiserte kandidater: {', '.join([k['navn'] for k in kvalifiserte])}")