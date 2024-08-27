python
import sympy as sp

def prompt_for_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Vennligst skriv inn et gyldig tall.")

def prompt_for_equation():
    print("Velkommen til ligningsløseren!")
    print("En andregradslikning har formen ax^2 + bx + c = 0.")
    print("Her er a, b, og c koeffisienter. Vennligst oppgi disse verdiene.")

    a = prompt_for_value("Hva er verdien av andregradsleddet (a)? ")
    b = prompt_for_value("Hva er verdien av førstegradsleddet (b)? ")
    c = prompt_for_value("Hva er verdien av konstantleddet (c)? ")
    return a, b, c

def solve_linear(b, c):
    if b == 0:
        print("Likningen er ugyldig fordi både a og b er 0.")
    else:
        solution = -c / b
        print(f"Løsning: x = {solution}")

def solve_quadratic(a, b, c):
    x = sp.symbols('x')
    expr = a*x**2 + b*x + c
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

def explain_and_solve(a, b, c):
    print(f"\nLikningen du har oppgitt er: {a}x^2 + {b}x + {c} = 0\n")

    if a == 0:
        print("Dette er ikke en andregradslikning fordi a = 0. Dette blir en førstegradslikning.")
        solve_linear(b, c)
    else:
        print("Dette er en andregradslikning.")
        print(f"Identifiserte koeffisienter: a = {a}, b = {b}, c = {c}")

        if c == 0:
            print("Konstantleddet (c) mangler.")
            solutions = sp.solve(a*sp.symbols('x')**2 + b*sp.symbols('x'), sp.symbols('x'))
            print(f"Løsning: x = {solutions}")
        elif b == 0:
            print("Førstegradsleddet (b) mangler.")
            solutions = sp.solve(a*sp.symbols('x')**2 + c, sp.symbols('x'))
            if solutions:
                print(f"Løsning: x = {solutions}")
            else:
                print("Ingen reelle løsninger.")
        else:
            solve_quadratic(a, b, c)

def main():
    a, b, c = prompt_for_equation()
    explain_and_solve(a, b, c)

if __name__ == "__main__":
    main()