// ... (previous code for introductory physics)

function bevegelseslikningerKonstantAkselerasjon() {
    // ... (same implementation as in previous response)
}

// Energi
function energi() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Energi</h3>
        <button onclick="beregnArbeid()">Beregn arbeid</button>
        <button onclick="beregnEffekt()">Beregn effekt</button>
        <button onclick="beregnVirkningsgrad()">Beregn virkningsgrad</button>
        <button onclick="beregnKinetiskEnergi()">Beregn kinetisk energi</button>
        <button onclick="beregnPotensiellEnergi()">Beregn potensiell energi</button>
        <button onclick="anvendEnergibevaring()">Anvend energibevaring</button>
    `;
}

function beregnArbeid() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Beregn arbeid (W = F * s * cos θ)</h3>
        <input type="number" id="kraft" placeholder="Kraft (N)">
        <input type="number" id="forflytning" placeholder="Forflytning (m)">
        <input type="number" id="vinkel" placeholder="Vinkel (grader)">
        <button onclick="regnUtArbeid()">Beregn</button>
    `;
}

function regnUtArbeid() {
    const kraft = parseFloat(document.getElementById("kraft").value);
    const forflytning = parseFloat(document.getElementById("forflytning").value);
    const vinkel = parseFloat(document.getElementById("vinkel").value);

    const arbeid = kraft * forflytning * Math.cos(radians(vinkel));

    document.getElementById("resultat").textContent = `Arbeidet utført er: ${arbeid.toFixed(2)} J`;

    const forklaringNorsk = `
        Arbeid (W) er produktet av kraft (F), forflytning (s) og cosinus til vinkelen (θ) mellom kraft og forflytning.
    `;
    const forklaringEngelsk = `
        Work (W) is the product of force (F), displacement (s), and the cosine of the angle (θ) between the force and displacement.
    `;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function beregnEffekt() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Beregn effekt (P = W / t eller P = F * v)</h3>
        <select id="effektValg">
            <option value="arbeidTid">Arbeid og tid</option>
            <option value="kraftHastighet">Kraft og hastighet</option>
        </select>
        <div id="effektInput"></div>
        <button onclick="regnUtEffekt()">Beregn</button>
    `;

    document.getElementById("effektValg").addEventListener("change", function() {
        const valg = this.value;
        const effektInputDiv = document.getElementById("effektInput");

        if (valg === "arbeidTid") {
            effektInputDiv.innerHTML = `
                <input type="number" id="arbeid" placeholder="Arbeid (J)">
                <input type="number" id="tid" placeholder="Tid (s)">
            `;
        } else if (valg === "kraftHastighet") {
            effektInputDiv.innerHTML = `
                <input type="number" id="kraft" placeholder="Kraft (N)">
                <input type="number" id="hastighet" placeholder="Hastighet (m/s)">
            `;
        }
    });
}

function regnUtEffekt() {
    const valg = document.getElementById("effektValg").value;
    let effekt, forklaringNorsk, forklaringEngelsk;

    if (valg === "arbeidTid") {
        const arbeid = parseFloat(document.getElementById("arbeid").value);
        const tid = parseFloat(document.getElementById("tid").value);
        if (tid === 0) {
            alert("Tid kan ikke være 0.");
            return;
        }
        effekt = arbeid / tid;
        forklaringNorsk = `Effekt (P) er arbeid (W) delt på tid (t).`;
        forklaringEngelsk = `Power (P) is work (W) divided by time (t).`;
    } else if (valg === "kraftHastighet") {
        const kraft = parseFloat(document.getElementById("kraft").value);
        const hastighet = parseFloat(document.getElementById("hastighet").value);
        effekt = kraft * hastighet;
        forklaringNorsk = `Effekt (P) er kraft (F) multiplisert med hastighet (v).`;
        forklaringEngelsk = `Power (P) is force (F) multiplied by velocity (v).`;
    }

    document.getElementById("resultat").textContent = `Effekten er: ${effekt.toFixed(2)} W`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function beregnVirkningsgrad() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Beregn virkningsgrad (η = W_nyttig / W_tilført * 100%)</h3>
        <input type="number" id="w_nyttig" placeholder="Nyttig arbeid (J)">
        <input type="number" id="w_tilfort" placeholder="Tilført arbeid (J)">
        <button onclick="regnUtVirkningsgrad()">Beregn</button>
    `;
}

function regnUtVirkningsgrad() {
    const w_nyttig = parseFloat(document.getElementById("w_nyttig").value);
    const w_tilfort = parseFloat(document.getElementById("w_tilfort").value);

    if (w_tilfort === 0) {
        alert("Tilført arbeid kan ikke være 0.");
        return;
    }

    const virkningsgrad = (w_nyttig / w_tilfort) * 100;
    document.getElementById("resultat").textContent = `Virkningsgraden er: ${virkningsgrad.toFixed(2)}%`;

    const forklaringNorsk = `
        Virkningsgrad (η) er forholdet mellom nyttig arbeid (W_nyttig) og tilført arbeid (W_tilført), uttrykt i prosent.
    `;
    const forklaringEngelsk = `
        Efficiency (η) is the ratio of useful work (W_nyttig) to the energy input (W_tilført), expressed as a percentage.
    `;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function beregnKinetiskEnergi() {
    // ... (samme som i forrige svar)
}

function beregnPotensiellEnergi() {
    // ... (samme som i forrige svar)
}

function anvendEnergibevaring() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Anvend energibevaring</h3>
        <p>Velg et scenario:</p>
        <select id="energibevaringScenario">
            <option value="frittFall">Fritt fall</option>
            <option value="pendel">Pendel</option>
            </select>
        <div id="energibevaringInput"></div>
        <button onclick="regnUtEnergibevaring()">Beregn</button>
    `;

    document.getElementById("energibevaringScenario").addEventListener("change", function() {
        const valg = this.value;
        const energibevaringInputDiv = document.getElementById("energibevaringInput");

        if (valg === "frittFall") {
            energibevaringInputDiv.innerHTML = `
                <input type="number" id="masse" placeholder="Masse (kg)">
                <input type="number" id="hoyde" placeholder="Høyde (m)">
            `;
        } else if (valg === "pendel") {
            energibevaringInputDiv.innerHTML = `
                <input type="number" id="masse" placeholder="Masse (kg)">
                <input type="number" id="lengde" placeholder="Lengde (m)">
                <input type="number"