/**
 * Bygger menyen for funksjoner.
 */
function funksjoner() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Funksjoner</h2>
        <button onclick="retteLinjer()">Rette linjer</button>
        <button onclick="polynomfunksjoner()">Polynomfunksjoner</button>
        <button onclick="eksponentialfunksjoner()">Eksponentialfunksjoner</button>
        <button onclick="derivasjonAvPolynomfunksjoner()">Derivasjon av polynomfunksjoner</button>
        <button onclick="regresjon()">Regresjon (lineær)</button>
        <button onclick="byggMatematikkMeny()">Tilbake til matematikkmenyen</button>
        <div id="funksjonerInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

/**
 * Viser input-felter for rette linjer.
 */
function retteLinjer() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Rette linjer (y = mx + b)</h3>
        <input type="number" id="stigningstall" placeholder="Stigningstall (m)">
        <input type="number" id="konstantledd" placeholder="Konstantledd (b)">
        <button onclick="regnUtRettLinje()">Tegn graf</

button>
    `;
}

/**
 * Beregner og tegner grafen for en rett linje.
 */
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

// Implementer de andre funksjonene for polynomfunksjoner, eksponentialfunksjoner, derivasjon og regresjon på lignende måte som rette linjer funksjonen.