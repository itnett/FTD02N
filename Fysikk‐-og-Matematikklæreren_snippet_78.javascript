// ... (tidligere kode for rette linjer)

function polynomfunksjoner() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Polynomfunksjoner</h3>
        <textarea id="polynom" placeholder="Skriv inn polynomet (f.eks., x**2 + 3*x - 1)"></textarea>
        <button onclick="tegnPolynomGraf()">Tegn graf</button>
    `;
}

function tegnPolynomGraf() {
    const polynomStr = document.getElementById("polynom").value;
    try {
        const x = symbols('x');
        const polynom = eval(polynomStr);

        const xValues = np.linspace(-10, 10, 400);
        const fPolynom = lambdify(x, polynom, 'numpy');
        const yValues = fPolynom(xValues);

        const trace = {
            x: xValues,
            y: yValues,
            mode: 'lines',
            type: 'scatter',
            name: `y = ${polynom}`
        };

        const layout = {
            title: 'Graf av polynomfunksjonen',
            xaxis: { title: 'x' },
            yaxis: { title: 'y' }
        };

        Plotly.newPlot('resultat', [trace], layout);

        const forklaringNorsk = `
            Et polynom er et uttrykk som består av flere ledd, hvor hvert ledd er et tall (koeffisient) multiplisert med en potens av x. 
            Graden til et polynom er den høyeste eksponenten i uttrykket.
            Grafen til et polynom kan ha flere nullpunkter (der grafen krysser x-aksen) og ekstremalpunkter (topper og bunner).
        `;

        const forklaringEngelsk = `
            A polynomial is an expression consisting of several terms, where each term is a number (coefficient) multiplied by a power of x. 
            The degree of a polynomial is the highest exponent in the expression.
            The graph of a polynomial can have multiple zeros (where the graph crosses the x-axis) and extrema (peaks and valleys).
        `;

        document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
    } catch (error) {
        alert("Ugyldig polynom. Vennligst skriv inn et gyldig uttrykk.");
    }
}

function eksponentialfunksjoner() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Eksponentialfunksjoner (y = a * b^x)</h3>
        <input type="number" id="a" placeholder="Startverdi (a)">
        <input type="number" id="b" placeholder="Vekstfaktor (b)">
        <button onclick="tegnEksponentialGraf()">Tegn graf</button>
    `;
}

function tegnEksponentialGraf() {
    const a = parseFloat(document.getElementById("a").value);
    const b = parseFloat(document.getElementById("b").value);

    const xValues = np.linspace(-2, 2, 100);
    const yValues = a * b ** xValues;

    const trace = {
        x: xValues,
        y: yValues,
        mode: 'lines',
        type: 'scatter',
        name: `y = ${a} * ${b}^x`
    };

    const layout = {
        title: 'Graf av eksponentialfunksjonen',
        xaxis: { title: 'x' },
        yaxis: { title: 'y' }
    };

    Plotly.newPlot('resultat', [trace], layout);

    const forklaringNorsk = `
        En eksponentialfunksjon er en funksjon på formen y = a * b^x, hvor:
        * a er startverdien (verdien av y når x = 0)
        * b er vekstfaktoren (hvor mye y øker for hver enhet x øker)
        Grafen til en eksponentialfunksjon er en kurve som enten vokser eller avtar eksponentielt.
    `;

    const forklaringEngelsk = `
        An exponential function is a function of the form y = a * b^x, where:
        * a is the initial value (the value of y when x = 0)
        * b is the growth factor (how much y increases for each unit increase in x)
        The graph of an exponential function is a curve that either grows or decays exponentially.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function derivasjonAvPolynomfunksjoner() {
    // ... (samme som i forrige svar)
}

function regresjon() {
    // ... (samme som i forrige svar)
}