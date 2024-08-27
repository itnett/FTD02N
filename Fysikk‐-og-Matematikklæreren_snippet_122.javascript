// Bygger menyen for studieretningsspesifikke temaer
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
    if (tall <= 0 || isNaN(tall)) {
        alert("Tallet må være et positivt tall.");
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
        <input type="number" id="n" placeholder="n (total antall elementer)">
        <input type="number" id="r" placeholder="r (antall elementer i utvalg)">
        <button onclick="regnUtKombinasjoner()">Beregn kombinasjoner</button>
    `;
}

function regnUtKombinasjoner() {
    const n = parseInt(document.getElementById("n").value);
    const r = parseInt(document.getElementById("r").value);

    if (isNaN(n) || isNaN(r) || n < 0 || r < 0 || r > n) {
        alert("Vennligst fyll inn gyldige verdier for n og r, der n ≥ r ≥ 0.");
        return;
    }

    const kombinasjoner = faktorial(n) / (faktorial(r) * faktorial(n - r));
    document.getElementById("resultat").textContent = `Antall kombinasjoner: ${kombinasjoner}`;

    const forklaringNorsk = `
        Kombinasjoner er antall måter å velge r elementer fra en mengde på n elementer uten å ta hensyn til rekkefølgen.
        Det beregnes som n! / (r!(n-r)!), der ! står for faktorial.
    `;

    const forklaringEngelsk = `
        Combinations are the number of ways to choose r elements from a set of n elements without regard to order.
        It is calculated as n! / (r!(n-r)!), where ! denotes factorial.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function faktorial(num) {
    if (num === 0 || num === 1) return 1;
    let result = 1;
    for (let i = num; i > 1; i--) {
        result *= i;
    }
    return result;
}

// Sannsynlighetsregning og statistikk
function sannsynlighetOgStatistikk() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Sannsynlighetsregning og statistikk</h3>
        <input type="number" id="gunstige" placeholder="Antall gunstige utfall">
        <input type="number" id="mulige" placeholder="Antall mulige utfall">
        <button onclick="beregnSannsynlighet()">Beregn sannsynlighet</button>
    `;
}

function beregnSannsynlighet() {
    const gunstige = parseInt(document.getElementById("gunstige").value);
    const mulige = parseInt(document.getElementById("mulige").value);

    if (isNaN(gunstige) || isNaN(mulige) || gunstige < 0 || mulige <= 0 || gunstige > mulige) {
        alert("Vennligst fyll inn gyldige verdier for gunstige og mulige utfall, der mulige > 0 og gunstige ≤ mulige.");
        return;
    }

    const sannsynlighet = gunstige / mulige;
    document.getElementById("resultat").textContent = `Sannsynligheten er: ${sannsynlighet.toFixed(4)}`;

    const forklaringNorsk = `
        Sannsynligheten for et hendelse er antall gunstige utfall delt på antall mulige utfall.
        I dette tilfellet er sannsynligheten ${sannsynlighet.toFixed(4)}.
    `;

    const forklaringEngelsk = `
        The probability of an event is the number of favorable outcomes divided by the number of possible outcomes.
        In this case, the probability is ${sannsynlighet.toFixed(4)}.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Faser og faseoverganger
function faserOgFaseoverganger() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Faser og faseoverganger</h3>
        <p>Faser refererer til de forskjellige tilstandene et stoff kan være i (fast, flytende, gass, plasma), og faseoverganger refererer til endringene mellom disse tilstandene.</p>
        <button onclick="studieretning_meny()">Tilbake</button>
    `;
}

// Varme og indre energi
function varmeOgIndreEnergi() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Varme og indre energi</h3>
        <input type="number" id="masse" placeholder="Masse (kg)">
        <input type="number" id="spesifikkVarme" placeholder="Spesifikk varme (J/kg°C)">
        <input type="number" id="temperaturEndring" placeholder="Temperaturendring (°C)">
        <button onclick="beregnVarme()">Beregn varme</button>
        <button onclick="studieretning_meny()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function beregnVarme() {
    const masse = parse

Float(document.getElementById("masse").value);
    const spesifikkVarme = parseFloat(document.getElementById("spesifikkVarme").value);
    const temperaturEndring = parseFloat(document.getElementById("temperaturEndring").value);

    if (isNaN(masse) || isNaN(spesifikkVarme) || isNaN(temperaturEndring) || masse <= 0 || spesifikkVarme <= 0 || temperaturEndring === 0) {
        alert("Vennligst fyll inn gyldige verdier for masse, spesifikk varme og temperaturendring.");
        return;
    }

    const varme = masse * spesifikkVarme * temperaturEndring;
    document.getElementById("resultat").textContent = `Varme (Q) er: ${varme.toFixed(2)} J`;

    const forklaringNorsk = `
        Varme (Q) er energien som overføres til eller fra et stoff på grunn av en temperaturendring. 
        Den beregnes som Q = mcΔT, hvor m er massen, c er den spesifikke varmekapasiteten, og ΔT er temperaturendringen.
        I dette tilfellet er varmen ${varme.toFixed(2)} J (joule).
    `;

    const forklaringEngelsk = `
        Heat (Q) is the energy transferred to or from a substance due to a temperature change. 
        It is calculated as Q = mcΔT, where m is the mass, c is the specific heat capacity, and ΔT is the temperature change.
        In this case, the heat is ${varme.toFixed(2)} J (joules).
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Termofysikkens 2. hovedsetning
function termofysikkensAndreLov() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Termofysikkens 2. hovedsetning</h3>
        <p>Termofysikkens andre lov sier at entropien i et isolert system alltid vil øke over tid, og at varme ikke kan spontant flytte seg fra et kaldere til et varmere område.</p>
        <button onclick="studieretning_meny()">Tilbake</button>
    `;
}

// Varmekapasitet og kalorimetri
function varmekapasitetOgKalorimetri() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Varmekapasitet og kalorimetri</h3>
        <input type="number" id="masse" placeholder="Masse (kg)">
        <input type="number" id="spesifikkVarme" placeholder="Spesifikk varme (J/kg°C)">
        <input type="number" id="temperaturEndring" placeholder="Temperaturendring (°C)">
        <button onclick="beregnVarmekapasitet()">Beregn varmekapasitet</button>
        <button onclick="studieretning_meny()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function beregnVarmekapasitet() {
    const masse = parseFloat(document.getElementById("masse").value);
    const spesifikkVarme = parseFloat(document.getElementById("spesifikkVarme").value);
    const temperaturEndring = parseFloat(document.getElementById("temperaturEndring").value);

    if (isNaN(masse) || isNaN(spesifikkVarme) || isNaN(temperaturEndring) || masse <= 0 || spesifikkVarme <= 0 || temperaturEndring === 0) {
        alert("Vennligst fyll inn gyldige verdier for masse, spesifikk varme og temperaturendring.");
        return;
    }

    const varmekapasitet = spesifikkVarme * masse;
    document.getElementById("resultat").textContent = `Varmekapasiteten er: ${varmekapasitet.toFixed(2)} J/°C`;

    const forklaringNorsk = `
        Varmekapasitet (C) er energien som kreves for å øke temperaturen på et stoff med én grad Celsius. 
        Den beregnes som C = mc, hvor m er massen og c er den spesifikke varmekapasiteten.
        I dette tilfellet er varmekapasiteten ${varmekapasitet.toFixed(2)} J/°C (joule per grad Celsius).
    `;

    const forklaringEngelsk = `
        Heat capacity (C) is the energy required to raise the temperature of a substance by one degree Celsius. 
        It is calculated as C = mc, where m is the mass and c is the specific heat capacity.
        In this case, the heat capacity is ${varmekapasitet.toFixed(2)} J/°C (joules per degree Celsius).
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Tallsystemer
function tallsystemer() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Tallsystemer</h3>
        <button onclick="desimaltTilBinært()">Desimalt til Binært</button>
        <button onclick="desimaltTilHeksadesimalt()">Desimalt til Heksadesimalt</button>
        <button onclick="binærtTilDesimalt()">Binært til Desimalt</button>
        <button onclick="heksadesimaltTilDesimalt()">Heksadesimalt til Desimalt</button>
    `;
}

function desimaltTilBinært() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Desimalt til Binært</h3>
        <input type="number" id="desimalt" placeholder="Desimalt tall">
        <button onclick="konverterDesimaltTilBinært()">Konverter</button>
        <button onclick="tallsystemer()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function konverterDesimaltTilBinært() {
    const desimalt = parseInt(document.getElementById("desimalt").value);
    if (isNaN(desimalt)) {
        alert("Vennligst fyll inn et gyldig desimalt tall.");
        return;
    }

    const binært = desimalt.toString(2);
    document.getElementById("resultat").textContent = `Binært: ${binært}`;

    const forklaringNorsk = `
        For å konvertere et desimalt tall til binært, deler vi tallet med 2 og registrerer resten.
        Dette gjentas til vi når null, og de registrerte restene leses baklengs for å få det binære tallet.
    `;

    const forklaringEngelsk = `
        To convert a decimal number to binary, we divide the number by 2 and record the remainder.
        This process is repeated until we reach zero, and the recorded remainders are read in reverse order to get the binary number.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function desimaltTilHeksadesimalt() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Desimalt til Heksadesimalt</h3>
        <input type="number" id="desimalt" placeholder="Desimalt tall">
        <button onclick="konverterDesimaltTilHeksadesimalt()">Konverter</button>
        <button onclick="tallsystemer()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function konverterDesimaltTilHeksadesimalt() {
    const desimalt = parseInt(document.getElementById("desimalt").value);
    if (isNaN(desimalt)) {
        alert("Vennligst fyll inn et gyldig desimalt tall.");
        return;
    }

    const heksadesimalt = desimalt.toString(16).toUpperCase();
    document.getElementById("resultat").textContent = `Heksadesimalt: ${heksadesimalt}`;

    const forklaringNorsk = `
        For å konvertere et desimalt tall til heksadesimalt, deler vi tallet med 16 og registrerer resten.
        Dette gjentas til vi når null, og de registrerte restene leses baklengs for å få det heksadesimale tallet.


    `;

    const forklaringEngelsk = `
        To convert a decimal number to hexadecimal, we divide the number by 16 and record the remainder.
        This process is repeated until we reach zero, and the recorded remainders are read in reverse order to get the hexadecimal number.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function binærtTilDesimalt() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Binært til Desimalt</h3>
        <input type="text" id="binært" placeholder="Binært tall">
        <button onclick="konverterBinærtTilDesimalt()">Konverter</button>
        <button onclick="tallsystemer()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function konverterBinærtTilDesimalt() {
    const binært = document.getElementById("binært").value;
    if (!/^[01]+$/.test(binært)) {
        alert("Vennligst fyll inn et gyldig binært tall.");
        return;
    }

    const desimalt = parseInt(binært, 2);
    document.getElementById("resultat").textContent = `Desimalt: ${desimalt}`;

    const forklaringNorsk = `
        For å konvertere et binært tall til desimalt, multipliserer vi hvert siffer i det binære tallet med 2 opphøyd i posisjonens plassverdi (startende fra 0 fra høyre) og summerer resultatene.
    `;

    const forklaringEngelsk = `
        To convert a binary number to decimal, we multiply each digit in the binary number by 2 raised to the power of the position's place value (starting from 0 from the right) and sum the results.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function heksadesimaltTilDesimalt() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Heksadesimalt til Desimalt</h3>
        <input type="text" id="heksadesimalt" placeholder="Heksadesimalt tall">
        <button onclick="konverterHeksadesimaltTilDesimalt()">Konverter</button>
        <button onclick="tallsystemer()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function konverterHeksadesimaltTilDesimalt() {
    const heksadesimalt = document.getElementById("heksadesimalt").value;
    if (!/^[0-9A-Fa-f]+$/.test(heksadesimalt)) {
        alert("Vennligst fyll inn et gyldig heksadesimalt tall.");
        return;
    }

    const desimalt = parseInt(heksadesimalt, 16);
    document.getElementById("resultat").textContent = `Desimalt: ${desimalt}`;

    const forklaringNorsk = `
        For å konvertere et heksadesimalt tall til desimalt, multipliserer vi hvert siffer i det heksadesimale tallet med 16 opphøyd i posisjonens plassverdi (startende fra 0 fra høyre) og summerer resultatene.
    `;

    const forklaringEngelsk = `
        To convert a hexadecimal number to decimal, we multiply each digit in the hexadecimal number by 16 raised to the power of the position's place value (starting from 0 from the right) and sum the results.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Algoritmisk tenking
function algoritmiskTenking() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Algoritmisk tenking</h3>
        <button onclick="boolskAlgebra()">Boolsk algebra</button>
        <button onclick="programmering()">Programmering</button>
        <button onclick="studieretning_meny()">Tilbake</button>
    `;
}

