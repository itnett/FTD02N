python
def solve_linear():
    print("Dette programmet løser lineære ligninger på formen ax + b = 0.")
    
    a = float(input("Skriv inn konstanten a: "))
    b = float(input("Skriv inn konstanten b: "))
    
    if a != 0:
        x = -b / a
        print(f"Løsningen er x = {x}.")
    else:
        if b == 0:
            print("Uendelig mange løsninger.")
        else:
            print("Ingen løsninger.")

solve_linear()