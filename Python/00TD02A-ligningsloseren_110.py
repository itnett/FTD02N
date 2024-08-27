python
def get_quadratic_coefficients():
    while True:
        try:
            a = float(input("Skriv inn koeffisienten a (foran x^2): "))
            b = float(input("Skriv inn koeffisienten b (foran x): "))
            c = float(input("Skriv inn konstanten c: "))
            return a, b, c
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn tallverdier for a, b og c.")

def solve_quadratic(a, b, c):
    import cmath
    d = (b**2) - (4*a*c)
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    return sol1, sol2

def profit_calculation():
    print("Oppgave 7")
    print("Beregning av hvor mange blader som må produseres og selges for å gå i overskudd.")
    
    try:
        # Definer kostnads- og inntektsfunksjonene
        def cost_function(x):
            return 0.0015 * x**2 + 20 * x + 50000
        
        def revenue_function(x):
            return -0.001 * x**2 + 50 * x
        
        # Løsning av likningen for overskudd
        # Inntekt = Kostnad => -0.001 * x^2 + 50 * x = 0.0015 * x^2 + 20 * x + 50000
        # Vi setter det lik null og finner x:
        # 0.0015 * x^2 + 20 * x + 50000 + 0.001 * x^2 - 50 * x = 0
        # 0.0025 * x^2 - 30 * x + 50000 = 0
        
        a = 0.0025
        b = -30
        c = 50000
        
        sol1, sol2 = solve_quadratic(a, b, c)
        
        print(f"Løsningene til ligningen 0.0025x^2 - 30x + 50000 = 0 er x = {sol1} og x = {sol2}")
        print("Det betyr at Hans Luftvik må produsere og selge mellom disse to mengdene for å gå i overskudd.")
    
    except Exception as e:
        print(f"En feil oppstod: {e}")

def main():
    while True:
        print("\nVelkommen til løseren for andregradslikninger.")
        print("Velg en oppgave:")
        print("1. Løs en standard andregradslikning")
        print("2. Beregn overskudd for Hans Luftvik sitt flymagasin (Oppgave 7)")
        print("0. Avslutt")
        
        try:
            choice = int(input("Ditt valg: "))
            if choice == 1:
                print("Du har valgt å løse en standard andregradslikning.")
                a, b, c = get_quadratic_coefficients()
                sol1, sol2 = solve_quadratic(a, b, c)
                print(f"Løsningene til ligningen {a}x^2 + {b}x + {c} = 0 er x = {sol1} og x = {sol2}")
            elif choice == 2:
                profit_calculation()
            elif choice == 0:
                print("Avslutter programmet.")
                break
            else:
                print("Ugyldig valg, vennligst prøv igjen.")
        except ValueError:
            print("Ugyldig input. Vennligst skriv inn et tall.")

if __name__ == "__main__":
    main()