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
                <input type="number" id="h