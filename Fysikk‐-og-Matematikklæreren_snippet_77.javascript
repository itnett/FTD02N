// trigonometri_geometri_modul.js

function trigonometri_og_geometri() {
    // ... (samme meny-funksjon som i forrige svar)
}

// ... (funksjoner for areal, omkrets, volum og overflate)

function pythagoras() {
    // ... (samme som i forrige svar)
}

function regnUtPythagoras() {
    // ... (samme som i forrige svar)
}

function trigonometri() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Trigonometri i rettvinklede trekanter</h3>
        <select id="trigValg">
            <option value="sinus">Finn sinus (sin)</option>
            <option value="cosinus">Finn cosinus (cos)</option>
            <option value="tangens">Finn tangens (tan)</option>
        </select>
        <div id="trigInput"></div>
        <button onclick="regnUtTrigonometri()">Beregn</button>
    `;

    document.getElementById("trigValg").addEventListener("change", function() {
        const valg = this.value;
        const trigInputDiv = document.getElementById("trigInput");

        if (valg === "sinus") {
            trigInputDiv.innerHTML = `
                <input type="number" id="motstående" placeholder="Motstående katet">
                <input type="number" id="hypotenus" placeholder="Hypotenus">
            `;
        } else if (valg === "cosinus") {
            trigInputDiv.innerHTML = `
                <input type="number" id="hosliggende" placeholder="Hosliggende katet">
                <input type="number" id="hypotenus" placeholder="Hypotenus">
            `;
        } else if (valg === "tangens") {
            trigInputDiv.innerHTML = `
                <input type="number" id="motstående" placeholder="Motstående katet">
                <input type="number" id="hosliggende" placeholder="Hosliggende katet">
            `;
        }
    });
}

function regnUtTrigonometri() {
    const valg = document.getElementById("trigValg").value;
    let resultat, forklaringNorsk, forklaringEngelsk;

    switch (valg) {
        case "sinus":
            const motstående = parseFloat(document.getElementById("motstående").value);
            const hypotenusSin = parseFloat(document.getElementById("hypotenus").value);
            resultat = Math.sin(motstående / hypotenusSin);
            forklaringNorsk = `Sinus til en vinkel i en rettvinklet trekant er forholdet mellom motstående katet og hypotenusen.`;
            forklaringEngelsk = `The sine of an angle in a right triangle is the ratio of the opposite side to the hypotenuse.`;
            break;
        case "cosinus":
            const hosliggende = parseFloat(document.getElementById("hosliggende").value);
            const hypotenusCos = parseFloat(document.getElementById("hypotenus").value);
            resultat = Math.cos(hosliggende / hypotenusCos);
            forklaringNorsk = `Cosinus til en vinkel i en rettvinklet trekant er forholdet mellom hosliggende katet og hypotenusen.`;
            forklaringEngelsk = `The cosine of an angle in a right triangle is the ratio of the adjacent side to the hypotenuse.`;
            break;
        case "tangens":
            const motståendeTan = parseFloat(document.getElementById("motstående").value);
            const hosliggendeTan = parseFloat(document.getElementById("hosliggende").value);
            resultat = Math.tan(motståendeTan / hosliggendeTan);
            forklaringNorsk = `Tangens til en vinkel i en rettvinklet trekant er forholdet mellom motstående katet og hosliggende katet.`;
            forklaringEngelsk = `The tangent of an angle in a right triangle is the ratio of the opposite side to the adjacent side.`;
            break;
        default:
            alert("Ugyldig valg.");
            return;
    }

    document.getElementById("resultat").textContent = `Resultat: ${resultat.toFixed(4)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function vektorer() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Vektorer i planet</h3>
        <input type="number" id="x1" placeholder="x1">
        <input type="number" id="y1" placeholder="y1">
        <input type="number" id="x2" placeholder="x2">
        <input type="number" id="y2" placeholder="y2">
        <button onclick="regnUtVektorer()">Beregn</button>
    `;
}

function regnUtVektorer() {
    const x1 = parseFloat(document.getElementById("x1").value);
    const y1 = parseFloat(document.getElementById("y1").value);
    const x2 = parseFloat(document.getElementById("x2").value);
    const y2 = parseFloat(document.getElementById("y2").value);

    const vektor1 = [x1, y1];
    const vektor2 = [x2, y2];

    // Beregn lengde av vektorer
    const lengde1 = Math.sqrt(x1**2 + y1**2);
    const lengde2 = Math.sqrt(x2**2 + y2**2);

    // Beregn prikkprodukt
    const prikkprodukt = x1*x2 + y1*y2;

    // Beregn vinkel mellom vektorer
    const vinkelRad = Math.acos(prikkprodukt / (lengde1 * lengde2));
    const vinkelDeg = vinkelRad * 180 / Math.PI;

    document.getElementById("resultat").textContent = `
        Lengde av vektor 1: ${lengde1.toFixed(2)}
        Lengde av vektor 2: ${lengde2.toFixed(2)}
        Prikkprodukt: ${prikkprodukt.toFixed(2)}
        Vinkel mellom vektorene: ${vinkelDeg.toFixed(2)} grader
    `;

    const forklaringNorsk = `
        Lengden av en vektor er beregnet ved hjelp av Pythagoras' setning. 
        Prikkproduktet av to vektorer er summen av produktene av deres tilsvarende komponenter. 
        Vinkelen mellom to vektorer kan beregnes ved hjelp av prikkproduktet og lengdene av vektorene.
    `;

    const forklaringEngelsk = `
        The length of a vector is calculated using the Pythagorean theorem. 
        The dot product of two vectors is the sum of the products of their corresponding components. 
        The angle between two vectors can be calculated using the dot product and the lengths of the vectors.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}