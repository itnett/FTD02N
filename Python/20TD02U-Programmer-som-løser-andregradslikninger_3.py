python
import numpy as np

def solve_linear_system():
    print("Dette programmet løser et system av to lineære ligninger:")
    print("ax + by = e")
    print("cx + dy = f")
    
    a = float(input("Skriv inn konstanten a: "))
    b = float(input("Skriv inn konstanten b: "))
    e = float(input("Skriv inn konstanten e: "))
    c = float(input("Skriv inn konstanten c: "))
    d = float(input("Skriv inn konstanten d: "))
    f = float(input("Skriv inn konstanten f: "))
    
    A = np.array([[a, b], [c, d]])
    B = np.array([e, f])
    
    try:
        solution = np.linalg.solve(A, B)
        print(f"Løsningen er x = {solution[0]}, y = {solution[1]}")
    except np.linalg.LinAlgError:
        print("Ligningssystemet har ingen unik løsning.")

solve_linear_system()