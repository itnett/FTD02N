function trigonometri_og_geometri() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Trigonometri og Geometri</h2>
        <button onclick="beregn_areal()">Beregn areal av ulike figurer</button>
        <button onclick="beregn_omkrets()">Beregn omkrets av ulike figurer</button>
        <button onclick="beregn_volum()">Beregn volum av ulike figurer</button>
        <button onclick="beregn_overflate()">Beregn overflate av ulike figurer</button>
        <button onclick="pythagoras()">Pythagoras' setning</button>
        <button onclick="trigonometri()">Trigonometri i rettvinklede trekanter</button>
        <button onclick="vektorer()">Vektorer i planet</button>
        <div id="trigGeomInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Implementer de forskjellige funksjonene på samme måte som i tidligere svar