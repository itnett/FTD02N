python
import pandas as pd
from datetime import datetime, timedelta

def create_project_plan(tasks, start_date="2024-07-01"):
    """
    Lag en prosjektplan med tidsfrister.

    Parametere:
    tasks (list): Liste over oppgaver
    start_date (str): Startdato for prosjektet (standardverdi "2024-07-01")

    Returnerer:
    pd.DataFrame: Prosjektplan
    """
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    plan = []
    for i, task in enumerate(tasks):
        end_date = start_date + timedelta(days=7 * (i + 1))  # Hver oppgave tar en uke
        plan.append({"Task": task, "Start Date": start_date.strftime("%Y-%m-%d"), "End Date": end_date.strftime("%Y-%m-%d")})
        start_date = end_date + timedelta(days=1)
    
    df_plan = pd.DataFrame(plan)
    return df_plan

# Eksempel på bruk
tasks = ["Analyze requirements", "Design system architecture", "Develop components", "Integrate and test", "Deploy system"]
project_plan = create_project_plan(tasks)
print(project_plan)