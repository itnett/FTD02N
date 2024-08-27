// Bygger menyen for fysikk
function fysikk_meny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="innledendeFysikk()">Innledende fysikk</button>
        <button onclick="kraftOgRettlinjetBevegelse()">Kraft og rettlinjet bevegelse</button>
        <button onclick="energiOgArbeid()">Energi og arbeid</button>
        <button onclick="termodynamikk()">Termodynamikk</button>
        <button onclick="byggHovedmeny()">Tilbake til hovedmenyen</button>
        <div id="fysikkInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Funksjoner for innledende fysikk
function innledendeFysikk() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Innledende fysikk</h3>
        <p>Velg et tema for å lære mer.</p>
        <button onclick="kraft()">Kraft</button>
        <button onclick="bevegelse()">Bevegelse</button>
        <button onclick="energi()">Energi</button>
        <button onclick="arbeid()">Arbeid</button>
    `;
}

// Funksjoner for kraft og rettlinjet bevegelse
function kraftOgRettlinjetBevegelse() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Kraft og rettlinjet bevegelse</h3>
        <button onclick="newtonsForsteLov()">Newtons første lov</button>
        <button onclick="newtonsAndreLov()">Newtons andre lov</button>
        <button onclick="newtonsTredjeLov()">Newtons tredje lov</button>
    `;
}

function newtonsForsteLov() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Newtons første lov</h3>
        <p>Newtons første lov, også kjent som treghetsloven, sier at et legeme vil forbli i ro eller i konstant bevegelse med mindre det påvirkes av en ekstern kraft.</p>
        <button onclick="kraftOgRettlinjetBevegelse()">Tilbake</button>
    `;
}

function newtonsAndreLov() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Newtons andre lov</h3>
        <p>Newtons andre lov sier at akselerasjonen av et legeme er proporsjonal med den påførte kraften og omvendt proporsjonal med massen av legemet.</p>
        <input type="number" id="kraft" placeholder="Kraft (N)">
        <input type="number" id="masse" placeholder="Masse (kg)">
        <button onclick="beregnAkselerasjon()">Beregn akselerasjon</button>
        <button onclick="kraftOgRettlinjetBevegelse()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function beregnAkselerasjon() {
    const kraft = parseFloat(document.getElementById("kraft").value);
    const masse = parseFloat(document.getElementById("masse").value);

    if (isNaN(kraft) || isNaN(masse) || masse <= 0) {
        alert("Vennligst fyll inn gyldige verdier for kraft og masse.");
        return;
    }

    const akselerasjon = kraft / masse;
    document.getElementById("resultat").textContent = `Akselerasjonen er: ${akselerasjon.toFixed(2)} m/s²`;

    const forklaringNorsk = `
        Newtons andre lov sier at akselerasjonen (a) av et legeme er lik den påførte kraften (F) delt på massen (m). 
        Akselerasjonen er derfor a = F / m. I dette tilfellet er akselerasjonen ${akselerasjon.toFixed(2)} m/s².
    `;

    const forklaringEngelsk = `
        Newton's second law states that the acceleration (a) of an object is equal to the applied force (F) divided by the mass (m). 
        Therefore, the acceleration is a = F / m. In this case, the acceleration is ${akselerasjon.toFixed(2)} m/s².
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function newtonsTredjeLov() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Newtons tredje lov</h3>
        <p>Newtons tredje lov sier at for hver kraft er det en like stor og motsatt rettet kraft.</p>
        <button onclick="kraftOgRettlinjetBevegelse()">Tilbake</button>
    `;
}

// Funksjoner for energi og arbeid
function energiOgArbeid() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Energi og arbeid</h3>
        <button onclick="potensiellEnergi()">Potensiell energi</button>
        <button onclick="kinetiskEnergi()">Kinetisk energi</button>
        <button onclick="arbeid()">Arbeid</button>
    `;
}

