python
while True:
    try:
        task_number = int(input("Skriv inn oppgavenummer (1-15) eller 0 for å avslutte: "))
        if task_number == 0:
            break
        if 1 <= task_number <= len(tasks):
            a, b, c = tasks[task_number - 1]
            sol1, sol2 = solve_quadratic(a, b, c)
            print(f"Oppgave {task_number}: Løsningene til ligningen {a}x^2 + {b}x + {c} = 0 er {sol1} og {sol2}")
        else:
            print("Ugyldig oppgavenummer. Prøv igjen.")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn et tall.")