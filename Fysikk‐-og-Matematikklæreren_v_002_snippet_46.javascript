function trigonometryGeometryMenu() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Trigonometri og Geometri</h2>
        <button onclick="calculateArea()">Beregn areal av ulike figurer</button>
        <button onclick="calculatePerimeter()">Beregn omkrets av ulike figurer</button>
        <button onclick="calculateVolume()">Beregn volum av ulike figurer</button>
        <button onclick="calculateSurfaceArea()">Beregn overflate av ulike figurer</button>
        <button onclick="pythagoras()">Pythagoras' setning</button>
        <button onclick="trigonometry()">Trigonometri i rettvinklede trekanter</button>
        <button onclick="vectors()">Vektorer i planet</button>
        <button onclick="buildMathMenu()">Tilbake til matematikkmenyen</button>
        <div id="trigGeomInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function calculateArea() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn areal</h3>
        <select id="shape">
            <option value="triangle">Trekant</option>
            <option value="circle">Sirkel</option>
            <option value="rectangle">Rektangel</option>
            <option value="parallelogram">Parallellogram</option>
            <option value="trapezoid">Trapes</option>
        </select>
        <div id="inputFields"></div>
        <button onclick="calculateShapeArea()">Beregn</button>
        <button class="generateCodeButton" data-topic="area">Generer kode</button>
    `;

    document.getElementById("shape").addEventListener("change", function() {
        const shape = this.value;
        const inputFieldsDiv = document.getElementById("inputFields");

        switch (shape) {
            case "triangle":
            case "parallelogram":
                inputFieldsDiv.innerHTML = `
                    <input type="number" id="base" placeholder="Grunnlinje">
                    <input type="number" id="height" placeholder="Høyde">
                `;
                break;
            case "circle":
                inputFieldsDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "rectangle":
                inputFieldsDiv.innerHTML = `
                    <input type="number" id="length" placeholder="Lengde">
                    <input type="number" id="width" placeholder="Bredde">
                `;
                break;
            case "trapezoid":
                inputFieldsDiv.innerHTML = `
                    <input type="number" id="a" placeholder="Side a">
                    <input type="number" id="b" placeholder="Side b">
                    <input type="number" id="height" placeholder="Høyde">
                `;
                break;
            default:
                inputFieldsDiv.innerHTML = "";
        }
    });
}

function calculateShapeArea() {
    const shape = document.getElementById("shape").value;
    let area;
    let forklaringNorsk, forklaringEngelsk;

    switch (shape) {
        case "triangle":
            const base = parseFloat(document.getElementById("base").value);
            const height = parseFloat(document.getElementById("height").value);
            area = 0.5 * base * height;
            forklaringNorsk = `Arealet av en trekant er halvparten av grunnlinjen multiplisert med høyden.`;
            forklaringEngelsk = `The area of a triangle is half the base multiplied by the height.`;
            break;
        case "circle":
            const radius = parseFloat(document.getElementById("radius").value);
            area = Math.PI * radius**2;
            forklaringNorsk = `Arealet av en sirkel er pi (π) multiplisert med radius kvadrert.`;
            forklaringEngelsk = `The area of a circle is pi (π) multiplied by the radius squared.`;
            break;
        case "rectangle":
            const length = parseFloat(document.getElementById("length").value);
            const width = parseFloat(document.getElementById("width").value);
            area = length * width;
            forklaringNorsk = `Arealet av et rektangel er lengden multiplisert med bredden.`;
            forklaringEngelsk = `The area of a rectangle is the length multiplied by the width.`;
            break;
        case "parallelogram":
            const baseP = parseFloat(document.getElementById("base").value);
            const heightP = parseFloat(document.getElementById("height").value);
            area = baseP * heightP;
            forklaringNorsk = `Arealet av et parallellogram er grunnlinjen multiplisert med høyden.`;
            forklaringEngelsk = `The area of a parallelogram is the base multiplied by the height.`;
            break;
        case "trapezoid":
            const a = parseFloat(document.getElementById("a").value);
            const b = parseFloat(document.getElementById("b").value);
            const heightT = parseFloat(document.getElementById("height").value);
            area = 0.5 * (a + b) * heightT;
            forklaringNorsk = `Arealet av et trapes er gjennomsnittet av de parallelle sidene multiplisert med høyden.`;
            forklaringEngelsk = `The area of a trapezoid is the average of the parallel sides multiplied by the height.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Arealet er: ${area.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}