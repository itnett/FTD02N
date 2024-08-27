// Bygg menyen for funksjoner og grafer
// Build the menu for functions and graphs
function buildFunctionsMenu() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Funksjoner og Grafer</h2>
        <button onclick="retteLinjer()">Rette Linjer</button>
        <button onclick="polynomfunksjoner()">Polynomfunksjoner</button>
        <button onclick="eksponentialfunksjoner()">Eksponentialfunksjoner</button>
        <button onclick="derivasjon()">Derivasjon av Polynomfunksjoner</button>
        <button onclick="regresjon()">Regresjon</button>
    `;
}

// Rette Linjer
// Straight Lines
function retteLinjer() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Rette Linjer</h2>
        <p>
            En rett linje kan beskrives med ligningen y = mx + b, der m er stigningstallet og b er skjæringspunktet med y-aksen.
        </p>
        <p>
            A straight line can be described by the equation y = mx + b, where m is the slope and b is the y-intercept.
        </p>
        <label for="stigning">Stigningstall (m):</label>
        <input type="number" id="stigning">
        <label for="skjering">Skjæringspunkt (b):</label>
        <input type="number" id="skjering">
        <button onclick="tegnRettLinje()">Tegn Rett Linje</button>
        <div id="graf"></div>
    `;
}

// Tegn rett linje
// Draw straight line
function tegnRettLinje() {
    const m = parseFloat(document.getElementById('stigning').value);
    const b = parseFloat(document.getElementById('skjering').value);
    const graf = document.getElementById('graf');

    if (isNaN(m) || isNaN(b)) {
        graf.innerHTML = '<p>Vennligst oppgi gyldige verdier for stigningstall og skjæringspunkt.</p>';
        return;
    }

    // Plotting the line using Plotly.js
    const xValues = Array.from({length: 11}, (_, i) => i - 5);
    const yValues = xValues.map(x => m * x + b);

    const data = [{
        x: xValues,
        y: yValues,
        type: 'scatter'
    }];

    Plotly.newPlot('graf', data);

    graf.innerHTML = `
        <p><strong>Forklaring på norsk:</strong> Ligningen for den rette linjen er y = ${m}x + ${b}.</p>
        <p><strong>Explanation in English:</strong> The equation of the straight line is y = ${m}x + ${b}.</p>
    `;
}

// Polynomfunksjoner
// Polynomial functions
function polynomfunksjoner() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Polynomfunksjoner</h2>
        <p>
            En polynomfunksjon er en funksjon som kan skrives som en sum av ledd, der hvert ledd er et produkt av en konstant og en variabel opphøyd i en heltallig eksponent.
        </p>
        <p>
            A polynomial function is a function that can be written as a sum of terms, where each term is a product of a constant and a variable raised to an integer exponent.
        </p>
        <label for="koeffisienter">Koeffisienter (komma-separert):</label>
        <input type="text" id="koeffisienter">
        <button onclick="tegnPolynom()">Tegn Polynom</button>
        <div id="graf"></div>
    `;
}

// Tegn polynom
// Draw polynomial
function tegnPolynom() {
    const koeffisienter = document.getElementById('koeffisienter').value.split(',').map(parseFloat);
    const graf = document.getElementById('graf');

    if (koeffisienter.some(isNaN)) {
        graf.innerHTML = '<p>Vennligst oppgi gyldige verdier for koeffisienter.</p>';
        return;
    }

    // Plotting the polynomial using Plotly.js
    const xValues = Array.from({length: 101}, (_, i) => i - 50);
    const yValues = xValues.map(x => koeffisienter.reduce((sum, coeff, index) => sum + coeff * Math.pow(x, index), 0));

    const data = [{
        x: xValues,
        y: yValues,
        type: 'scatter'
    }];

    Plotly.newPlot('graf', data);

    graf.innerHTML = `
        <p><strong>Forklaring på norsk:</strong> Polynomfunksjonen er beskrevet av koeffisientene: ${koeffisienter.join(', ')}.</p>
        <p><strong>Explanation in English:</strong> The polynomial function is described by the coefficients: ${koeffisienter.join(', ')}.</p>
    `;
}

// Eksponentialfunksjoner
// Exponential functions
function eksponentialfunksjoner() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Eksponentialfunksjoner</h2>
        <p>
            En eksponentialfunksjon er en funksjon der en variabel vises i eksponenten. Den generelle formen er f(x) = a * b^x, der a og b er konstanter.
        </p>
        <p>
            An exponential function is a function where a variable appears in the exponent. The general form is f(x) = a * b^x, where a and b are constants.
        </p>
        <label for="a">Konstant a:</label>
        <input type="number" id="a">
        <label for="b">Konstant b:</label>
        <input type="number" id="b">
        <button onclick="tegnEksponential()">Tegn Eksponential</button>
        <div id="graf"></div>
    `;
}

// Tegn eksponentialfunksjon
// Draw exponential function
function tegnEksponential() {
    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);
    const graf = document.getElementById('graf');

    if (isNaN(a) || isNaN(b)) {
        graf.innerHTML = '<p>Vennligst oppgi gyldige verdier for konstantene a og b.</p>';
        return;
    }

    // Plotting the exponential function using Plotly.js
    const xValues = Array.from({length: 101}, (_, i) => i - 50);
    const yValues = xValues.map(x => a * Math.pow(b, x));

    const data = [{
        x: xValues,
        y: yValues,
        type: 'scatter'
    }];

    Plotly.newPlot('graf', data);

    graf.innerHTML = `
        <p><strong>Forklaring på norsk:</strong> Eksponentialfunksjonen er f(x) = ${a} * ${b}^x.</p>
        <p><strong>Explanation in English:</strong> The exponential function is f(x) = ${a} * ${b}^x.</p>
    `;
}

// Derivasjon av polynomfunksjoner
// Derivative of polynomial functions
function derivasjon() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Derivasjon av Polynomfunksjoner</h2>
        <p>
            Derivasjon av en polynomfunksjon innebærer å finne funksjonen som beskriver helningen til den opprinnelige funksjonen. For en polynomfunksjon f(x) = ax^n, er den deriverte f'(x) = n*ax^(n-1).
        </p>
        <p>
            Differentiation of a polynomial function involves finding the function that describes the slope of the original function. For a polynomial function f(x) = ax^n, the derivative is f'(x) = n*ax^(n-1).
        </p>
        <label for="koeffisienterDeriv">Koeffisienter (komma-separert):</label>
        <input type="text" id="koeffisienterDeriv">
        <button onclick="deriverPolynom()">Deriver Polynom</button>
        <div id="graf"></div>
    `;
}

// Deriver polynom
// Differentiate polynomial
function deriverPolynom() {
    const koeffisienter = document.getElementById('koeffisienterDeriv').value.split(',').map(parseFloat);
    const graf = document.getElementById('graf');

    if (koeffisienter.some(isNaN)) {