python
from datetime import datetime, timedelta

def generer_prosjektplan(start_dato, varighet_dager, oppgaver):
    start = datetime.strptime(start_dato, "%Y-%m-%d")
    plan = []
    for index, oppgave in enumerate(oppgaver):
        sluttdato = start + timedelta(days=varighet_dager[index])
        plan.append(f"Oppgave {index+1}: {oppgave}, Start: {start.date()}, Slutt: {sluttdato.date()}")
        start = sluttdato + timedelta(days=1)
    return "\n".join(plan)

start_dato = "2024-09-01"
varighet_dager = [5, 10, 7, 3]
oppgaver = ["Planlegging", "Design", "Utvikling", "Testing"]

print(generer_prosjektplan(start_dato, varighet_dager, oppgaver))