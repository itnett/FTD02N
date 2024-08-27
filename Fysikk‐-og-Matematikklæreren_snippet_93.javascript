// Build the Trigonometry and Geometry menu
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
            resultat = 'Vennligst

Let's complete the content for each file in the interactive learning platform, ensuring all concepts are well-documented in Norwegian and English.

### Project Structure