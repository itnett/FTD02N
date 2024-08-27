// Bygger menyen for funksjoner
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

// Funksjoner for rette linjer
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

    if (isNaN(m) || isNaN(b)) {
        alert("Vennligst fyll inn gyldige verdier.");
        return;
    }

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

// Funksjoner for polynomfunksjoner
function polynomfunksjoner() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Polynomfunksjoner</h3>
        <input type="text" id="polynom" placeholder="Skriv inn polynom (f.eks. x^3 - 2x + 1)">
        <button onclick="tegnPolynomGraf()">Tegn graf</button>
    `;
}

function tegnPolynomGraf() {
    const polynomStr = document.getElementById("polynom").value;
    if (!polynomStr) {
        alert("Vennligst fyll inn et polynom.");
        return;
    }

    try {
        const xValues = [];
        const yValues = [];

        for (let x = -10; x <= 10; x += 0.1) {
            xValues.push(x);
            yValues.push(math.evaluate(polynomStr, { x }));
        }

        const trace = {
            x: xValues,
            y: yValues,
            mode: 'lines',
            type: 'scatter',
            name: polynomStr
        };

        const layout = {
            title: `Graf av polynomfunksjon ${polynomStr}`,
            xaxis: { title: 'x' },
            yaxis: { title: 'y' }
        };

        Plotly.newPlot('resultat', [trace], layout);

        const forklaringNorsk = `
            Et polynom er et matematisk uttrykk bestående av variabler og koeffisienter, som kan kombineres ved bruk av
            addisjon, subtraksjon, multiplikasjon og ikke-negative heltallseksponenter. I denne grafen er polynomet ${polynomStr}.
        `;

        const forklaringEngelsk = `
            A polynomial is a mathematical expression consisting of variables and coefficients, combined using
            addition, subtraction, multiplication, and non-negative integer exponents. In this graph, the polynomial is ${polynomStr}.
        `;

        document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
    } catch (error) {
        alert("Det oppsto en feil ved evaluering av polynomet. Vennligst sjekk syntaksen.");
    }
}

// Funksjoner for eksponentialfunksjoner
function eksponentialfunksjoner() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Eksponentialfunksjoner</h3>
        <input type="number" id="base" placeholder="Base (a)">
        <input type="number" id="eksponent" placeholder="Eksponent (x)">
        <button onclick="tegnEksponentialGraf()">Tegn graf</button>
    `;
}

function tegnEksponentialGraf() {
    const base = parseFloat(document.getElementById("base").value);
    const eksponent = parseFloat(document.getElementById("eksponent").value);

    if (isNaN(base) || isNaN(eksponent)) {
        alert("Vennligst fyll inn gyldige verdier.");
        return;
    }

    const xValues = [];
    const yValues = [];

    for (let x = -10; x <= 10; x += 0.1) {
        xValues.push(x);
        yValues.push(base ** x);
    }

    const trace = {
        x: xValues,
        y: yValues,
        mode: 'lines',
        type: 'scatter',
        name: `y = ${base}^x`
    };

    const layout = {
        title: `Graf av eksponentialfunksjon y = ${base}^x`,
        xaxis: { title: 'x' },
        yaxis: { title: 'y' }
    };

    Plotly.newPlot('resultat', [trace], layout);

    const forklaringNorsk = `
        En eksponentialfunksjon er en funksjon hvor en konstant base opphøyes til en variabel eksponent. 
        I denne grafen er basen ${base} og eksponenten x.
    `;

    const forklaringEngelsk = `
        An exponential function is a function where a constant base is raised to a variable exponent. 
        In this graph, the base is ${base} and the exponent is x.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for derivasjon av polynomfunksjoner
function derivasjonAvPolynomfunksjoner() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Derivasjon av polynomfunksjoner</h3>
        <input type="text" id="polynom" placeholder="Skriv inn polynom (f.eks. x^3 - 2x + 1)">
        <button onclick="regnUtDerivasjon()">Beregn derivasjon</button>
    `;
}

