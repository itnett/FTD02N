/**
 * Bygger menyen for studieretningsspesifikke temaer.
 */
function studieretning_meny() {
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
        <div id="studieretningInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

/**
 * Implementer funksjonene for studieretningsspesifikke temaer.
 */
function briggskeLogaritmer() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Briggske logaritmer (base 10)</h3>
        <input type="number" id="tall" placeholder="Skriv inn et tall">
        <button onclick="regnUtBriggskLogaritme()">Beregn</button>
    `;
}

function regnUtBriggskLogaritme() {
    const tall = parseFloat(document.getElementById("tall").value);
    if (tall <= 0) {
        alert("Tallet må være positivt.");
        return;
    }

    const logaritme = Math.log10(tall);
    document.getElementById("resultat").textContent = `log₁₀(${tall}) = ${logaritme.toFixed(4)}`;

    const forklaringNorsk = `
        Briggske logaritmer, også kjent som titallslogaritmer eller vanlige logaritmer, er logaritmer med grunntall 10. 
        Logaritmen til et tall x i base 10 er eksponenten som 10 må opphøyes i for å få x.
    `;

    const forklaringEngelsk = `
        Common logarithms, also known as base-10 logarithms or Briggsian logarithms, are logarithms with base 10.
        The logarithm of a number x to base 10 is the exponent to which 10 must be raised to obtain x.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Implementer de andre funksjonene for kombinatorikk, sannsynlighet og statistikk, faser og faseoverganger, varme og indre energi, termofysikkens 2. hovedsetning, varmekapasitet og kalorimetri, tallsystemer, og algoritmisk tenking på lignende måte.