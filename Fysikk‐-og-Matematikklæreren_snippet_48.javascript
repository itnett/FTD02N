// Sannsynlighetsregning og statistikk
function sannsynlighetOgStatistikk() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Sannsynlighetsregning og statistikk</h3>
        <button onclick="beregnSannsynlighet()">Beregning av sannsynlighet</button>
        <button onclick="beregnGjennomsnitt()">Beregning av gjennomsnitt</button>
        <button onclick="beregnVarians()">Beregning av varians</button>
        <div id="statistikkInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function beregnSannsynlighet() {
    const statistikkInputDiv = document.getElementById("statistikkInput");
    statistikkInputDiv.innerHTML = `
        <h4>Beregning av sannsynlighet</h4>
        <input type="number" id="gunstige" placeholder="Antall gunstige utfall">
        <input type="number" id="mulige" placeholder="Antall mulige utfall">
        <button onclick="regnUtSannsynlighet()">Beregn</button>
    `;
}

function regnUtSannsynlighet() {
    const gunstige = parseFloat(document.getElementById("gunstige").value);
    const mulige = parseFloat(document.getElementById("mulige").value);
    
    if (mulige === 0) {
        alert("Antall mulige utfall kan ikke være null.");
        return;
    }
    
    const sannsynlighet = gunstige / mulige;
    document.getElementById("resultat").textContent = `Sannsynligheten er: ${sannsynlighet.toFixed(4)}`;
    
    const forklaringNorsk = `
        Sannsynligheten for et hendelse er forholdet mellom antall gunstige utfall og antall mulige utfall.
        I dette tilfellet er sannsynligheten ${gunstige} / ${mulige} = ${sannsynlighet.toFixed(4)}.
    `;
    
    const forklaringEngelsk = `
        The probability of an event is the ratio of the number of favorable outcomes to the number of possible outcomes.
        In this case, the probability is ${gunstige} / ${mulige} = ${sannsynlighet.toFixed(4)}.
    `;
    
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function beregnGjennomsnitt() {
    const statistikkInputDiv = document.getElementById("statistikkInput");
    statistikkInputDiv.innerHTML = `
        <h4>Beregning av gjennomsnitt</h4>
        <input type="text" id="verdier" placeholder="Skriv inn verdier separert med komma">
        <button onclick="regnUtGjennomsnitt()">Beregn</button>
    `;
}

function regnUtGjennomsnitt() {
    const verdierStr = document.getElementById("verdier").value;
    const verdier = verdierStr.split(',').map(Number);
    
    const sum = verdier.reduce((acc, val) => acc + val, 0);
    const gjennomsnitt = sum / verdier.length;
    document.getElementById("resultat").textContent = `Gjennomsnittet er: ${gjennomsnitt.toFixed(4)}`;
    
    const forklaringNorsk = `
        Gjennomsnittet er summen av alle verdiene delt på antall verdier.
        I dette tilfellet er gjennomsnittet (${verdier.join(' + ')}) / ${verdier.length} = ${gjennomsnitt.toFixed(4)}.
    `;
    
    const forklaringEngelsk = `
        The average is the sum of all values divided by the number of values.
        In this case, the average is (${verdier.join(' + ')}) / ${verdier.length} = ${gjennomsnitt.toFixed(4)}.
    `;
    
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function beregnVarians() {
    const statistikkInputDiv = document.getElementById("statistikkInput");
    statistikkInputDiv.innerHTML = `
        <h4>Beregning av varians</h4>
        <input type="text" id="verdier" placeholder="Skriv inn verdier separert med komma">
        <button onclick="regnUtVarians()">Beregn</button>
    `;
}

function regnUtVarians() {
    const verdierStr = document.getElementById("verdier").value;
    const verdier = verdierStr.split(',').map(Number);
    
    const sum = verdier.reduce((acc, val) => acc + val, 0);
    const gjennomsnitt = sum / verdier.length;
    const sumKvadratAvvik = verdier.reduce((acc, val) => acc + Math.pow(val - gjennomsnitt, 2), 0);
    const varians = sumKvadratAvvik / verdier.length;
    document.getElementById("resultat").textContent = `Variansen er: ${varians.toFixed(4)}`;
    
    const forklaringNorsk = `
        Variansen er gjennomsnittet av kvadratene av avvikene fra gjennomsnittet.
        I dette tilfellet er variansen summen av kvadratene av avvikene fra gjennomsnittet, delt på antall verdier.
    `;
    
    const forklaringEngelsk = `
        The variance is the average of the squares of the deviations from the mean.
        In this case, the variance is the sum of the squares of the deviations from the mean, divided by the number of values.
    `;
    
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}