python
import math

# Funksjon for å utføre grunnleggende fysikk- og matematikkberegninger
def basic_physics_calculations():
    try:
        # Beregning av kraft ved hjelp av Newtons andre lov: F = ma
        mass = float(input("Oppgi masse i kg: "))
        acceleration = float(input("Oppgi akselerasjon i m/s^2: "))
        force = mass * acceleration
        print(f"Kraften er {force} N.")

        # Beregning av energi ved hjelp av kinetisk energiformel: E_k = 0.5 * m * v^2
        velocity = float(input("Oppgi hastighet i m/s: "))
        kinetic_energy = 0.5 * mass * velocity ** 2
        print(f"Kinetisk energi er {kinetic_energy} Joule.")

    except ValueError:
        print("Feil: Vennligst oppgi et gyldig tall.")

# Funksjon for å evaluere eget arbeid i henhold til matematiske og fysiske lover
def evaluate_work():
    try:
        # Bruk av dimensjonsanalyse for å verifisere en beregning
        force_calculated = float(input("Oppgi beregnet kraft i Newton: "))
        mass = float(input("Oppgi masse brukt i beregningen (kg): "))
        acceleration = float(input("Oppgi akselerasjon brukt i beregningen (m/s^2): "))

        # Kontrollere at F = ma
        if math.isclose(force_calculated, mass * acceleration, rel_tol=1e-5):
            print("Beregningen er korrekt i henhold til Newtons andre lov.")
        else:
            print("Feil: Beregningen samsvarer ikke med Newtons andre lov.")

    except ValueError:
        print("Feil: Vennligst oppgi et gyldig tall.")

# Funksjon for å trene på å utvide kunnskap innen realfag
def expand_knowledge():
    try:
        # Beregning av logaritmer, noe som ofte brukes i fysikk og ingeniørfag
        value = float(input("Oppgi et tall for å beregne logaritmen (basis 10): "))
        if value > 0:
            log_value = math.log10(value)
            print(f"Logaritmen (basis 10) av {value} er {log_value}.")
        else:
            print("Feil: Tallet må være positivt.")

    except ValueError:
        print("Feil: Vennligst oppgi et gyldig tall.")

# Funksjon for å trene på beregninger relevant for dimensjoneringer
def perform_estimations():
    try:
        # Beregning av nødvendig strømkapasitet for et datasenter basert på antall servere
        num_servers = int(input("Oppgi antall servere: "))
        power_per_server = float(input("Oppgi gjennomsnittlig effekt per server (Watt): "))
        total_power = num_servers * power_per_server
        print(f"Total effektbehov er {total_power} Watt.")

        # Beregning av årlig energiforbruk basert på driftstid
        hours_per_day = 24
        days_per_year = 365
        yearly_energy_consumption = (total_power * hours_per_day * days_per_year) / 1000 # kWh
        print(f"Årlig energiforbruk er {yearly_energy_consumption} kWh.")

    except ValueError:
        print("Feil: Vennligst oppgi et gyldig tall.")

# Funksjon for å vurdere matematikkens og fysikkens plass i samfunnet
def societal_impact():
    print("\nMatematikk og fysikk spiller en sentral rolle i teknologisk utvikling, fra energi til helse.")
    print("Kunnskap i realfag gir grunnlag for innovasjon og løsning av komplekse problemer som påvirker samfunnet.")
    print("Dette omfatter alt fra å utvikle ny medisinsk teknologi til å forstå klimaendringer.")
    print("\nFor å utvide dine kunnskaper innen realfag, anbefales det å følge med på forskningspublikasjoner, ta videreutdanning, og delta i faglige nettverk.")

# Hovedmeny for å navigere i de ulike treningsmodulene
def main_menu():
    while True:
        print("\nHovedmeny - Velg en funksjon for å trene på dine realfagskunnskaper:")
        print("1. Utføre grunnleggende fysikkberegninger")
        print("2. Evaluere eget arbeid i henhold til matematiske og fysiske lover")
        print("3. Utvide din kunnskap innen realfag")
        print("4. Utføre beregninger relevant for dimensjoneringer")
        print("5. Forstå matematikkens og fysikkens plass i samfunnet")
        print("6. Avslutt")

        choice = input("Oppgi ditt valg (1-6): ")

        if choice == "1":
            basic_physics_calculations()
        elif choice == "2":
            evaluate_work()
        elif choice == "3":
            expand_knowledge()
        elif choice == "4":
            perform_estimations()
        elif choice == "5":
            societal_impact()
        elif choice == "6":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg, vennligst prøv igjen.")

# Kjør hovedmenyen
if __name__ == "__main__":
    main_menu()