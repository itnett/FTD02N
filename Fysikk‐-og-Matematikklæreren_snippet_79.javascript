// fysikk_modul.js

function fysikk_meny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="innledendeFysikk()">Innledende fysikk</button>
        <button onclick="kraftOgRettlinjetBevegelse()">Kraft og rettlinjet bevegelse</button>
        <button onclick="energi()">Energi</button>
        <button onclick="termodynamikkensForsteLov()">Termodynamikkens første lov</button>
        <button onclick="byggHovedmeny()">Tilbake til hovedmenyen</button>
        <div id="fysikkInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Innledende fysikk
function innledendeFysikk() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Innledende fysikk</h3>
        <button onclick="siSystemOgPrefikser()">SI-systemet og dekadiske prefikser</button>
        <button onclick="masseTyngdeTetthet()">Masse, tyngde og massetetthet</button>
        <button onclick="usikkerhetOgGjeldendeSiffer()">Usikkerhet og korrekt bruk av gjeldende siffer</button>
    `;
}

function siSystemOgPrefikser() {
    // ... (implementasjon for SI-systemet og prefikser, som i forrige svar)
}

function masseTyngdeTetthet() {
    // ... (implementasjon for masse, tyngde og massetetthet, som i forrige svar)
}

function usikkerhetOgGjeldendeSiffer() {
    // ... (implementasjon for usikkerhet og gjeldende siffer)
}

// Kraft og rettlinjet bevegelse
function kraftOgRettlinjetBevegelse() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Kraft og rettlinjet bevegelse</h3>
        <button onclick="newtonsLover()">Newtons lover</button>
        <button onclick="bevegelseslikningerKonstantFart()">Bevegelseslikninger (konstant fart)</button>
        <button onclick="bevegelseslikningerKonstantAkselerasjon()">Bevegelseslikninger (konstant akselerasjon)</button>
    `;
}

function newtonsLover() {
    // ... (implementasjon for Newtons lover)
}

function bevegelseslikningerKonstantFart() {
    // ... (implementasjon for bevegelseslikninger med konstant fart)
}

function bevegelseslikningerKonstantAkselerasjon() {
    // ... (implementasjon for bevegelseslikninger med konstant akselerasjon, som i forrige svar)
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
    // ... (implementasjon for å beregne arbeid)
}

function beregnEffekt() {
    // ... (implementasjon for å beregne effekt)
}

function beregnVirkningsgrad() {
    // ... (implementasjon for å beregne virkningsgrad)
}

function beregnKinetiskEnergi() {
    // ... (implementasjon for å beregne kinetisk energi)
}

function beregnPotensiellEnergi() {
    // ... (implementasjon for å beregne potensiell energi)
}

function anvendEnergibevaring() {
    // ... (implementasjon for å anvende energibevaring)
}

// Termodynamikkens første lov
function termodynamikkensForsteLov() {
    // ... (implementasjon for termodynamikkens første lov)
}