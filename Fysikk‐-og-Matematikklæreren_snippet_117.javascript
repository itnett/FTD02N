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
            areal = Math.PI * radius ** 2;
            forklaringNorsk = `Arealet av en sirkel er π * radius^2.`;
            forklaringEngelsk = `The area of a circle is π * radius squared.`;
            break;
        case "rektangel":
            const bredde = parseFloat(document.getElementById("bredde").value);
            const hoyde = parseFloat(document.getElementById("hoyde").value);
            areal = bredde * hoyde;
            forklaringNorsk = `Arealet av et rektangel er bredde * høyde.`;
            forklaringEngelsk = `The area of a rectangle is width * height.`;
            break;
        case "trekant":
            const grunnlinje = parseFloat(document.getElementById("grunnlinje").value);
            const hoydeT = parseFloat(document.getElementById("hoyde").value);
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
        <h3>Beregn Omkrets</h3>
        <label for="figur">Velg figur:</label>
        <select id="figur">
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
            <option value="trekant">Trekant</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtOmkrets()">Beregn</button>
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
                    <input type="number" id="side1" placeholder="Side 1">
                    <input type="number" id="side2" placeholder="Side 2">
                    <input type="number" id="side3" placeholder="Side 3">
                `;
                break;
            default:
                inputFeltDiv.innerHTML = "";
        }
    });
}

function regnUtOmkrets() {
    const figur = document.getElementById("figur").value;
    let omkrets;
    let forklaringNorsk, forklaringEngelsk;

    switch (figur) {
        case "sirkel":
            const radius = parseFloat(document.getElementById("radius").value);
            omkrets = 2 * Math.PI * radius;
            forklaringNorsk = `Omkretsen av en sirkel er 2 * π * radius.`;
            forklaringEngelsk = `The circumference of a circle is 2 * π * radius.`;
            break;
        case "rektangel":
            const bredde = parseFloat(document.getElementById("bredde").value);
            const hoyde = parseFloat(document.getElementById("hoyde").value);
            omkrets = 2 * (bredde + hoyde);
            forklaringNorsk = `Omkretsen av et rektangel er 2 * (bredde + høyde).`;
            forklaringEngelsk = `The circumference of a rectangle is 2 * (width + height).`;
            break;
        case "trekant":
            const side1 = parseFloat(document.getElementById("side1").value);
            const side2 = parseFloat(document.getElementById("side2").value);
            const side3 = parseFloat(document.getElementById("side3").value);
            omkrets = side1 + side2 + side3;
            forklaringNorsk = `Omkretsen av en trekant er summen av alle sidene.`;
            forklaringEngelsk = `The circumference of a triangle is the sum of all sides.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Omkretsen er: ${omkrets.toFixed(2)} meter.`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for volumberegning
// Functions for calculating volume
function beregnVolum() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn Volum</h3>
        <label for="figur">Velg figur:</label>
        <select id="figur">
            <option value="kule">Kule</option>
            <option value="kube">Kube</option>
            <option value="sylinder">Sylinder</option>
            <option value="kjegle">Kjegle</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtVolum()">Beregn</button

Absolutely! Here is the complete content for the `trigonometri_geometri_modul.js` file, covering all the specified topics with explanations, calculations, and visualizations: