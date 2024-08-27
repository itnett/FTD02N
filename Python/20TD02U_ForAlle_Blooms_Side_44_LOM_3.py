python
  kompetanse = {
      "Ansatt A": {"Python": 3, "Ledelse": 4},
      "Ansatt B": {"Python": 5, "Ledelse": 2},
  }

  def generer_utviklingsplan(kompetanse):
      for ansatt, ferdigheter in kompetanse.items():
          for ferdighet, nivå in ferdigheter.items():
              if nivå < 4:
                  print(f"{ansatt} bør utvikle ferdigheten: {ferdighet}")

  generer_utviklingsplan(kompetanse)