python
# ... (tidligere kode for algebra, trigonometri og geometri)

def funksjoner():
    """
    Presents the functions submenu and allows the user to select a specific operation.

    Presenterer undermenyen for funksjoner og lar brukeren velge en spesifikk operasjon.
    """

    while True:
        print("\nFunksjoner:")
        print("1. Rette linjer")
        print("2. Polynomfunksjoner")
        print("3. Eksponentialfunksjoner")
        print("4. Derivasjon av polynomfunksjoner")
        print("5. Regresjon (lineær)")
        print("0. Tilbake til hovedmenyen")

        valg = input("Skriv inn ditt valg (0-5): ")

        if valg == '1':
            rette_linjer()
        elif valg == '2':
            polynomfunksjoner()
        elif valg == '3':
            eksponentialfunksjoner()
        elif valg == '4':
            derivasjon_av_polynomfunksjoner()
        elif valg == '5':
            regresjon()
        elif valg == '0':
            break
        else:
            print("Ugyldig valg. Vennligst prøv igjen.")

def rette_linjer():
    """
    Calculates and visualizes linear functions (y = mx + b) based on user input.

    Beregner og visualiserer lineære funksjoner (y = mx + b) basert på brukerinput.
    """

    try:
        m = float(input("Skriv inn stigningstallet (m): "))
        b = float(input("Skriv inn konstantleddet (b): "))

        x_values = np.linspace(-10, 10, 100)
        y_values = m * x_values + b

        plt.plot(x_values, y_values, label=f'y = {m}x + {b}')
        plt.title('Graf av en rett linje')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def polynomfunksjoner():
    """
    Calculates and visualizes polynomial functions based on user input.

    Beregner og visualiserer polynomfunksjoner basert på brukerinput.
    """

    grad = int(input("Skriv inn graden til polynomet: "))
    koeffisienter = []
    for i in range(grad + 1):
        koeffisienter.append(float(input(f"Skriv inn koeffisienten for x^{grad-i}: ")))

    x = symbols('x')
    polynom = sum(koeffisienter[i] * x**(grad-i) for i in range(grad + 1))

    print(f"Polynomfunksjonen er: {polynom}")

    # Visualisering
    x_values = np.linspace(-10, 10, 400)
    f_polynom = lambdify(x, polynom, 'numpy')
    y_values = f_polynom(x_values)

    plt.plot(x_values, y_values, label=f'y = {polynom}')
    plt.title('Graf av polynomfunksjonen')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

def eksponentialfunksjoner():
    """
    Calculates and visualizes exponential functions (y = a * b^x) based on user input.

    Beregner og visualiserer eksponentialfunksjoner (y = a * b^x) basert på brukerinput.
    """

    try:
        a = float(input("Skriv inn startverdien (a): "))
        b = float(input("Skriv inn vekstfaktoren (b): "))

        x_values = np.linspace(-2, 2, 100)
        y_values = a * b**x_values

        plt.plot(x_values, y_values, label=f'y = {a} * {b}^x')
        plt.title('Graf av eksponentialfunksjonen')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn tall.")

def derivasjon_av_polynomfunksjoner():
    """
    Calculates and displays the derivative of a polynomial function provided by the user.

    Beregner og viser den deriverte av en polynomfunksjon oppgitt av brukeren.
    """
    
    try:
        polynom_str = input("Skriv inn polynomet (f.eks., 'x**2 + 3*x - 1'): ")
        x = symbols('x')
        polynom = eval(polynom_str)
        derivert = diff(polynom, x)
        print(f"Den deriverte av polynomet {polynom} er: {derivert}")

        # Visualisering av polynomet og den deriverte
        x_vals = np.linspace(-10, 10, 400)
        f_polynom = lambdify(x, polynom, 'numpy')
        f_derivert = lambdify(x, derivert, 'numpy')
        y_vals = f_polynom(x_vals)
        y_derivert_vals = f_derivert(x_vals)

        plt.plot(x_vals, y_vals, label=f'y = {polynom}')
        plt.plot(x_vals, y_derivert_vals, label=f"y' = {derivert}", linestyle='--')
        plt.title('Polynom og dets Deriverte')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
    except:
        print("Ugyldig input eller polynom. Vennligst prøv igjen.")

def regresjon():
    """
    Performs linear regression on a set of data points provided by the user.

    Utfører lineær regresjon på et sett med datapunkter oppgitt av brukeren.
    """

    try:
        n = int(input("Skriv inn antall datapunkter: "))
        x_values = []
        y_values = []
        for i in range(n):
            x = float(input(f"Skriv inn x-verdi for punkt {i+1}: "))
            y = float(input(f"Skriv inn y-verdi for punkt {i+1}: "))
            x_values.append(x)
            y_values.append(y)

        x_values = np.array(x_values).reshape((-1, 1))
        y_values = np.array(y_values)

        model = LinearRegression()
        model.fit(x_values, y_values)
        y_pred = model.predict(x_values)

        plt.scatter(x_values, y_values, color='blue', label='Datapunkter')
        plt.plot(x_values, y_pred, color='red', label='Regresjonslinje')
        plt.title('Lineær Regresjon')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt