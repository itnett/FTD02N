python
  import datetime

  oppgaver = [
      {"navn": "Planlegging", "start": "2024-01-01", "slutt": "2024-01-05"},
      {"navn": "Gjennomføring", "start": "2024-01-06", "slutt": "2024-02-01"},
  ]

  def lag_gantt_diagram(oppgaver):
      for oppgave in oppgaver:
          start = datetime.datetime.strptime(oppgave["start"], "%Y-%m-%d")
          slutt = datetime.datetime.strptime(oppgave["slutt"], "%Y-%m-%d")
          print(f"{oppgave['navn']}: {'-' * (slutt - start).days}")

  lag_gantt_diagram(oppgaver)