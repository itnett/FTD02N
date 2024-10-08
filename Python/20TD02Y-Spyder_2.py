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
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        return client
    except Exception as e:
        logger.error(f"Feil ved SSH-tilkobling: {e}")
        return None  # Return None for å indikere mislykket tilkobling

def run_ios_command(client, command):
    """Kjører en kommando på en Cisco-enhet via SSH og returnerer output."""
    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        if error:
            logger.error(f"Feil ved kjøring av kommando: {error}")
        return output
    except Exception as e:
        logger.error(f"Feil ved kjøring av kommando: {e}")
        return None  # Return None for å indikere mislykket kommando

# ... (Resten av funksjonene for konfigurasjon av grensesnitt og VLAN er de samme) ...

# --- ITIL 4 KONSEPTER OG IMPLEMENTASJON ---
# ... (Funksjonene for ITIL Service Value System og Four Dimensions er de samme) ...

# --- HOVEDPROGRAM ---
def main():
    logger.info("Starter CCNA og ITIL 4 eksempler...")

    # CCNA Eksempler
    hostname = input("Skriv inn Cisco-enhetens IP-adresse eller vertsnavn: ")
    username = input("Skriv inn brukernavn: ")
    password = getpass.getpass("Skriv inn passord: ")
    client = ssh_connect(hostname, username, password)

    if client:  # Sjekk om SSH-tilkoblingen var vellykket
        # Konfigurer grensesnitt
        configure_interface(client, 'GigabitEthernet0/1', '192.168.1.1', '255.255.255.0')

        # Konfigurer VLAN
        configure_vlan(client, vlan_id=10, vlan_name='Management')

        client.close()
    else:
        logger.error("Kan ikke fortsette med CCNA-eksempler på grunn av mislykket SSH-tilkobling.")

    # ITIL 4 Eksempler (kjøres uavhengig av SSH-tilkobling)
    itil_service_value_system()
    itil_four_dimensions()

    logger.info("CCNA og ITIL 4 eksempler fullført.")

if __name__ == "__main__":
    main()