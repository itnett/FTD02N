python
import subprocess
import os
import json
import docker
import logging

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
    """Installerer en pakke."""
    try:
        subprocess.run(['sudo', 'apt-get', 'install', '-y', package_name], check=True)
        logger.info(f"Pakken {package_name} ble installert.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Feil ved installasjon av pakke: {e}")

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

# --- HOVEDFUNKSJON FOR Å KJØRE EKSEMPLENE ---
def run_linux_and_container_examples():
    logger.info("Starter eksempler på Linux og containere...")
    check_linux_distribution()
    create_user('testuser')
    list_network_interfaces()
    list_processes()
    install_package('htop')
    list_filesystem()
    run_docker_container('hello-world')
    list_docker_containers()
    logger.info("Eksempler på Linux og containere fullført.")

if __name__ == "__main__":
    run_linux_and_container_examples()