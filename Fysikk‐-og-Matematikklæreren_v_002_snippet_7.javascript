function fysikk_meny() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="innledendeFysikk()">Innledende fysikk</button>
        <button onclick="kraftOgRettlinjetBevegelse()">Kraft og rettlinjet bevegelse</button>
        <button onclick="energiOgArbeid()">Energi og arbeid</button>
        <

button onclick="termodynamikk()">Termodynamikk</button>
        <button onclick="byggHovedmeny()">Tilbake til hovedmenyen</button>
        <div id="fysikkInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function innledendeFysikk() {
    const fysikkInputDiv = document.getElementById("fysikkInput");
    fysikkInputDiv.innerHTML = `
        <h3>Innledende fysikk</h3>
        <input type="text" id="input1" placeholder="Input 1">
        <button onclick="beregnInnledendeFysikk()">Beregn</button>
    `;
}

function beregnInnledendeFysikk() {
    const input1 = document.getElementById("input1").value;

    // Her legger du inn beregningen og viser resultatet
    document.getElementById("resultat").textContent = `Resultatet er: ...`;

    const forklaringNorsk = `
        Forklaring på norsk ...
    `;

    const forklaringEngelsk = `
        Explanation in English ...
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}