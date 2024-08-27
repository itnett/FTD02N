function funksjoner() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Funksjoner</h2>
        <button onclick="retteLinjer()">Rette linjer</button>
        <button onclick="polynomfunksjoner()">Polynomfunksjoner</button>
        <button onclick="eksponentialfunksjoner()">Eksponentialfunksjoner</button>
        <button onclick="derivasjonAvPolynomfunksjoner()">Derivasjon av polynomfunksjoner</button>
        <button onclick="regresjon

()">Regresjon (lineær)</button>
        <div id="funksjonerInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Implementer de forskjellige funksjonene på samme måte som i tidligere svar