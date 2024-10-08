python
def prompt_for_equation():
    print("Velkommen til ligningsløseren!")
    print("Vennligst skriv inn en andregradslikning i form av ax^2 + bx + c = 0")
    print("hvor a, b, og c er koeffisienter.")
    
    while True:
        try:
            a = float(input("Hva er verdien av andregradsleddet (a)? "))
            b = float(input("Hva er verdien av førstegradsleddet (b)? "))
            c = float(input("Hva er verdien av konstantleddet (c)? "))
            return a, b, c
        except ValueError:
            print("Vennligst skriv inn gyldige tall for a, b, og c.")

def explain_and_solve(a, b, c):
    import sympy as sp

    x = sp.symbols('x')
    expr = a*x**2 + b*x + c
    print(f"\nLikningen du har oppgitt er: {a}x^2 + {b}x + {c} = 0\n")

    if a == 0:
        print("Dette er ikke en andregradslikning fordi a = 0. Dette blir en førstegradslikning.")
        if b != 0:
            solution = sp.solve(expr, x)
            print(f"Løsning: x = {solution}")
        else:
            print("Likningen er ugyldig fordi både a og b er 0.")
        return

    print("Dette er en andregradslikning.")
    print(f"Identifiserte koeffisienter: a = {a}, b = {b}, c = {c}")

    if c == 0:
        print("Konstantleddet (c) mangler.")
        print("Når konstantleddet mangler, kan vi faktorisere uttrykket ved å sette x utenfor parentes.")
        solutions = sp.solve(a*x**2 + b*x, x)
        print(f"Løsning: x = {solutions}")
    elif b == 0:
        print("Førstegradsleddet (b) mangler.")
        print("Når førstegradsleddet mangler, kan vi isolere x^2 på den ene siden og deretter ta kvadratrota.")
        solutions = sp.solve(a*x**2 + c, x)
        if solutions:
            print(f"Løsning: x = {solutions}")
        else:
            print("Ingen reelle løsninger.")
    else:
        print("Bruker abc-formelen for å løse andregradslikningen.")
        print("abc-formelen er: x = (-b ± sqrt(b^2 - 4ac)) / 2a")
        discriminant = b**2 - 4*a*c
        print(f"Diskriminanten (b^2 - 4ac) er: {discriminant}")
        if discriminant > 0:
            sol1 = (-b + sp.sqrt(discriminant)) / (2*a)
            sol2 = (-b - sp.sqrt(discriminant)) / (2*a)
            print(f"Løsningene er: x1 = {sol1}, x2 = {sol2}")
        elif discriminant == 0:
            sol = -b / (2*a)
            print(f"Det er kun én løsning: x = {sol}")
        else:
            print("Ingen reelle løsninger.")
    
    # Verifisering av løsningen
    solutions = sp.solve(expr, x)
    if solutions:
        if all(sp.simplify(expr.subs(x, sol)) == 0 for sol in solutions):
            print("Løsningen er verifisert.")
        else:
            print("Løsningen stemmer ikke.")

def main():
    a, b, c = prompt_for_equation()
    explain_and_solve(a, b, c)

if __name__ == "__main__":
    main()