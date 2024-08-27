document.addEventListener('DOMContentLoaded', () => {
    byggHovedmeny();
});

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
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Matematikk</h2>
        <button onclick="algebra_meny()">Algebra</button>
        <button onclick="trigonometri_og_geometri()">Trigonometri og Geometri</button>
        <button onclick="funksjoner()">Funksjoner</button>
    `;
}

function byggFysikkMeny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="fysikk_meny()">Fysikk</button>
    `;
}

function byggStudieretningMeny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Studieretningsspesifikke Temaer</h2>
        <button onclick="studieretning_meny()">Studieretningsspesifikke Temaer</button>
    `;
}