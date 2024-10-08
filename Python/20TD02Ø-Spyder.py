python
import subprocess
import os
import json
import docker
import logging
import matplotlib.pyplot as plt

# Sett opp logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- SYSTEMDRIFT OG LINUX DISTRIBUSJONER ---
def check_linux_distribution():
    """Sjekker hvilken Linux-distribusjon som er installert."""
    try:
        result = subprocess.run(['lsb_release', '-a'], capture_output=True, text=True)
        logger.info(f"Linux Distribution:\n{result.stdout}")
    except FileNotFoundError:
        logger.error("lsb_release kommando ikke funnet. Er dette et Linux-system?")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")

# --- BRUKERADMINISTRASJON OG INSTALLASJON ---
def create_user(username):
    """Oppretter en ny bruker."""
    try:
        subprocess.run(['sudo', 'useradd', username], check=True)
        logger.info(f"Brukeren {username} ble opprettet.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved oppretting av bruker: {e}")
    except PermissionError:
        logger.error("Du har ikke tillatelse til å opprette brukere. Kjør skriptet med sudo.")

# --- NETTVERK OG PROSESSER ---
def list_network_interfaces():
    """Lister alle nettverksgrensesnitt."""
    try:
        result = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
        logger.info(f"Nettverksgrensesnitt:\n{result.stdout}")
    except FileNotFoundError:
        logger.error("ip kommando ikke funnet. Er dette et Linux-system?")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")

def list_processes():
    """Lister alle kjørende prosesser."""
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        logger.info(f"Prosesser:\n{result.stdout}")
    except FileNotFoundError:
        logger.error("ps kommando ikke funnet. Er dette et Linux-system?")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")

# --- TERMINAL OG PAKKESYSTEMER ---
def install_package(package_name):
    """Installerer en pakke og håndterer ulike feil."""
    try:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package_name], check=True)
        logger.info(f"Pakken {package_name} ble installert.")
    except subprocess.CalledProcessError as e:
        if e.returncode == 100:  # Pakken finnes ikke
            logger.error(f"Pakken {package_name} ble ikke funnet.")
        else:
            logger.error(f"Feil ved installasjon av pakke: {e}")
    except PermissionError:
        logger.error("Du har ikke tillatelse til å installere pakker. Kjør skriptet med sudo.")

# --- LAGRING OG FILSYSTEMER ---
def list_filesystem():
    """Lister filsystemet."""
    try:
        result = subprocess.run(['df', '-h'], capture_output=True, text=True)
        logger.info(f"Filsystem:\n{result.stdout}")
    except FileNotFoundError:
        logger.error("df kommando ikke funnet. Er dette et Linux-system?")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")

# --- CONTAINERE OG AUTOMATISERING ---
def run_docker_container(image_name):
    """Kjører en Docker-container."""
    client = docker.from_env()
    try:
        container = client.containers.run(image_name, detach=True)
        logger.info(f"Docker Container {container.short_id} kjører med bilde {image_name}")
        return container
    except docker.errors.ImageNotFound:
        logger.error(f"Bildet {image_name} ikke funnet.")
    except docker.errors.APIError as e:
        logger.error(f"Docker API-feil: {e}")

def list_docker_containers():
    """Lister alle kjørende Docker-containere."""
    client = docker.from_env()
    try:
        containers = client.containers.list()
        for container in containers:
            logger.info(f"Container {container.short_id} kjører med bilde {container.image.tags}")
    except docker.errors.APIError as e:
        logger.error(f"Docker API-feil: {e}")

# --- SIMULERING AV ULIKE DISTRIBUSJONER ---
def simulate_distribution(distro_name):
    """Simulerer ulike Linux-distribusjoner ved hjelp av Docker."""
    client = docker.from_env()
    try:
        container = client.containers.run(f"{distro_name}:latest", command="/bin/bash", detach=True, tty=True)
        logger.info(f"Docker Container {container.short_id} kjører {distro_name}")
        # Kjør kommandoer inne i containeren for å demonstrere forskjeller
        exec_result = client.containers.get(container.short_id).exec_run("lsb_release -a")
        logger.info(f"Distribusjon detaljer:\n{exec_result.output.decode()}")
        container.stop()
    except docker.errors.ImageNotFound:
        logger.error(f"Bildet {distro_name} ikke funnet.")
    except docker.errors.APIError as e:
        logger.error(f"Docker API-feil: {e}")

# --- INTERAKTIVE ELEMENTER ---
def interactive_menu():
    """Interaktiv meny for å velge kommandoer å kjøre."""
    options = {
        '1': ('Sjekk Linux-distribusjon', check_linux_distribution),
        '2': ('Opprett bruker', lambda: create_user('testuser')),
        '3': ('List nettverksgrensesnitt', list_network_interfaces),
        '4': ('List prosesser', list_processes),
        '5': ('Installer pakke', lambda: install_package('htop')),
        '6': ('List filsystem', list_filesystem),
        '7': ('Kjør Docker container', lambda: run_docker_container('hello-world')),
        '8': ('List Docker containere', list_docker_containers),
        '9': ('Simuler distribusjon', lambda: simulate_distribution('ubuntu'))
    }

    while True:
        print("\nInteraktiv meny:")
        for key, (desc, _) in options.items():
            print(f"{key}: {desc}")
        choice = input("Velg et alternativ (eller 'q' for å avslutte): ")
        if choice == 'q':
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Ugyldig valg. Prøv igjen.")

# --- VISUALISERING AV SYSTEMINFORMASJON ---
def visualize_disk_usage():
    """Visualiserer diskbruk ved hjelp av matplotlib."""
    try:
        result = subprocess.run(['df', '-h'], capture_output=True, text=True)
        lines = result.stdout.split('\n')[1:-1]
        partitions, sizes, used = [], [], []
        for line in lines:
            parts = line.split()
            partitions.append(parts[0])
            sizes.append(int(parts[1][:-1]))
            used.append(int(parts[2][:-1]))

        plt.bar(partitions, used, label='Brukt')
        plt.bar(partitions, sizes, bottom=used, label='Total', alpha=0.5)
        plt.xlabel('Partisjon')
        plt.ylabel('Størrelse (GB)')
        plt.title('Diskbruk')
        plt.legend()
        plt.show()
    except FileNotFoundError:
        logger.error("df kommando ikke funnet. Er dette et Linux-system?")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_linux_and_container_examples():
    logger.info("Starter eksempler på Linux og containere...")
    interactive_menu()
    visualize_disk_usage()
    logger.info("Eksempler på Linux og containere fullført.")

if __name__ == "__main__":
    run_linux_and_container_examples()