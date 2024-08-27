function trigonometri_og_geometri() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Trigonometri og Geometri</h2>
        <button onclick="beregn_areal()">Beregn areal av ulike figurer</button>
        <button onclick="beregn_omkrets()">Beregn omkrets av ulike figurer</button>
        <button onclick="beregn_volum()">Beregn volum av ulike figurer</button>
        <button onclick="beregn_overflate()">Beregn overflate av ulike figurer</button>
        <button onclick="pythagoras()">Pythagoras' setning</button>
        <button onclick="trigonometri()">Trigonometri i rettvinklede trekanter</button>
       

 <button onclick="vektorer()">Vektorer i planet</button>
        <button onclick="byggMatematikkMeny()">Tilbake til matematikkmenyen</button>
        <div id="trigGeomInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function beregn_areal() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn areal</h3>
        <select id="figur">
            <option value="trekant">Trekant</option>
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
            <option value="parallellogram">Parallellogram</option>
            <option value="trapes">Trapes</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtAreal()">Beregn</button>
    `;

    document.getElementById("figur").addEventListener("change", function() {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");

        switch (figur) {
            case "trekant":
            case "parallellogram":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="grunnlinje" placeholder="Grunnlinje">
                    <input type="number" id="hoyde" placeholder="Høyde">
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
            case "trapes":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="a" placeholder="Side a">
                    <input type="number" id="b" placeholder="Side b">
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
        case "trekant":
            const grunnlinje = parseFloat(document.getElementById("grunnlinje").value);
            const hoyde = parseFloat(document.getElementById("hoyde").value);
            areal = 0.5 * grunnlinje * hoyde;
            forklaringNorsk = `Arealet av en trekant er halvparten av grunnlinjen multiplisert med høyden.`;
            forklaringEngelsk = `The area of a triangle is half the base multiplied by the height.`;
            break;
        case "sirkel":
            const radius = parseFloat(document.getElementById("radius").value);
            areal = Math.PI * radius**2;
            forklaringNorsk = `Arealet av en sirkel er pi (π) multiplisert med radius kvadrert.`;
            forklaringEngelsk = `The area of a circle is pi (π) multiplied by the radius squared.`;
            break;
        case "rektangel":
            const lengde = parseFloat(document.getElementById("lengde").value);
            const bredde = parseFloat(document.getElementById("bredde").value);
            areal = lengde * bredde;
            forklaringNorsk = `Arealet av et rektangel er lengden multiplisert med bredden.`;
            forklaringEngelsk = `The area of a rectangle is the length multiplied by the width.`;
            break;
        case "parallellogram":
            const grunnlinjeP = parseFloat(document.getElementById("grunnlinje").value);
            const hoydeP = parseFloat(document.getElementById("hoyde").value);
            areal = grunnlinjeP * hoydeP;
            forklaringNorsk = `Arealet av et parallellogram er grunnlinjen multiplisert med høyden.`;
            forklaringEngelsk = `The area of a parallelogram is the base multiplied by the height.`;
            break;
        case "trapes":
            const a = parseFloat(document.getElementById("a").value);
            const b = parseFloat(document.getElementById("b").value);
            const hoydeT = parseFloat(document.getElementById("hoyde").value);
            areal = 0.5 * (a + b) * hoydeT;
            forklaringNorsk = `Arealet av et trapes er gjennomsnittet av de parallelle sidene multiplisert med høyden.`;
            forklaringEngelsk = `The area of a trapezoid is the average of the parallel sides multiplied by the height.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Arealet er: ${areal.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}