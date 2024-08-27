function fysikk_meny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="innledendeFysikk()">Innledende fysikk</button>
        <button onclick="kraftOgRettlinjetBevegelse()">Kraft og rettlinjet bevegelse</button>
        <button onclick="energiOgArbeid()">Energi og arbeid</button>
        <button onclick="termodynamikk()">Termodynamikk</button>
        <div id="fysikkInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Implementer de forskjellige funksjonene på samme måte som i tidligere svar