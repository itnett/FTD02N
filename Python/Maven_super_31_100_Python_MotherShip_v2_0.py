python
# Del 1: Grunnleggende og Filhåndtering
import os  # Modul for filsystemoperasjoner
import logging  # For logging av hendelser og feil
import re  # For regulære uttrykk (mønstermatching)

# Konfigurer logging
logging.basicConfig(filename='log_analyzer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Del 2: Funksjoner og Datastrukturer
def read_log_file(filename):
    """Leser en loggfil og returnerer innholdet som en liste av linjer."""
    try:
        with open(filename, 'r') as f:
            log_lines = f.readlines()
        return log_lines
    except FileNotFoundError:
        logging.error(f"Filen {filename} ble ikke funnet.")
        return []  # Returner en tom liste hvis filen ikke finnes

def search_for_pattern(pattern, log_lines):
    """Søker etter et mønster i loggfilen og returnerer treff."""
    matches = []
    for line in log_lines:
        if re.search(pattern, line):
            matches.append(line)
    return matches

def count_occurrences(pattern, log_lines):
    """Teller antall forekomster av et mønster i loggfilen."""
    return len(search_for_pattern(pattern, log_lines))

# Del 3: Brukerinteraksjon og Kontrollstrukturer
def main():
    """Hovedfunksjonen som kjører programmet."""
    log_file = input("Skriv inn navnet på loggfilen: ")
    log_lines = read_log_file(log_file)

    if not log_lines:  # Sjekk om filen ble lest riktig
        return

    while True:
        print("\nVelg en handling:")
        print("1. Søk etter mønster")
        print("2. Tell forekomster av mønster")
        print("3. Avslutt")

        choice = input("Ditt valg: ")

        if choice == '1':
            pattern = input("Skriv inn mønsteret du vil søke etter: ")
            matches = search_for_pattern(pattern, log_lines)
            if matches:
                print("Treff:")
                for match in matches:
                    print(match.strip())  # Fjern whitespace før utskrift
            else:
                print("Ingen treff funnet.")
        elif choice == '2':
            pattern = input("Skriv inn mønsteret du vil telle: ")
            count = count_occurrences(pattern, log_lines)
            print(f"Antall forekomster: {count}")
        elif choice == '3':
            break
        else:
            print("Ugyldig valg.")

if __name__ == "__main__":
    main()