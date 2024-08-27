// trigonometri_geometri_modul.js

function trigonometri_og_geometri() {
    // ... (samme meny-funksjon som i forrige svar)
}

function beregn_areal() {
    // ... (samme som i forrige svar)
}

function regnUtAreal() {
    // ... (samme som i forrige svar)
}

function beregn_omkrets() {
    // ... (samme som i forrige svar, men legg til flere figurer)
        case "parallellogram":
            const grunnlinjeP = parseFloat(document.getElementById("grunnlinje").value);
            const sidelengdeP = parseFloat(document.getElementById("sidelengde").value);
            omkrets = 2 * (grunnlinjeP + sidelengdeP);
            forklaringNorsk = `Omkretsen av et parallellogram er to ganger summen av grunnlinjen og sidelengden.`;
            forklaringEngelsk = `The perimeter of a parallelogram is twice the sum of the base and the side length.`;
            break;
        case "trapes":
            const a = parseFloat(document.getElementById("a").value);
            const b = parseFloat(document.getElementById("b").value);
            const c = parseFloat(document.getElementById("c").value);
            const d = parseFloat(document.getElementById("d").value);
            omkrets = a + b + c + d;
            forklaringNorsk = `Omkretsen av et trapes er summen av alle sidene.`;
            forklaringEngelsk = `The perimeter of a trapezoid is the sum of all its sides.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Omkretsen er: ${omkrets.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Beregn volum
function beregn_volum() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn volum</h3>
        <select id="figur">
            <option value="kule">Kule</option>
            <option value="kube">Kube</option>
            <option value="sylindrisk">Sylinder</option>
            <option value="kjegle">Kjegle</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtVolum()">Beregn</button>
    `;
    document.getElementById("figur").addEventListener("change", function () {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");

        switch (figur) {
            case "kule":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "kube":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="sidelengde" placeholder="Sidelengde">
                `;
                break;
            case "sylindrisk":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            case "kjegle":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            default:
                inputFeltDiv.innerHTML = "";
        }
    });
}

function regnUtVolum() {
    const figur = document.getElementById("figur").value;
    let volum;
    let forklaringNorsk, forklaringEngelsk;

    switch (figur) {
        case "kule":
            const radius = parseFloat(document.getElementById("radius").value);
            volum = (4 / 3) * Math.PI * radius ** 3;
            forklaringNorsk = `Volumet av en kule er (4/3) * pi (π) * radius i tredje.`;
            forklaringEngelsk = `The volume of a sphere is (4/3) * pi (π) * radius cubed.`;
            break;
        case "kube":
            const sidelengde = parseFloat(document.getElementById("sidelengde").value);
            volum = sidelengde ** 3;
            forklaringNorsk = `Volumet av en kube er sidelengden opphøyd i tredje.`;
            forklaringEngelsk = `The volume of a cube is the side length cubed.`;
            break;
        case "sylindrisk":
            const radiusS = parseFloat(document.getElementById("radius").value);
            const hoydeS = parseFloat(document.getElementById("hoyde").value);
            volum = Math.PI * radiusS ** 2 * hoydeS;
            forklaringNorsk = `Volumet av en sylinder er pi (π) * radius kvadrert * høyden.`;
            forklaringEngelsk = `The volume of a cylinder is pi (π) * radius squared * height.`;
            break;
        case "kjegle":
            const radiusK = parseFloat(document.getElementById("radius").value);
            const hoydeK = parseFloat(document.getElementById("hoyde").value);
            volum = (1 / 3) * Math.PI * radiusK ** 2 * hoydeK;
            forklaringNorsk = `Volumet av en kjegle er (1/3) * pi (π) * radius kvadrert * høyden.`;
            forklaringEngelsk = `The volume of a cone is (1/3) * pi (π) * radius squared * height.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Volumet er: ${volum.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Beregn overflate
function beregn_overflate() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn overflate</h3>
        <select id="figur">
            <option value="kule">Kule</option>
            <option value="kube">Kube</option>
            <option value="sylindrisk">Sylinder</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtOverflate()">Beregn</button>
    `;

    document.getElementById("figur").addEventListener("change", function () {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");

        switch (figur) {
            case "kule":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "kube":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="sidelengde" placeholder="Sidelengde">
                `;
                break;
            case "sylindrisk":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            default:
                inputFeltDiv.innerHTML = "";
        }
    });
}

function regnUtOverflate() {
    const figur = document.getElementById("figur").value;
    let overflate;
    let forklaringNorsk, forklaringEngelsk;

    switch (figur) {
        case "kule":
            const radius = parseFloat(document.getElementById("radius").value);
            overflate = 4 * Math.PI * radius ** 2;
            forklaringNorsk = `Overflaten av en kule er 4 * pi (π) * radius kvadrert.`;
            forklaringEngelsk = `The surface area of a sphere is 4 * pi (π) * radius squared.`;
            break;
        case "kube":
            const sidelengde = parseFloat(document.getElementById("sidelengde").value);
            overflate = 6 * sidelengde ** 2;
            forklaringNorsk = `Overflaten av en kube er 6 * sidelengden kvad