// Bygg menyen for trigonometri og geometri
// Build the menu for trigonometry and geometry
function buildTrigGeoMenu() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Trigonometri og Geometri</h2>
        <button onclick="beregnAreal()">Beregn Areal</button>
        <button onclick="beregnOmkrets()">Beregn Omkrets</button>
        <button onclick="pythagoras()">Pythagoras' setning</button>
        <button onclick="trigonometri()">Trigonometri i rettvinklede trekanter</button>
        <button onclick="vektorer()">Vektorer i planet</button>
    `;
}

// Beregn areal
// Calculate area
function beregnAreal() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Beregn Areal</h2>
        <label for="form">Velg form:</label>
        <select id="form">
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
            <option value="trekant">Trekant</option>
        </select>
        <div id="arealInputs"></div>
        <button onclick="regnUtAreal()">Beregn</button>
        <div id="resultat"></div>
    `;

    document.getElementById('form').addEventListener('change', function() {
        const form = this.value;
        const inputsDiv = document.getElementById('arealInputs');
        inputsDiv.innerHTML = '';

        if (form === 'sirkel') {
            inputsDiv.innerHTML = `
                <label for="radius">Radius:</label>
                <input type="number" id="radius">
            `;
        } else if (form === 'rektangel') {
            inputsDiv.innerHTML = `
                <label for="bredde">Bredde:</label>
                <input type="number" id="bredde">
                <label for="hoyde">Høyde:</label>
                <input type="number" id="hoyde">
            `;
        } else if (form === 'trekant') {
            inputsDiv.innerHTML = `
                <label for="grunnlinje">Grunnlinje:</label>
                <input type="number" id="grunnlinje">
                <label for="hoyde">Høyde:</label>
                <input type="number" id="hoyde">
            `;
        }
    });
}

// Beregn areal basert på valgt form
// Calculate area based on selected shape
function regnUtAreal() {
    const form = document.getElementById('form').value;
    let resultat = '';
    let forklaringNorsk = '';
    let forklaringEngelsk = '';

    if (form === 'sirkel') {
        const radius = parseFloat(document.getElementById('radius').value);
        if (isNaN(radius)) {
            resultat = 'Vennligst oppgi en gyldig radius.';
        } else {
            const areal = Math.PI * radius * radius;
            resultat = `Arealet av sirkelen er ${areal.toFixed(2)} kvadratmeter.`;
            forklaringNorsk = 'Arealet av en sirkel beregnes ved formelen: π * radius^2.';
            forklaringEngelsk = 'The area of a circle is calculated using the formula: π * radius^2.';
        }
    } else if (form === 'rektangel') {
        const bredde = parseFloat(document.getElementById('bredde').value);
        const hoyde = parseFloat(document.getElementById('hoyde').value);
        if (isNaN(bredde) || isNaN(hoyde)) {
            resultat = 'Vennligst oppgi gyldige mål for bredde og høyde.';
        } else {
            const areal = bredde * hoyde;
            resultat = `Arealet av rektangelet er ${areal.toFixed(2)} kvadratmeter.`;
            forklaringNorsk = 'Arealet av et rektangel beregnes ved formelen: bredde * høyde.';
            forklaringEngelsk = 'The area of a rectangle is calculated using the formula: width * height.';
        }
    } else if (form === 'trekant') {
        const grunnlinje = parseFloat(document.getElementById('grunnlinje').value);
        const hoyde = parseFloat(document.getElementById('hoyde').value);
        if (isNaN(grunnlinje) || isNaN(hoyde)) {
            resultat = 'Vennligst oppgi gyldige mål for grunnlinje og høyde.';
        } else {
            const areal = (grunnlinje * hoyde) / 2;
            resultat = `Arealet av trekanten er ${areal.toFixed(2)} kvadratmeter.`;
            forklaringNorsk = 'Arealet av en trekant beregnes ved formelen: (grunnlinje * høyde) / 2.';
            forklaringEngelsk = 'The area of a triangle is calculated using the formula: (base * height) / 2.';
        }
    }

    document.getElementById('resultat').innerHTML = `
        <p>${resultat}</p>
        <p><strong>Forklaring på norsk:</strong> ${forklaringNorsk}</p>
        <p><strong>Explanation in English:</strong> ${forklaringEngelsk}</p>
    `;
}

// Beregn omkrets
// Calculate circumference
function beregnOmkrets() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Beregn Omkrets</h2>
        <label for="form">Velg form:</label>
        <select id="form">
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
            <option value="trekant">Trekant</option>
        </select>
        <div id="omkretsInputs"></div>
        <button onclick="regnUtOmkrets()">Beregn</button>
        <div id="resultat"></div>
    `;

    document.getElementById('form').addEventListener('change', function() {
        const form = this.value;
        const inputsDiv = document.getElementById('omkretsInputs');
        inputsDiv.innerHTML = '';

        if (form === 'sirkel') {
            inputsDiv.innerHTML = `
                <label for="radius">Radius:</label>
                <input type="number" id="radius">
            `;
        } else if (form === 'rektangel') {
            inputsDiv.innerHTML = `
                <label for="bredde">Bredde:</label>
                <input type="number" id="bredde">
                <label for="hoyde">Høyde:</label>
                <input type="number" id="hoyde">
            `;
        } else if (form === 'trekant') {
            inputsDiv.innerHTML = `
                <label for="side1">Side 1:</label>
                <input type="number" id="side1">
                <label for="side2">Side 2:</label>
                <input type="number" id="side2">
                <label for="side3">Side 3:</label>
                <input type="number" id="side3">
            `;
        }
    });
}

// Beregn omkrets basert på valgt form
// Calculate circumference based on selected shape
function regnUtOmkrets() {
    const form = document.getElementById('form').value;
    let resultat = '';
    let forklaringNorsk = '';
    let forklaringEngelsk = '';

    if (form === 'sirkel') {
        const radius = parseFloat(document.getElementById('radius').value);
        if (isNaN(radius)) {
            resultat = 'Vennligst oppgi en gyldig radius.';
        } else {
            const omkrets = 2 * Math.PI * radius;
            resultat = `Omkretsen av sirkelen er ${omkrets.toFixed(2)} meter.`;
            forklaringNorsk = 'Omkretsen av en sirkel beregnes ved formelen: 2 * π * radius.';
            forklaringEngelsk = 'The circumference of a circle is calculated using the formula: 2 * π * radius.';
        }
    } else if (form === 'rektangel') {
        const bredde = parseFloat(document.getElementById('bredde').value);
        const hoyde = parseFloat(document.getElementById('hoyde').value);
        if (isNaN(bredde) || isNaN(hoyde)) {
            resultat = 'Vennligst oppgi gyldige mål for bredde og høyde.';
        } else {
            const omkrets = 2 * (bredde + hoyde);
            resultat = `Omkretsen av rektangelet er ${omkrets.toFixed(2)} meter.`;
            forklaringNorsk = 'Omkrets

Let's complete the content of `trigonometri_geometri_modul.js` with detailed comments in Norwegian and English.

### 5. `trigonometri_geometri_modul.js`