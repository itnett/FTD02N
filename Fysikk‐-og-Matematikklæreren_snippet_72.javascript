// Funksjoner for å bygge menyene dynamisk
function byggHovedmeny() {
    const menyDiv = document.getElementById("meny");
    menyDiv.innerHTML = `
        <h2>Velg emne:</h2>
        <button onclick="byggMatematikkMeny()">Matematikk</button>
        <button onclick="byggFysikkMeny()">Fysikk</button>
        <button onclick="byggStudieretningMeny()">Studieretningsspesifikke temaer</button>
    `;
    document.getElementById("innhold").innerHTML = ""; // Tøm innhold-området når man går tilbake til hovedmenyen
}

function byggMatematikkMeny() {
    // ... (samme som før)
}

function byggFysikkMeny() {
    // ... (samme som før)
}

function byggStudieretningMeny() {
    // ... (samme som før)
}

// Event listeners for å håndtere brukerinteraksjon
document.addEventListener('DOMContentLoaded', () => {
    byggHovedmeny();
    // ... (legg til event listeners for knapper og input-felt)
});