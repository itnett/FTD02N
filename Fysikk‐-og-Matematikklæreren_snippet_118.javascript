// Bygg menyen for trigonometri og geometri
// Build the menu for trigonometry and geometry
function buildTrigGeoMenu() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Trigonometri og Geometri</h2>
        <button onclick="beregnAreal()">Beregn Areal</button>
        <button onclick="beregnOmkrets()">Beregn Omkrets</button>
        <button onclick="beregnVolum()">Beregn Volum</button>
        <button onclick="beregnOverflate()">Beregn Overflate</button>
        <button onclick="pythagoras()">Pythagoras' setning</button>
        <button onclick="trigonometri()">Trigonometri i rettvinklede trekanter</button>
        <button onclick="vektorer()">Vektorer i planet</button>
        <div id="trigGeomInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Funksjoner for arealberegning
// Functions for calculating area
function beregnAreal() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn Areal</h3>
        <label for="figur">Velg figur:</label>
        <select id="figur">
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
            <option value="trekant">Trekant</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtAreal()">Beregn</button>
    `;

    document.getElementById("figur").addEventListener("change", function() {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");

        switch (figur) {
            case "sirkel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "rektangel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="bredde" placeholder="Bredde">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            case "trekant":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="grunnlinje" placeholder="Grunnlinje">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            default:
                inputFeltDiv.innerHTML = "";
        }
    });
}

function regnUtAreal() {
    const figur = document.getElementById("figur").value;
    let areal;
    let forklaringNorsk, forklaringEngelsk;

    switch (figur) {
        case "sirkel":
            const radius = parseFloat(document.getElementById("radius").value);
            if (isNaN(radius)) {
                document.getElementById("resultat").textContent = 'Vennligst oppgi en gyldig radius.';
                return;
            }
            areal = Math.PI * radius ** 2;
            forklaringNorsk = `Arealet av en sirkel er π * radius^2.`;
            forklaringEngelsk = `The area of a circle is π * radius squared.`;
            break;
        case "rektangel":
            const bredde = parseFloat(document.getElementById("bredde").value);
            const hoyde = parseFloat(document.getElementById("hoyde").value);
            if (isNaN(bredde) || isNaN(hoyde)) {
                document.getElementById("resultat").textContent = 'Vennligst oppgi gyldige mål for bredde og høyde.';
                return;
            }
            areal = bredde * hoyde;
            forklaringNorsk = `Arealet av et rektangel er bredde * høyde.`;
            forklaringEngelsk = `The area of a rectangle is width * height.`;
            break;
        case "trekant":
            const grunnlinje = parseFloat(document.getElementById("grunnlinje").value);
            const hoydeT = parseFloat(document.getElementById("hoyde").value);
            if (isNaN(grunnlinje) || isNaN(hoydeT)) {
                document.getElementById("resultat").textContent = 'Vennligst oppgi gyldige mål for grunnlinje og høyde.';
                return;
            }
            areal = (grunnlinje * hoydeT) / 2;
            forklaringNorsk = `Arealet av en trekant er (grunnlinje * høyde) / 2.`;
            forklaringEngelsk = `The area of a triangle is (base * height) / 2.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Arealet er: ${areal.toFixed(2)} kvadratmeter.`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for omkretsberegning
// Functions for calculating circumference
function beregnOmkrets() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn Omkrets</h3