function potensiellEnergi() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Potensiell energi</h3>
        <input type="number" id="masse" placeholder="Masse (kg)">
        <input type="number" id="hoyde" placeholder="Høyde (m)">
        <button onclick="beregnPotensiellEnergi()">Beregn potensiell energi</button>
        <button onclick="energiOgArbeid()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function beregnPotensiellEnergi() {
    const masse = parseFloat(document.getElementById("masse").value);
    const hoyde = parseFloat(document.getElementById("hoyde").value);

    if (isNaN(masse) || isNaN(hoyde) || masse <= 0 || hoyde <= 0) {
        alert("Vennligst fyll inn gyldige verdier for masse og høyde.");
        return;
    }

    const gravitasjon = 9.81; // m/s²
    const potensiellEnergi = masse * gravitasjon * hoyde;
    document.getElementById("resultat").textContent = `Potensiell energi er: ${potensiellEnergi.toFixed(2)} J`;

    const forklaringNorsk = `
        Potensiell energi (Ep) er energien et legeme har på grunn av sin posisjon i et gravitasjonsfelt. 
        Den beregnes som Ep = mgh, hvor m er massen, g er gravitasjonsakselerasjonen (9,81 m/s²), og h er høyden. 
        I dette tilfellet er den potensielle energien ${potensiellEnergi.toFixed(2)} J (joule).
    `;

    const forklaringEngelsk = `
        Potential energy (Ep) is the energy an object has because of its position in a gravitational field. 
        It is calculated as Ep = mgh, where m is the mass, g is the gravitational acceleration (9.81 m/s²), and h is the height. 
        In this case, the potential energy is ${potensiellEnergi.toFixed(2)} J (joules).
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function kinetiskEnergi() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Kinetisk energi</h3>
        <input type="number" id="masse" placeholder="Masse (kg)">
        <input type="number" id="hastighet" placeholder="Hastighet (m/s)">
        <button onclick="beregnKinetiskEnergi()">Beregn kinetisk energi</button>
        <button onclick="energiOgArbeid()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;


}

function beregnKinetiskEnergi() {
    const masse = parseFloat(document.getElementById("masse").value);
    const hastighet = parseFloat(document.getElementById("hastighet").value);

    if (isNaN(masse) || isNaN(hastighet) || masse <= 0 || hastighet <= 0) {
        alert("Vennligst fyll inn gyldige verdier for masse og hastighet.");
        return;
    }

    const kinetiskEnergi = 0.5 * masse * hastighet ** 2;
    document.getElementById("resultat").textContent = `Kinetisk energi er: ${kinetiskEnergi.toFixed(2)} J`;

    const forklaringNorsk = `
        Kinetisk energi (Ek) er energien et legeme har på grunn av sin bevegelse. 
        Den beregnes som Ek = 0,5 * mv², hvor m er massen og v er hastigheten. 
        I dette tilfellet er den kinetiske energien ${kinetiskEnergi.toFixed(2)} J (joule).
    `;

    const forklaringEngelsk = `
        Kinetic energy (Ek) is the energy an object has due to its motion. 
        It is calculated as Ek = 0.5 * mv², where m is the mass and v is the velocity. 
        In this case, the kinetic energy is ${kinetiskEnergi.toFixed(2)} J (joules).
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function arbeid() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Arbeid</h3>
        <input type="number" id="kraft" placeholder="Kraft (N)">
        <input type="number" id="distanse" placeholder="Distanse (m)">
        <button onclick="beregnArbeid()">Beregn arbeid</button>
        <button onclick="energiOgArbeid()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function beregnArbeid() {
    const kraft = parseFloat(document.getElementById("kraft").value);
    const distanse = parseFloat(document.getElementById("distanse").value);

    if (isNaN(kraft) || isNaN(distanse) || kraft <= 0 || distanse <= 0) {
        alert("Vennligst fyll inn gyldige verdier for kraft og distanse.");
        return;
    }

    const arbeid = kraft * distanse;
    document.getElementById("resultat").textContent = `Arbeidet er: ${arbeid.toFixed(2)} J`;

    const forklaringNorsk = `
        Arbeid (W) er energien som overføres til eller fra et legeme via en kraft som får det til å bevege seg. 
        Det beregnes som W = Fd, hvor F er kraften og d er distansen. 
        I dette tilfellet er arbeidet ${arbeid.toFixed(2)} J (joule).
    `;

    const forklaringEngelsk = `
        Work (W) is the energy transferred to or from an object via a force causing it to move. 
        It is calculated as W = Fd, where F is the force and d is the distance. 
        In this case, the work is ${arbeid.toFixed(2)} J (joules).
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for termodynamikk
function termodynamikk() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Termodynamikk</h3>
        <button onclick="termodynamikkensForsteLov()">Termodynamikkens første lov</button>
        <button onclick="termodynamikkensAndreLov()">Termodynamikkens andre lov</button>
    `;
}

function termodynamikkensForsteLov() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Termodynamikkens første lov</h3>
        <p>Termodynamikkens første lov, også kjent som energibevaringsloven, sier at energi ikke kan skapes eller ødelegges, bare omdannes fra en form til en annen.</p>
        <button onclick="termodynamikk()">Tilbake</button>
    `;
}

function termodynamikkensAndreLov() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Termodynamikkens andre lov</h3>
        <p>Termodynamikkens andre lov sier at entropien i et isolert system alltid vil øke over tid, og at varme ikke kan spontant flytte seg fra et kaldere til et varmere område.</p>
        <button onclick="termodynamikk()">Tilbake</button>
    `;
}