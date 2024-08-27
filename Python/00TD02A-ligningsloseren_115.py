python
# Define the function to solve quadratic equations using the quadratic formula
def solve_quadratic(a, b, c):
    import cmath
    d = (b**2) - (4*a*c)
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)
    return sol1, sol2

# List of tasks (each task is a tuple of coefficients a, b, c)
tasks = [
    (1, -4, 3),  # Oppgave 1a
    (1, 2, -15),  # Oppgave 1b
    (1, 6, 8),  # Oppgave 1c
    (1, -7, 12),  # Oppgave 1d
    (1, -2, -35),  # Oppgave 2a
    (2, 3, -2),  # Oppgave 2b
    (8, -2, -1),  # Oppgave 2c
    (1, 0, -3),  # Oppgave 2d
    # Graphical solutions for Oppgave 3, 4, 5, and 6 are omitted in this example
    (1, -6, 0),  # Oppgave 8a
    (2, 10, 0),  # Oppgave 8b
    (-3, 12, 0),  # Oppgave 8c
    (-1, -3, 0),  # Oppgave 8d
    (1, -25, 0),  # Oppgave 9a
    (2, -32, 0),  # Oppgave 9b
    (-2, 18, 0),  # Oppgave 9c
    (1, 0, 4),  # Oppgave 9d, which has no real solution
    (1, 6, -7),  # Oppgave 10
    (1, 8, -48),  # Oppgave 11
    (1, -4, 3),  # Oppgave 12a
    (1, 10, -24),  # Oppgave 12b
    (2, 16, -18),  # Oppgave 12c
    (1, -5, 4),  # Oppgave 13a
    (1, 7, -8),  # Oppgave 13b
    (1, -9, 20),  # Oppgave 13c
    (1, -6, 8),  # Oppgave 14
    (1, -2, 2),  # Oppgave 15a
    (1, 2, 5)  # Oppgave 15b
]

# Loop through each task and solve the quadratic equation
for i, (a, b, c) in enumerate(tasks):
    sol1, sol2 = solve_quadratic(a, b, c)
    print(f"Oppgave {i+1}: Løsningene til ligningen {a}x^2 + {b}x + {c} = 0 er {sol1} og {sol2}")