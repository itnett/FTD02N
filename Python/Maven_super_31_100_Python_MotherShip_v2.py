python
# Del 1: Grunnleggende og Filhåndtering

# Importer nødvendige moduler
import os  # Modul for filsystemoperasjoner
import logging  # For logging av hendelser og feil
import re  # For regulære uttrykk (mønstermatching)
from functools import reduce  # For reduce-funksjonen

# Konfigurer logging
logging.basicConfig(filename='log_analyzer.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Del 2: Funksjoner og Datastrukturer

def read_log_file(filename):
    """Leser en loggfil og returnerer innholdet som en liste av linjer.

    Args:
        filename (str): Navnet på loggfilen som skal leses.

    Returns:
        list: En liste der hvert element er en linje fra loggfilen.
              Returnerer en tom liste hvis filen ikke finnes.
    """
    try:
        with open(filename, 'r') as f:  # Åpner filen i lese-modus ('r')
            log_lines = f.readlines()  # Leser alle linjene og lagrer dem i en liste
        return log_lines
    except FileNotFoundError:  # Håndterer tilfelle der filen ikke finnes
        logging.error(f"Filen {filename} ble ikke funnet.")
        return []

def search_for_pattern(pattern, log_lines):
    """Søker etter et mønster i loggfilen og returnerer treff.

    Args:
        pattern (str): Mønsteret som skal søkes etter (kan være et regulært uttrykk).
        log_lines (list): En liste av linjer fra loggfilen.

    Returns:
        list: En liste av linjer som matcher mønsteret.
    """
    matches = []
    for line in log_lines:  # Går gjennom hver linje i loggfilen
        if re.search(pattern, line):  # Søker etter mønsteret i linjen
            matches.append(line)  # Legger til linjen i trefflisten hvis den matcher
    return matches

def count_occurrences(pattern, log_lines):
    """Teller antall forekomster av et mønster i loggfilen.

    Args:
        pattern (str): Mønsteret som skal telles.
        log_lines (list): En liste av linjer fra loggfilen.

    Returns:
        int: Antall ganger mønsteret forekommer i loggfilen.
    """
    return len(search_for_pattern(pattern, log_lines))  # Bruker len() for å telle treff

# Del 3: Brukerinteraksjon og Kontrollstrukturer

def get_user_choice():
    """Viser en meny og får brukerens valg.

    Returns:
        str: Brukerens valg (en streng).
    """
    print("\nVelg en handling:")
    print("1. Søk etter mønster")
    print("2. Tell forekomster av mønster")
    print("3. Analyser IP-adresser") # Ny funksjon for å demonstrere flere konsepter
    print("4. Avslutt")
    return input("Ditt valg: ")

def analyze_ip_addresses(log_lines):
    """Analyserer IP-adresser i loggfilen.

    Args:
        log_lines (list): En liste av linjer fra loggfilen.
    """
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  # Mønster for å finne IP-adresser

    # Bruker list comprehension for å finne alle IP-adresser
    ip_addresses = [re.search(ip_pattern, line).group() for line in log_lines if re.search(ip_pattern, line)]

    if not ip_addresses:
        print("Ingen IP-adresser funnet.")
        return

    # Fjerner duplikater ved å konvertere til mengde og tilbake til liste
    unique_ips = list(set(ip_addresses))

    # Sorterer IP-adressene
    sorted_ips = sorted(unique_ips)

    # Bruker enumerate for å få både indeks og verdi
    for index, ip in enumerate(sorted_ips):
        print(f"{index + 1}. {ip}")

    # Bruker map for å konvertere til heltall og deretter reduce for å finne summen
    ip_sums = reduce(lambda x, y: x + y, map(lambda ip: sum(map(int, ip.split('.'))), sorted_ips))

    # Bruker any og all for å sjekke betingelser
    has_private_ip = any(ip.startswith('192.168.') or ip.startswith('10.') for ip in sorted_ips)
    all_valid_ips = all(all(0 <= int(octet) <= 255 for octet in ip.split('.')) for ip in sorted_ips)

    print(f"\nAntall unike IP-adresser: {len(unique_ips)}")
    print(f"Summen av alle IP-adresser (som heltall): {ip_sums}")
    print(f"Inneholder private IP-adresser: {has_private_ip}")
    print(f"Alle IP-adresser er gyldige: {all_valid_ips}")

def main():
    """Hovedfunksjonen som kjører programmet."""
    log_file = input("Skriv inn navnet på loggfilen: ")
    log_lines = read_log_file(log_file)

    if not log_lines:  # Sjekk om filen ble lest riktig
        return

    while True:  # Hovedløkke som kjører til brukeren velger å avslutte
        choice = get_user_choice()

        if choice == '1':
            pattern = input("Skriv inn mønsteret du vil søke etter: ")
            matches = search_for_pattern(pattern, log_lines)
            if matches:
                print("Treff:")
                for match in matches:
                    print(match.strip()) 
            else:
                print("Ingen treff funnet.")
        elif choice == '2':
            pattern = input("Skriv inn mønsteret du vil telle: ")
            count = count_occurrences(pattern, log_lines)
            print(f"Antall forekomster: {count}")
        elif choice == '3':
            analyze_ip_addresses(log_lines)
        elif choice == '4':
            break  # Avslutter løkken og programmet
        else:
            print("Ugyldig valg.")

# Sjekker om skriptet kjøres direkte (ikke importert som modul)
if __name__ == "__main__":
    main()  # Kjører hovedfunksjonen hvis skriptet kjøres direkte