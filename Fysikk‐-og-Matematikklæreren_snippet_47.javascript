// studieretning_modul.js

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
        <div id="studieretningInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Briggske logaritmer
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

// Kombinatorikk
function kombinatorikk() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Kombinatorikk</h3>
        <select id="kombinatorikkType">
            <option value="permutasjon">Permutasjon</option>
            <option value="kombinasjon">Kombinasjon</option>
        </select>
        <input type="number" id="n" placeholder="n">
        <input type="number" id="k" placeholder="k (kun for kombinasjon)">
        <button onclick="regnUtKombinatorikk()">Beregn</button>
    `;

    document.getElementById("kombinatorikkType").addEventListener("change", function() {
        const kInput = document.getElementById("k");
        if (this.value === "kombinasjon") {
            kInput.style.display = "block";
        } else {
            kInput.style.display = "none";
        }
    });
}

function regnUtKombinatorikk() {
    const type = document.getElementById("kombinatorikkType").value;
    const n = parseInt(document.getElementById("n").value);
    let k, resultat;

    if (type === "permutasjon") {
        resultat = factorial(n);
        document.getElementById("resultat").textContent = `Antall permutasjoner av ${n} elementer er: ${resultat}`;
    } else if (type === "kombinasjon") {
        k = parseInt(document.getElementById("k").value);
        if (k > n || n < 0 || k < 0) {
            alert("Ugyldige verdier for n og k. n må være større eller lik k, og begge må være ikke-negative.");
            return;
        }
        resultat = factorial(n) / (factorial(k) * factorial(n - k));
        document.getElementById("resultat").textContent = `Antall kombinasjoner av ${n} elementer valgt ${k} om gangen er: ${resultat}`;
    }

    // Forklaringer (norsk og engelsk)
    // ... (Legg til forklaringer for permutasjoner og kombinasjoner)
}

function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// ... (Resten av funksjonene for sannsynlighet og statistikk, faser og faseoverganger, varme og indre energi, etc.)