function boolskAlgebra() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Boolsk algebra</h3>
        <input type="text" id="boolskUttrykk" placeholder="Boolsk uttrykk (f.eks. A AND B OR NOT C)">
        <button onclick="evaluerBoolskAlgebra()">Evaluer</button>
        <button onclick="algoritmiskTenking()">Tilbake</button>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

function evaluerBoolskAlgebra() {
    const boolskUttrykk = document.getElementById("boolskUttrykk").value;
    if (!boolskUttrykk) {
        alert("Vennligst fyll inn et boolsk uttrykk.");
        return;
    }

    try {
        const evalResult = eval(boolskUttrykk
            .replace(/AND/g, '&&')
            .replace(/OR/g, '||')
            .replace(/NOT/g, '!'));
        document.getElementById("resultat").textContent = `Resultat: ${evalResult}`;

        const forklaringNorsk = `
            Boolsk algebra er en gren av matematikken som omhandler sannhetsverdiene sann (true) og usann (false). 
            Vanlige operasjoner inkluderer AND (og), OR (eller), og NOT (ikke). 
            I dette tilfellet er resultatet ${evalResult}.
        `;

        const forklaringEngelsk = `
            Boolean algebra is a branch of mathematics that deals with truth values true and false. 
            Common operations include AND, OR, and NOT. 
            In this case, the result is ${evalResult}.
        `;

        document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
    } catch (error) {
        alert("Det oppsto en feil ved evalueringen av det boolske uttrykket. Vennligst sjekk syntaksen.");
    }
}

function programmering() {
    const studieretningInputDiv = document.getElementById("studieretningInput");
    studieretningInputDiv.innerHTML = `
        <h3>Programmering</h3>
        <p>Her kan du lære grunnleggende programmering og algoritmer.</p>
        <button onclick="studieretning_meny()">Tilbake</button>
    `;
}