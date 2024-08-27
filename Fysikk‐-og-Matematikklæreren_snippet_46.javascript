// funksjoner_modul.js

function funksjoner() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Funksjoner</h2>
        <button onclick="retteLinjer()">Rette linjer</button>
        <button onclick="polynomfunksjoner()">Polynomfunksjoner</button>
        <button onclick="eksponentialfunksjoner()">Eksponentialfunksjoner</button>
        <button onclick="derivasjonAvPolynomfunksjoner()">Derivasjon av polynomfunksjoner</button>
        <button onclick="regresjon()">Regresjon (lineær)</button>
        <div id="funksjonerInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function retteLinjer() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Rette linjer (y = mx + b)</h3>
        <input type="number" id="stigningstall" placeholder="Stigningstall (m)">
        <input type="number" id="konstantledd" placeholder="Konstantledd (b)">
        <button onclick="regnUtRettLinje()">Tegn graf</button>
    `;
}

function regnUtRettLinje() {
    const m = parseFloat(document.getElementById("stigningstall").value);
    const b = parseFloat(document.getElementById("konstantledd").value);

    const xValues = [-10, 10]; // Endepunkter for x-aksen
    const yValues = [m * xValues[0] + b, m * xValues[1] + b];

    const trace = {
        x: xValues,
        y: yValues,
        mode: 'lines',
        type: 'scatter',
        name: `y = ${m}x + ${b}`
    };

    const layout = {
        title: 'Graf av en rett linje',
        xaxis: { title: 'x' },
        yaxis: { title: 'y' }
    };

    Plotly.newPlot('resultat', [trace], layout);

    const forklaringNorsk = `
        En rett linje kan beskrives med likningen y = mx + b, hvor:
        * m er stigningstallet (hvor bratt linjen er)
        * b er konstantleddet (hvor linjen krysser y-aksen)
        I denne grafen er m = ${m} og b = ${b}.
    `;

    const forklaringEngelsk = `
        A straight line can be described by the equation y = mx + b, where:
        * m is the slope (how steep the line is)
        * b is the y-intercept (where the line crosses the y-axis)
        In this graph, m = ${m} and b = ${b}.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function polynomfunksjoner() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Polynomfunksjoner</h3>
        <input type="text" id="polynom" placeholder="Skriv inn polynomet (f.eks., x**2 + 3*x - 1)">
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

        // Forklaring (norsk og engelsk)
        const forklaringNorsk = `
            Et polynom er et uttrykk som består av flere ledd, hvor hvert ledd er et tall multiplisert med en potens av x.
            Grafen til et polynom kan ha flere nullpunkter og ekstremalpunkter.
        `;

        const forklaringEngelsk = `
            A polynomial is an expression consisting of several terms, where each term is a number multiplied by a power of x.
            The graph of a polynomial can have multiple zeros and extrema.
        `;

        document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
    } catch (error) {
        alert("Ugyldig polynom. Vennligst skriv inn et gyldig uttrykk.");
    }
}

// ... (Resten av funksjonene for eksponentialfunksjoner, derivasjon og regresjon)