function regnUtDerivasjon() {
    const polynomStr = document.getElementById("polynom").value;
    if (!polynomStr) {
        alert("Vennligst fyll inn et polynom.");
        return;
    }

    try {
        const derivasjonStr = math.derivative(polynomStr, 'x').toString();

        const xValues = [];
        const yValues = [];
        const yValuesDerivert = [];

        for (let x = -10; x <= 10; x += 0.1) {
            xValues.push(x);
            yValues.push(math.evaluate(polynomStr, { x

 }));
            yValuesDerivert.push(math.evaluate(derivasjonStr, { x }));
        }

        const tracePolynom = {
            x: xValues,
            y: yValues,
            mode: 'lines',
            type: 'scatter',
            name: polynomStr
        };

        const traceDerivert = {
            x: xValues,
            y: yValuesDerivert,
            mode: 'lines',
            type: 'scatter',
            name: `Derivert: ${derivasjonStr}`
        };

        const layout = {
            title: `Graf av polynom og dets deriverte`,
            xaxis: { title: 'x' },
            yaxis: { title: 'y' }
        };

        Plotly.newPlot('resultat', [tracePolynom, traceDerivert], layout);

        const forklaringNorsk = `
            Derivasjon av et polynom gir oss helningen (stigningstallet) til grafen i hvert punkt. 
            Den deriverte funksjonen er ${derivasjonStr}.
        `;

        const forklaringEngelsk = `
            The derivative of a polynomial gives us the slope of the graph at each point. 
            The derivative function is ${derivasjonStr}.
        `;

        document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
    } catch (error) {
        alert("Det oppsto en feil ved evaluering av derivasjonen. Vennligst sjekk syntaksen.");
    }
}

// Funksjoner for regresjon
function regresjon() {
    const funksjonerInputDiv = document.getElementById("funksjonerInput");
    funksjonerInputDiv.innerHTML = `
        <h3>Regresjon (lineær)</h3>
        <input type="number" id="xValues" placeholder="x-verdier (kommaseparert)">
        <input type="number" id="yValues" placeholder="y-verdier (kommaseparert)">
        <button onclick="regnUtRegresjon()">Beregn regresjon</button>
    `;
}

function regnUtRegresjon() {
    const xValuesStr = document.getElementById("xValues").value;
    const yValuesStr = document.getElementById("yValues").value;

    if (!xValuesStr || !yValuesStr) {
        alert("Vennligst fyll inn både x- og y-verdier.");
        return;
    }

    const xValues = xValuesStr.split(',').map(Number);
    const yValues = yValuesStr.split(',').map(Number);

    if (xValues.length !== yValues.length) {
        alert("Antallet x- og y-verdier må være det samme.");
        return;
    }

    const n = xValues.length;
    const sumX = xValues.reduce((a, b) => a + b, 0);
    const sumY = yValues.reduce((a, b) => a + b, 0);
    const sumXY = xValues.reduce((sum, x, i) => sum + x * yValues[i], 0);
    const sumX2 = xValues.reduce((sum, x) => sum + x ** 2, 0);

    const m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX ** 2);
    const b = (sumY - m * sumX) / n;

    const yRegresjon = xValues.map(x => m * x + b);

    const traceData = {
        x: xValues,
        y: yValues,
        mode: 'markers',
        type: 'scatter',
        name: 'Data'
    };

    const traceRegresjon = {
        x: xValues,
        y: yRegresjon,
        mode: 'lines',
        type: 'scatter',
        name: `Regresjonslinje: y = ${m.toFixed(2)}x + ${b.toFixed(2)}`
    };

    const layout = {
        title: 'Lineær regresjon',
        xaxis: { title: 'x' },
        yaxis: { title: 'y' }
    };

    Plotly.newPlot('resultat', [traceData, traceRegresjon], layout);

    const forklaringNorsk = `
        Lineær regresjon er en metode for å finne den beste rette linjen som passer til et sett med data. 
        Regresjonslinjen har formelen y = mx + b, hvor m er stigningstallet og b er konstantleddet.
        I denne regresjonen er m = ${m.toFixed(2)} og b = ${b.toFixed(2)}.
    `;

    const forklaringEngelsk = `
        Linear regression is a method to find the best-fitting straight line to a set of data. 
        The regression line has the formula y = mx + b, where m is the slope and b is the y-intercept.
        In this regression, m = ${m.toFixed(2)} and b = ${b.toFixed(2)}.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}