python
import json
import logging
import datetime
from datetime import timedelta
from collections import namedtuple
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Sett opp logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- DATAMODELLER ---
Project = namedtuple('Project', ['name', 'status', 'start_date', 'end_date', 'tasks', 'team', 'risks', 'issues'])
Task = namedtuple('Task', ['name', 'duration', 'resources', 'status', 'dependencies', 'start_date', 'end_date'])
Resource = namedtuple('Resource', ['name', 'role', 'availability'])

# --- KRAVSPESIFIKASJON OG INITIERING ---
def create_requirement_specification(**kwargs):
    """Oppretter en kravspesifikasjon for et prosjekt (bruker kwargs for fleksibilitet)."""
    logger.info(f"Kravspesifikasjon for prosjektet '{kwargs['project_name']}' opprettet.")
    return kwargs

def initiate_project(specification):
    """Initierer et prosjekt basert på kravspesifikasjonen."""
    project = Project(
        name=specification['project_name'],
        status='Initiert',
        start_date=datetime.date.today(),
        end_date=None,  # Beregnes senere basert på oppgaver
        tasks=[],
        team=[],
        risks=specification.get('risks', []),
        issues=[]
    )
    logger.info(f"Prosjekt '{project.name}' initiert.")
    return project

# --- RESSURSSTYRING ---
def add_resource(project, name, role, availability=1.0):
    """Legger til en ressurs til prosjektet."""
    resource = Resource(name, role, availability)
    project.team.append(resource)
    logger.info(f"Ressurs '{name}' lagt til prosjektet '{project.name}'.")

def add_task(project, name, duration, resources, dependencies=None):
    """Legger til en oppgave i prosjektet."""
    task = Task(name, duration, resources, 'Ikke startet', dependencies or [], None, None)  # Initialiser start- og sluttdato til None
    project.tasks.append(task)
    logger.info(f"Oppgave '{name}' lagt til i prosjektet '{project.name}'.")

# --- PLANLEGGING (inkludert Gantt-diagram) ---
def calculate_project_schedule(project):
    """Beregner tidsplanen for prosjektet og oppdaterer start- og sluttdatoer for oppgaver."""
    end_date = project.start_date
    for task in project.tasks:
        start_date = end_date if not task.dependencies else max(t.end_date for t in project.tasks if t.name in task.dependencies)
        end_date = start_date + timedelta(days=task.duration)
        task = task._replace(start_date=start_date, end_date=end_date)
        logger.info(f"Oppgave '{task.name}': {start_date} - {end_date}")
    return project._replace(end_date=end_date)

def generate_gantt_chart(project):
    """Genererer et Gantt-diagram for prosjektet."""
    fig, ax = plt.subplots(figsize=(12, 6))  # Juster størrelsen for bedre lesbarhet

    for i, task in enumerate(project.tasks):
        ax.barh(task.name, (task.end_date - task.start_date).days, left=task.start_date, align='center')
        ax.text(task.start_date + (task.end_date - task.start_date) / 2, i, task.name, ha='center', va='center', color='white')

    ax.set_xlabel('Dato')
    ax.set_ylabel('Oppgave')
    ax.set_title(f'Gantt-diagram for prosjektet: {project.name}')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))  # Vis ukedager på x-aksen
    plt.xticks(rotation=45)
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

# --- RISIKOSTYRING ---
# (Samme som før)

# --- DOKUMENTASJON OG RAPPORTERING ---
# (Samme som før)

# --- HOVEDFUNKSJON ---
# (Samme som før, men husk å kalle calculate_project_schedule før du genererer Gantt-diagrammet)