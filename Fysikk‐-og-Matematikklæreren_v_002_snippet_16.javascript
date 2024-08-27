function fysikk_meny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="innledendeFysikk()">Innledende fysikk</button>
        <button onclick="kraftOgRettlinjetBevegelse()">Kraft og rettlinjet bevegelse</button>
        <button onclick="energiOgArbeid()">Energi og arbeid</button>
        <button onclick="termodynamikk()">Termodynamikk</button>
        <button onclick="byggHovedmeny()">Tilbake til hovedmenyen</button>
    `;
}

// Funksjoner for de ulike emnene, f.eks.:
function innledendeFysikk() { /* Implementasjon */ }
function kraftOgRettlinjetBevegelse() { /* Implementasjon */ }
function energiOgArbeid() { /* Implementasjon */ }
function termodynamikk() { /* Implementasjon */ }