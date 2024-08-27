// Regneregler
function regnUtRegneregler() {
    // ... (samme implementasjon som i forrige svar)
}

// Brøk og prosentregning
function regnUtBrokAddisjon() {
    const teller1 = parseInt(document.getElementById("teller1").value);
    const nevner1 = parseInt(document.getElementById("nevner1").value);
    const teller2 = parseInt(document.getElementById("teller2").value);
    const nevner2 = parseInt(document.getElementById("nevner2").value);

    if (nevner1 === 0 || nevner2 === 0) {
        alert("Ugyldig input. Nevneren kan ikke være 0.");
        return;
    }

    const fellesnevner = lcm(nevner1, nevner2);
    const nyTeller1 = teller1 * (fellesnevner / nevner1);
    const nyTeller2 = teller2 * (fellesnevner / nevner2);
    const sumTeller = nyTeller1 + nyTeller2;

    const resultat = simplifyFraction(sumTeller, fellesnevner);
    document.getElementById("resultat").textContent = `${resultat.teller}/${resultat.nevner}`;

    // Forklaring (norsk og engelsk)
    const forklaringNorsk = `
        For å addere brøker, må vi først finne en fellesnevner. I dette tilfellet er fellesnevneren ${fellesnevner}. 
        Vi multipliserer deretter teller og nevner i hver brøk med den faktoren som gjør at nevneren blir lik fellesnevneren. 
        Til slutt adderer vi tellerne og forenkler brøken hvis mulig.
    `;

    const forklaringEngelsk = `
        To add fractions, we first need to find a common denominator. In this case, the common denominator is ${fellesnevner}. 
        We then multiply the numerator and denominator of each fraction by the factor that makes the denominator equal to the common denominator. 
        Finally, we add the numerators and simplify the fraction if possible.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Hjelpefunksjoner for brøkregning
function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}

function lcm(a, b) {
    return (a * b) / gcd(a, b);
}

function simplifyFraction(teller, nevner) {
    const gcdValue = gcd(teller, nevner);
    return { teller: teller / gcdValue, nevner: nevner / gcdValue };
}

// ... (Resten av funksjonene for brøk og prosentregning, potenser, standardform, sammentrekning og faktorisering)