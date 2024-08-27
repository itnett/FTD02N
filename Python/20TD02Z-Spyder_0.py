python
import json
import logging
import datetime

# Sett opp logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- KRAVSPESIFIKASJON ---
def create_requirement_specification(project_name, stakeholders, objectives, scope, deliverables, milestones):
    """Oppretter en kravspesifikasjon for et prosjekt."""
    specification = {
        'project_name': project_name,
        'stakeholders': stakeholders,
        'objectives': objectives,
        'scope': scope,
        'deliverables': deliverables,
        'milestones': milestones
    }
    logger.info(f"Kravspesifikasjon for prosjektet '{project_name}' opprettet.")
    return specification

def save_specification_to_file(specification, filename):
    """Lagrer kravspesifikasjonen til en fil."""
    with open(filename, 'w') as f:
        json.dump(specification, f, indent=4)
    logger.info(f"Kravspesifikasjon lagret til filen '{filename}'.")

# --- INITIERING OG PLANLEGGING ---
def initiate_project(specification):
    """Initierer et prosjekt basert på kravspesifikasjonen."""
    project = {
        'name': specification['project_name'],
        'status': 'initiated',
        'start_date': datetime.date.today().isoformat(),
        'end_date': None,
        'tasks': [],
        'team': [],
        'risks': [],
        'issues': []
    }
    logger.info(f"Prosjekt '{project['name']}' initiert.")
    return project

# --- RESSURSSTYRING ---
def assign_resources(project, team_members):
    """Tildeler ressurser til prosjektet."""
    project['team'].extend(team_members)
    logger.info(f"Ressurser tildelt prosjektet '{project['name']}': {team_members}")

def add_task(project, task_name, duration, resources):
    """Legger til en oppgave i prosjektet."""
    task = {
        'name': task_name,
        'duration': duration,
        'resources': resources,
        'status': 'not started'
    }
    project['tasks'].append(task)
    logger.info(f"Oppgave '{task_name}' lagt til i prosjektet '{project['name']}'.")

# --- RISIKOVURDERING ---
def assess_risks(project, risks):
    """Legger til risikoer i prosjektet."""
    project['risks'].extend(risks)
    logger.info(f"Risikoer lagt til prosjektet '{project['name']}': {risks}")

# --- DOKUMENTASJON OG RAPPORTER ---
def generate_project_report(project):
    """Genererer en rapport for prosjektet."""
    report = {
        'project_name': project['name'],
        'status': project['status'],
        'start_date': project['start_date'],
        'end_date': project['end_date'],
        'tasks': project['tasks'],
        'team': project['team'],
        'risks': project['risks'],
        'issues': project['issues']
    }
    logger.info(f"Generert rapport for prosjektet '{project['name']}'.")
    return report

def save_report_to_file(report, filename):
    """Lagrer prosjektets rapport til en fil."""
    with open(filename, 'w') as f:
        json.dump(report, f, indent=4)
    logger.info(f"Prosjektrapport lagret til filen '{filename}'.")

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
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
    assign_resources(project, ['Alice', 'Bob', 'Charlie'])

    # Legge til oppgaver
    add_task(project, 'Design fase', 30, ['Alice'])
    add_task(project, 'Utviklingsfase', 60, ['Bob', 'Charlie'])
    add_task(project, 'Testfase', 15, ['Charlie'])

    # Vurdere risikoer
    assess_risks(project, [
        {'risk': 'Forsinkelser i designfasen', 'impact': 'High', 'probability': 'Medium'},
        {'risk': 'Tekniske problemer under utvikling', 'impact': 'Medium', 'probability': 'High'}
    ])

    # Generere og lagre prosjektrapport
    report = generate_project_report(project)
    save_report_to_file(report, 'project_report.json')

    logger.info("Eksempler på prosjektledelse fullført.")

if __name__ == "__main__":
    run_project_management_examples()