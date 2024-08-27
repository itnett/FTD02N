function algebraMenu() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Algebra</h2>
        <button onclick="regneregler()">Regneregler</button>
        <button onclick="brokOgProsentregning()">Brøk og prosentregning</button>
        <button onclick="potenser()">Potenser</button>
        <button onclick="tallPaStandardform()">Tall på standardform</button>
        <button onclick="sammentrekningOgFaktorisering()">Sammentrekning og faktorisering</button>
        <button onclick="losForstegradslikning()">Løs likninger av første grad</button>
        <button onclick="losAndregradslikning()">Løs likninger av andre grad</button>
        <button onclick="losLikningssett()">Løs likningssett med to ukjente</button>
        <button onclick="tilpasseOgOmformeFormler()">Tilpasse og omforme formeluttrykk</button>
        <button onclick="buildMathMenu()">Tilbake til matematikkmenyen</button>
    `;
}

function regneregler() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h3>Regneregler</h3>
        <input

 type="number" id="num1" placeholder="Tall 1">
        <select id="operator">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" id="num2" placeholder="Tall 2">
        <button onclick="calculateArithmetic()">Beregn</button>
        <button class="generateCodeButton" data-topic="regneregler">Generer kode</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function calculateArithmetic() {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const operator = document.getElementById("operator").value;

    let result;
    switch (operator) {
        case "+":
            result = num1 + num2;
            break;
        case "-":
            result = num1 - num2;
            break;
        case "*":
            result = num1 * num2;
            break;
        case "/":
            if (num2 !== 0) {
                result = num1 / num2;
            } else {
                alert("Kan ikke dele med null.");
                return;
            }
            break;
        default:
            alert("Ugyldig operator.");
            return;
    }

    document.getElementById("resultat").textContent = `${num1} ${operator} ${num2} = ${result}`;

    const forklaringNorsk = `
        Dette er en enkel regneoperasjon. Operatoren "${operator}" angir hvilken regneoperasjon som skal utføres.
    `;

    const forklaringEngelsk = `
        This is a simple arithmetic operation. The operator "${operator}" indicates which operation to perform.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}