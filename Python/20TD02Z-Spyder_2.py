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
    return project

def calculate_task_end_date(project, task_name):
    """Hjelpefunksjon for å finne sluttdatoen til en oppgave."""
    for task in project.tasks:
        if task.name == task_name:
            return project.start_date + timedelta(days=task.duration)

def generate_gantt_chart(project):
    """Genererer et Gantt-diagram for prosjektet."""
    fig, ax = plt.subplots()

    for i, task in enumerate(project.tasks):
        start_date = project.start_date + timedelta(days=sum(dep.duration for dep in project.tasks if dep.name in task.dependencies))
        end_date = start_date + timedelta(days=task.duration)
        ax.barh(task.name, (end_date - start_date).days, left=start_date, align='center')
        ax.text(start_date + (end_date - start_date) / 2, i, task.name, ha='center', va='center', color='white', fontsize=10)

    ax.set_xlabel('Dato')
    ax.set_ylabel('Oppgave')
    ax.set_title(f'Gantt-diagram for prosjektet: {project.name}')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()
    plt.show()

# --- RISIKOSTYRING ---
def assess_risk(project, risk_description, impact, probability):
    """Vurderer og legger til en risiko i prosjektet."""
    project.risks.append({'beskrivelse': risk_description, 'konsekvens': impact, 'sannsynlighet': probability})
    logger.info(f"Risiko vurdert og lagt til: {risk_description}, Konsekvens: {impact}, Sannsynlighet: {probability}")

# --- DOKUMENTASJON OG RAPPORTERING ---
def generate_project_report(project):
    """Genererer en rapport for prosjektet."""
    report = project._asdict()
    pprint(report)  # En enkel måte å vise prosjektinformasjon på
    return report

def save_report_to_file(report, filename):
    """Lagrer prosjektets rapport til en fil."""
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    logger.info(f"Prosjektrapport lagret til filen '{filename}'.")

# --- HOVEDFUNKSJON ---
def run_project_management_examples():
    logger.info("Starter eksempler på prosjektledelse...")

    # Opprette kravspesifikasjon
    specification = create_requirement_specification(
        project_name='Ny nettside',
        stakeholders=['Kunde', 'Prosjektleder', 'Utviklingsteam'],
        objectives=['Øke online tilstedeværelse', 'Forbedre brukeropplevelse'],
        scope='Utvikle en ny nettside med moderne design og funksjonaliteter',
        deliverables=['Design mockups', 'Utviklet nettside', 'Testresultater'],
        milestones=[
            {'name': 'Design ferdigstilt', 'due_date': '2024-07-01'},
            {'name': 'Utvikling ferdigstilt', 'due_date': '2024-09-01'},
            {'name': 'Lansering', 'due_date': '2024-10-01'}
        ]
    )
    save_specification_to_file(specification, 'requirement_specification.json')

    # Initiere prosjekt
    project = initiate_project(specification)

    # Tilordne ressurser
    add_resource(project, 'Alice', 'Designer', availability=0.8)
    add_resource(project, 'Bob', 'Utvikler', availability=1.0)
    add_resource(project, 'Charlie', 'Tester', availability=0.5)

    # Legge til oppgaver
    add_task(project, 'Design fase', 30, ['Alice'])
    add_task(project, 'Utviklingsfase', 60, ['Bob'])
    add_task(project, 'Testfase', 15, ['Charlie'], dependencies=['Utviklingsfase'])

    # Beregne tidsplan
    project = calculate_project_schedule(project)

    # Vurdere risikoer
    assess_risk(project, 'Forsinkelser i designfasen', 'Høy', 'Middels')
    assess_risk(project, 'Tekniske problemer under utvikling', 'Middels', 'Høy')

    # Generere og lagre prosjektrapport
    report = generate_project_report(project)
    save_report_to_file(report, 'project_report.json')

    # Generere Gantt-diagram
    generate_gantt_chart(project)

    logger.info("Eksempler på prosjektledelse fullført.")

if __name__ == "__main__":
    run_project_management_examples()