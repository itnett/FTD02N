// trigonometri_geometri_modul.js

function trigonometri_og_geometri() {
    // ... (samme som før)
}

// Arealberegning
function beregn_areal() {
    // ... (samme som før)
}

function regnUtAreal() {
    // ... (samme som før)
}

// Omkretsberegning
function beregn_omkrets() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn omkrets</h3>
        <select id="figur">
            <option value="trekant">Trekant</option>
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtOmkrets()">Beregn</button>
    `;

    // Event listener for å oppdatere inputfelt basert på valgt figur
    document.getElementById("figur").addEventListener("change", function() {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");
        
        switch (figur) {
            case "trekant":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="side1" placeholder="Side 1">
                    <input type="number" id="side2" placeholder="Side 2">
                    <input type="number" id="side3" placeholder="Side 3">
                `;
                break;
            case "sirkel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "rektangel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="lengde" placeholder="Lengde">
                    <input type="number" id="bredde" placeholder="Bredde">
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
        case "trekant":
            const side1 = parseFloat(document.getElementById("side1").value);
            const side2 = parseFloat(document.getElementById("side2").value);
            const side3 = parseFloat(document.getElementById("side3").value);
            omkrets = side1 + side2