// ... (tidligere kode for areal, omkrets, volum og overflate)

function pythagoras() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Pythagoras' setning (a² + b² = c²)</h3>
        <select id="pythagorasValg">
            <option value="hypotenus">Finn hypotenus (c)</option>
            <option value="katet">Finn katet (a eller b)</option>
        </select>
        <div id="pythagorasInput"></div>
        <button onclick="regnUtPythagoras()">Beregn</button>
    `;

    document.getElementById("pythagorasValg").addEventListener("change", function() {
        const valg = this.value;
        const pythagorasInputDiv = document.getElementById("pythagorasInput");

        if (valg === "hypotenus") {
            pythagorasInputDiv.innerHTML = `
                <input type="number" id="katet1" placeholder="Katet a">
                <input type="number" id="katet2" placeholder="Katet b">
            `;
        } else if (valg === "katet") {
            pythagorasInputDiv.innerHTML = `
                <input type="number" id="hypotenus" placeholder="Hypotenus (c)">
                <input type="number" id="kjentKatet" placeholder="Kjente katet (a eller b)">
            `;
        }
    });
}

function regnUtPythagoras() {
    const valg = document.getElementById("pythagorasValg").value;
    let resultat, forklaringNorsk, forklaringEngelsk;

    if (valg === "hypotenus") {
        const a = parseFloat(document.getElementById("katet1").value);
        const b = parseFloat(document.getElementById("katet2").value);
        resultat = Math.sqrt(a**2 + b**2);
        forklaringNorsk = `Hypotenusen (c) er roten av summen av kvadratene av katetene a og b.`;
        forklaringEngelsk = `The hypotenuse (c) is the square root of the sum of the squares of the legs a and b.`;
    } else if (valg === "katet") {
        const c = parseFloat(document.getElementById("hypotenus").value);
        const kjentKatet = parseFloat(document.getElementById("kjentKatet").value);
        resultat = Math.sqrt(c**2 - kjentKatet**2);
        forklaringNorsk = `Den ukjente kateten er roten av differansen mellom kvadratet av hypotenusen og kvadratet av den kjente kateten.`;
        forklaringEngelsk = `The unknown leg is the square root of the difference between the square of the hypotenuse and the square of the known leg.`;
    }

    document.getElementById("resultat").textContent = `Resultat: ${resultat.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function trigonometri() {
    // ... (implementasjon for trigonometri i rettvinklede trekanter)
}

function vektorer() {
    // ... (implementasjon for vektorer i planet)
}