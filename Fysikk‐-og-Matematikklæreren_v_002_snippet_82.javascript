// Funksjoner

function buildFunctionsMenu() {
    // ... (same as in previous response)
}

// Rette linjer
function retteLinjer() {
    // ... (same as in previous response)
}

function regnUtRettLinje() {
    // ... (same as in previous response)
}

// Polynomfunksjoner
function polynomfunksjoner() {
    // ... (same as in previous response)
}

function tegnPolynomGraf() {
    // ... (same as in previous response)
}

// Eksponentialfunksjoner
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
        En eksponentialfunksjon beskriver en størrelse som vokser eller avtar med en konstant prosentvis endring over tid.
        Formelen er y = a * b^x, der:
        * a er startverdien (verdien av y når x = 0)
        * b er vekstfaktoren (hvor mye y endres for hver enhetsøkning i x).
    `;
    const forklaringEngelsk = `
        An exponential function describes a quantity that grows or decays at a constant percentage rate over time.
        The formula is y = a * b^x, where:
        * a is the initial value (the value of y when x = 0)
        * b is the growth factor (how much y changes for each unit increase in x).
    `;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Derivasjon av polynomfunksjoner
function derivasjonAvPolynomfunksjoner() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Derivasjon av polynomfunksjoner</h3>
        <textarea id="polynom" placeholder="Skriv inn polynomet (f.eks., x**2 + 3*x - 1)"></textarea>
        <button onclick="regnUtDerivasjon()">Beregn</button>
    `;
}

function regnUtDerivasjon() {
    const polynomStr = document.getElementById("polynom").value;
    try {
        const x = symbols('x');
        const polynom = eval(polynomStr);
        const derivert = diff(polynom, x);

        document.getElementById("resultat").textContent = `Den deriverte av ${polynom} er: ${derivert}`;

        const forklaringNorsk = `
            Den deriverte av et polynom er et nytt polynom som beskriver hvor raskt det opprinnelige polynomet endrer seg i hvert punkt. 
            Den deriverte kan brukes til å finne stigningstallet til tangenten til grafen i et gitt punkt.
        `;

        const forklaringEngelsk = `
            The derivative of a polynomial is a new polynomial that describes how fast the original polynomial changes at each point. 
            The derivative can be used to find the slope of the tangent line to the graph at a given point.
        `;

        document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;

        // Plotly-visualisering (optional)
        // ... (Legg til kode for å plotte grafen til polynomet og den deriverte)
    } catch (error) {
        alert("Ugyldig polynom. Vennligst skriv inn et gyldig uttrykk.");
    }
}

// Regresjon ved hjelp av digitale hjelpemidler
function regresjon() {
    // ... (same as in previous response)
}

function utførRegresjon() {
    // ... (same as in previous response)
}