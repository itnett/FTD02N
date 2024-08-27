function regnUtRegneregler() {
    // Hent verdier fra input-felt
    const tall1 = parseFloat(document.getElementById("tall1").value);
    const tall2 = parseFloat(document.getElementById("tall2").value);
    const operator = document.getElementById("operator").value;

    // Utfør beregning
    let resultat;
    switch (operator) {
        case "+":
            resultat = tall1 + tall2;
            break;
        // ... (andre operatorer)
    }

    // Vis resultat og forklaring
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Regneregler</h2>
        <p>${tall1} ${operator} ${tall2} = ${resultat}</p>
        <p>Forklaring (norsk): ...</p>
        <p>Explanation (English): ...</p>
    `;
}