// algebra_modul.js

function algebra_meny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Algebra</h2>
        <button onclick="regneregler()">Regneregler</button>
        <button onclick="brok_og_prosentregning()">Brøk og prosentregning</button>
        <button onclick="potenser()">Potenser</button>
        <button onclick="tall_pa_standardform()">Tall på standardform</button>
        <button onclick="sammentrekning_og_faktorisering()">Sammentrekning og faktorisering</button>
        <button onclick="los_forstegradslikning()">Løs likninger av første grad</button>
        <button onclick="los_andregradslikning()">Løs likninger av andre grad</button>
        <button onclick="los_likningssett()">Løs likningssett med to ukjente</button>
        <button onclick="tilpasse_og_omforme_formler()">Tilpasse og omforme formeluttrykk</button>
    `;
}

// Regneregler
function regneregler() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Regneregler</h2>
        <input type="number" id="tall1" placeholder="Tall 1">
        <select id="operator">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" id="tall2" placeholder="Tall 2">
        <button onclick="regnUtRegneregler()">Beregn</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function regnUtRegneregler() {
    const tall1 = parseFloat(document.getElementById("tall1").value);
    const tall2 = parseFloat(document.getElementById("tall2").value);
    const operator = document.getElementById("operator").value;

    let resultat;
    switch (operator) {
        case "+":
            resultat = tall1 + tall2;
            break;
        case "-":
            resultat = tall1 - tall2;
            break;
        case "*":
            resultat = tall1 * tall2;
            break;
        case "/":
            if (tall2 !== 0) {
                resultat = tall1 / tall2;
            } else {
                alert("Kan ikke dele med null.");
                return;
            }
            break;
        default:
            alert("Ugyldig operator.");
            return;
    }

    document.getElementById("resultat").textContent = `${tall1} ${operator} ${tall2} = ${resultat}`;

    // Forklaring (norsk og engelsk)
    const forklaringNorsk = `
        Dette er en enkel regneoperasjon. Operatoren "${operator}" angir hvilken regneoperasjon som skal utføres.
    `;

    const forklaringEngelsk = `
        This is a simple arithmetic operation. The operator "${operator}" indicates which operation to perform.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Brøk og prosentregning
function brok_og_prosentregning() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Brøk og prosentregning</h2>
        <button onclick="addere_broker()">Addisjon av brøker</button>
        <button onclick="subtrahere_broker()">Subtraksjon av brøker</button>
        <button onclick="multiplisere_broker()">Multiplikasjon av brøker</button>
        <button onclick="dividere_broker()">Divisjon av brøker</button>
        <button onclick="konverter_brok_desimal()">Konvertering mellom brøk og desimaltall</button>
        <button onclick="beregn_prosent()">Beregning av prosent</button>
        <button onclick="beregn_prosentvis_endring()">Beregning av prosentvis økning/reduksjon</button>
        <div id="brokInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function addere_broker() {
    const brokInputDiv = document.getElementById("brokInput");
    brokInputDiv.innerHTML = `
        <h3>Addisjon av brøker</h3>
        <input type="number" id="teller1" placeholder="Teller 1"> / <input type="number" id="nevner1" placeholder="Nevner 1 (ikke 0)">
        <br>
        <input type="number" id="teller2" placeholder="Teller 2"> / <input type="number" id="nevner2" placeholder="Nevner 2 (ikke 0)">
        <br>
        <button onclick="regnUtBrokAddisjon()">Beregn</button>
    `;
}

// ... (Resten av funksjonene for brøk og prosentregning, potenser, standardform, sammentrekning og faktorisering, etc.)