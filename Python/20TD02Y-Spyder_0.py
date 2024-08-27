python
import paramiko
import logging
import getpass
from tabulate import tabulate

# Konfigurasjon
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- CISCO IOS FUNKSJONER (CCNA) ---
def ssh_connect(hostname, username, password, port=22):
    """Oppretter SSH-tilkobling til en Cisco-enhet."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)
    return client

def run_ios_command(client, command):
    """Kjører en kommando på en Cisco-enhet via SSH og returnerer output."""
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    error = stderr.read().decode()
    if error:
        logger.error(f"Feil ved kjøring av kommando: {error}")
        raise Exception(f"Feil ved kjøring av kommando: {error}")
    return output

def configure_interface(client, interface, ip_address, subnet_mask):
    """Konfigurerer en grensesnitt på en Cisco-router eller switch."""
    commands = [
        f"interface {interface}",
        f"ip address {ip_address} {subnet_mask}",
        "no shutdown",
        "exit"
    ]
    for cmd in commands:
        run_ios_command(client, cmd)
    logger.info(f"Grensesnitt {interface} konfigurert med IP {ip_address}/{subnet_mask}")

def configure_vlan(client, vlan_id, vlan_name):
    """Konfigurerer et VLAN på en Cisco-switch."""
    commands = [
        f"vlan {vlan_id}",
        f"name {vlan_name}",
        "exit"
    ]
    for cmd in commands:
        run_ios_command(client, cmd)
    logger.info(f"VLAN {vlan_id} med navn {vlan_name} konfigurert")

# --- ITIL 4 KONSEPTER OG IMPLEMENTASJON ---
def itil_service_value_system():
    """Beskriver ITIL Service Value System."""
    svs = {
        "Guiding Principles": "Recommendations that guide an organization in all circumstances.",
        "Governance": "The means by which an organization is directed and controlled.",
        "Service Value Chain": "An operating model for the creation, delivery, and continual improvement of services.",
        "Continual Improvement": "A recurring organizational activity performed at all levels to ensure that an organization's performance continually meets stakeholders' expectations.",
        "Practices": "Sets of organizational resources designed for performing work or accomplishing an objective."
    }
    print("ITIL Service Value System:")
    print(tabulate(svs.items(), headers=["Component", "Description"]))

def itil_four_dimensions():
    """Beskriver de fire dimensjonene av ITIL 4."""
    dimensions = {
        "Organizations and People": "Ensures that the way an organization is structured and managed as well as its roles, responsibilities, and systems of authority and communication is well-defined and supports its overall strategy and operating model.",
        "Information and Technology": "Includes the information and knowledge necessary for the management of services, as well as the technologies required.",
        "Partners and Suppliers": "Encompasses the relationships an organization has with other organizations that are involved in the design, development, deployment, delivery, support, and/or continual improvement of services.",
        "Value Streams and Processes": "Defines the activities, workflows, controls, and procedures needed to achieve agreed objectives."
    }
    print("The Four Dimensions of ITIL 4:")
    print(tabulate(dimensions.items(), headers=["Dimension", "Description"]))

# --- HOVEDPROGRAM ---
def main():
    logger.info("Starter CCNA og ITIL 4 eksempler...")

    # CCNA Eksempler
    hostname = input("Skriv inn Cisco-enhetens IP-adresse: ")
    username = input("Skriv inn brukernavn: ")
    password = getpass.getpass("Skriv inn passord: ")
    client = ssh_connect(hostname, username, password)

    # Konfigurer grensesnitt
    configure_interface(client, 'GigabitEthernet0/1', '192.168.1.1', '255.255.255.0')

    # Konfigurer VLAN
    configure_vlan(client, vlan_id=10, vlan_name='Management')

    client.close()

    # ITIL 4 Eksempler
    itil_service_value_system()
    itil_four_dimensions()

    logger.info("CCNA og ITIL 4 eksempler fullført.")

if __name__ == "__main__":
    main()