// Funksjoner for å bygge menyene dynamisk
function byggHovedmeny() {
    const menyDiv = document.getElementById("meny");
    menyDiv.innerHTML = `
        <h2>Velg emne:</h2>
        <button onclick="byggMatematikkMeny()">Matematikk</button>
        <button onclick="byggFysikkMeny()">Fysikk</button>
        <button onclick="byggStudieretningMeny()">Studieretningsspesifikke temaer</button>
    `;
}

function byggMatematikkMeny() {
    // ... (din kode for å bygge matematikkmenyen dynamisk)
}

// ... (funksjoner for å bygge de andre menyene)

// Event listeners for å håndtere brukerinteraksjon
document.addEventListener('DOMContentLoaded', () => {
    byggHovedmeny();
    // ... (legg til event listeners for knapper og input-felt)
});