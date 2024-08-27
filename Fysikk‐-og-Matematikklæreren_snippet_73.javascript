// algebra_modul.js

function algebra_meny() {
    // ... (samme som før)
}

// Regneregler
function regneregler() {
    // ... (samme som før)
}

function regnUtRegneregler() {
    // ... (samme som før)
}

// Brøk og prosentregning
function brok_og_prosentregning() {
    // ... (samme som før)
}

function addere_broker() {
    // ... (samme som før)
}

function subtrahere_broker() {
    // ... (samme som før, men med subtraksjon i stedet for addisjon)
}

function multiplisere_broker() {
    // ... (samme som før, men med multiplikasjon i stedet for addisjon)
}

function dividere_broker() {
    // ... (samme som før, men med divisjon i stedet for addisjon)
}

function konverter_brok_desimal() {
    // ... (samme som før)
}

function beregn_prosent() {
    // ... (samme som før)
}

function beregn_prosentvis_endring() {
    // ... (samme som før)
}

// Potenser
function potenser() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h3>Potenser</h3>
        <input type="number" id="grunnTall" placeholder="Grunntall">
        <input type="number" id="eksponent" placeholder="Eksponent">
        <button onclick="regnUtPotens()">Beregn</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function regnUtPotens() {
    const grunnTall = parseFloat(document.getElementById("grunnTall").value);
    const eksponent = parseFloat(document.getElementById("eksponent").value);

    const resultat = Math.pow(grunnTall, eksponent);
    document.getElementById("resultat").textContent = `${grunnTall}^${eksponent} = ${resultat}`;

    const forklaringNorsk = `
        En potens er en måte å skrive gjentatt multiplikasjon på. Grunntallet er tallet som multipliseres med seg selv, 
        og eksponenten angir hvor mange ganger det skal multipliseres.
    `;

    const forklaringEngelsk = `
        A power is a way of writing repeated multiplication. The base is the number that is multiplied by itself, 
        and the exponent indicates how many times it should be multiplied.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Tall på standardform
function tall_pa_standardform() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h3>Tall på standardform</h3>
        <input type="number" id="tall" placeholder="Skriv inn et tall">
        <button onclick="konverterTilStandardform()">Konverter</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function konverterTilStandardform() {
    const tall = parseFloat(document.getElementById("tall").value);
    const standardform = tall.toExponential(2); // 2 desimaler
    document.getElementById("resultat").textContent = `${tall} på standardform er: ${standardform}`;

    const forklaringNorsk = `
        Standardform, også kjent som vitenskapelig notasjon, er en måte å skrive veldig store eller veldig små tall på. 
        Det består av et tall mellom 1 og 10 multiplisert med 10 opphøyd i en eksponent.
    `;

    const forklaringEngelsk = `
        Scientific notation, also known as standard form, is a way of writing very large or very small numbers. 
        It consists of a number between 1 and 10 multiplied by 10 raised to an exponent.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Sammentrekning og faktorisering
function sammentrekning_og_faktorisering() {
    // ... (samme som før)
}

// Likninger og formelregning
function los_forstegradslikning() {
    // ... (samme som før)
}

function los_andregradslikning() {
    // ... (samme som før)
}

function los_likningssett() {
    // ... (samme som før)
}

function tilpasse_og_omforme_formler() {
    // ... (samme som før)
}