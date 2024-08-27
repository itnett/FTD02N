document.addEventListener('DOMContentLoaded', () => {
    byggHovedmeny();
});

/**
 * Bygger hovedmenyen.
 */
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

/**
 * Bygger menyen for matematikk.
 */
function byggMatematikkMeny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Matematikk</h2>
        <button onclick="algebra_meny()">Algebra</button>
        <button onclick="trigonometri_og_geometri()">Trigonometri og Geometri</button>
        <button onclick="funksjoner()">Funksjoner</button>
        <button onclick="byggHovedmeny()">Tilbake til hovedmenyen</button>
    `;
}

/**
 * Bygger menyen for fysikk.
 */
function byggFysikkMeny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="innledendeFysikk()">Innledende fysikk</button>
        <button onclick="kraftOgRettlinjetBevegelse()">Kraft og rettlinjet bevegelse</button>
        <button onclick="energi()">Energi</button>
        <button onclick="termodynamikkensForsteLov()">Termodynamikkens første lov</button>
        <button onclick="byggHovedmeny()">Tilbake til hovedmenyen</button>
    `;
}

/**
 * Bygger menyen for studieretningsspesifikke temaer.
 */
function byggStudieretningMeny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Studieretningsspesifikke Temaer</h2>
        <button onclick="briggskeLogaritmer()">Briggske logaritmer</button>
        <button onclick="kombinatorikk()">Kombinatorikk</button>
        <button onclick="sannsynlighetOgStatistikk()">Sannsynlighetsregning og statistikk</button>
        <button onclick="faserOgFaseoverganger()">Faser og faseoverganger</button>
        <button onclick="varmeOgIndreEnergi()">Varme og indre energi</button>
        <button onclick="termofysikkensAndreLov()">Termofysikkens 2. hovedsetning</button>
        <button onclick="varmekapasitetOgKalorimetri()">Varmekapasitet og kalorimetri</button>
        <button onclick="tallsystemer()">Tallsystemer</button>
        <button onclick="algoritmiskTenking()">Algoritmisk tenking</button>
        <button onclick="byggHovedmeny()">Tilbake til hovedmenyen</button>
    `;
}