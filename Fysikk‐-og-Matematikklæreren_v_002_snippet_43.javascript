document.addEventListener('DOMContentLoaded', () => {
    buildMainMenu();
});

function buildMainMenu() {
    const menyDiv = document.getElementById("meny");
    menyDiv.innerHTML = `
        <h2>Velg emne:</h2>
        <button onclick="buildMathMenu()">Matematikk</button>
        <button onclick="buildPhysicsMenu()">Fysikk</button>
        <button onclick="buildSpecialTopicsMenu()">Studieretningsspesifikke temaer</button>
    `;
    document.getElementById("innhold").innerHTML = ""; // Clear content area when going back to main menu
}

function buildMathMenu() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Matematikk</h2>
        <button onclick="algebraMenu()">Algebra</button>
        <button onclick="trigonometryGeometryMenu()">Trigonometri og Geometri</button>
        <button onclick="functionsMenu()">Funksjoner</button>
        <button onclick="buildMainMenu()">Tilbake til hovedmenyen</button>
    `;
}

function buildPhysicsMenu() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="introPhysics()">Innledende fysikk</button>
        <button onclick="forceAndMotion()">Kraft og rettlinjet bevegelse</button>
        <button onclick="energyAndWork()">Energi og arbeid</button>
        <button onclick="thermodynamics()">Termodynamikk</button>
        <button onclick="buildMainMenu()">Tilbake til hovedmenyen</button>
    `;
}

function buildSpecialTopicsMenu() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Studieretningsspesifikke Temaer</h2>
        <button onclick="briggsLogarithms()">Briggske logaritmer</button>
        <button onclick="combinatorics()">Kombinatorikk</button>
        <button onclick="probabilityAndStatistics()">Sannsynlighetsregning og statistikk</button>
        <button onclick="phasesAndTransitions()">Faser og faseoverganger</button>
        <button onclick="heatAndInternalEnergy()">Varme og indre energi</button>
        <button onclick="secondLawThermodynamics()">Termofysikkens 2. hovedsetning</button>
        <button onclick="heatCapacityAndCalorimetry()">Varmekapasitet og kalorimetri</button>
        <button onclick="numberSystems()">Tallsystemer</button>
        <button onclick="algorithmicThinking()">Algoritmisk tenking</button>
        <button onclick="buildMainMenu()">Tilbake til hovedmenyen</button>
    `;
}

document.getElementById("innhold").addEventListener("click", function(event) {
    if (event.target.classList.contains("generateCodeButton")) {
        const topic = event.target.dataset.topic;
        const input = getInputValues(topic);
        const code = generateCodeForTrinket(topic, input);
        displayCode(code);
    }
});

function displayCode(code) {
    const resultatDiv = document.getElementById("resultat");
    resultatDiv.innerHTML += `
        <h3>Generert kode for Trinket:</h3>
        <pre>${code}</pre>
    `;
}

function getInputValues(topic) {
    // Implement this function to get input values based on the selected topic
}