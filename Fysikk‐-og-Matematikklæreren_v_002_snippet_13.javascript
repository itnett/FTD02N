function algebra_meny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Algebra</h2>
        <button onclick="regneregler()">Regneregler</button>
        <button onclick="brok_og_prosentregning()">Brøk og prosentregning</button>
        <button onclick="potenser()">Potenser</button>
        <button onclick="tall_pa_standardform()">Tall på standardform</button>
        <button onclick="sammentrekning_og_faktorisering()">Sammentrekning og faktorisering</button>
        <button onclick="los_forstegradslikning()">Løs likninger av første grad</button>
        <button onclick="los_andregradslikning()">Løs likninger av andre grad</button>
        <button onclick="los_likningssett()">Løs likningssett med to ukjente</button>
        <button onclick="tilpasse_og_omforme_formler()">Tilpasse og omforme formeluttrykk</button>
        <button onclick="byggMatematikkMeny()">Tilbake til matematikkmenyen</button>
    `;
}

// Funksjoner for de ulike emnene, f.eks.:
function regneregler() { /* Implementasjon */ }
function brok_og_prosentregning() { /* Implementasjon */ }
function potenser() { /* Implementasjon */ }
function tall_pa_standardform() { /* Implementasjon */ }
function sammentrekning_og_faktorisering() { /* Implementasjon */ }
function los_forstegradslikning() { /* Implementasjon */ }
function los_andregradslikning() { /* Implementasjon */ }
function los_likningssett() { /* Implementasjon */ }
function tilpasse_og_omforme_formler() { /* Implementasjon */ }