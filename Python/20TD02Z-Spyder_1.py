python
import json
import logging
import datetime
from datetime import timedelta
from collections import namedtuple
from pprint import pprint

# Sett opp logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- DATAMODELLER FOR PROSJEKT, OPPGAVE OG RESSURS ---
Project = namedtuple('Project', ['name', 'status', 'start_date', 'end_date', 'tasks', 'team', 'risks', 'issues'])
Task = namedtuple('Task', ['name', 'duration', 'resources', 'status', 'dependencies'])
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
        risks=specification.get('risks', []),  # Valgfritt felt
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
    if dependencies is None:
        dependencies = []
    task = Task(name, duration, resources, 'Ikke startet', dependencies)
    project.tasks.append(task)
    logger.info(f"Oppgave '{name}' lagt til i prosjektet '{project.name}'.")

# --- PLANLEGGING (inkludert Gantt-diagram) ---
def calculate_project_schedule(project):
    """Beregner tidsplanen for prosjektet (forenklet)."""
    end_date = project.start_date
    for task in project.tasks:
        start_date = end_date if not task.dependencies else max(calculate_task_end_date(project, dep) for dep in task.dependencies)
        end_date = start_date + timedelta(days=task.duration)
        logger.info(f"Oppgave '{task.name}': {start_date} - {end_date}")  # Gantt-info
    project._replace(end_date=end_date)

def calculate_task_end_date(project, task_name):
    """Hjelpefunksjon for å finne sluttdatoen til en oppgave."""
    for task in project.tasks:
        if task.name == task_name:
            return project.start_date + timedelta(days=task.duration)

# --- RISIKOSTYRING ---
def assess_risk(project, risk_description, impact, probability):
    """Vurderer og legger til en risiko i prosjektet."""
    project.risks.append({'beskrivelse': risk_description, 'konsekvens': impact, 'sannsynlighet': probability})

# --- DOKUMENTASJON OG RAPPORTERING ---
def generate_project_report(project):
    """Genererer en rapport for prosjektet."""
    pprint(project._asdict())  # En enkel måte å vise prosjektinformasjon på

# --- HOVEDFUNKSJON ---
def run_project_management_examples():
    # (Resten av hovedfunksjonen er lik, men bruker de nye funksjonene og datamodellene)
    pass 

if __name__ == "__main__":
    run_project_management_examples()