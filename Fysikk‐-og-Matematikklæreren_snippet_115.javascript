// Bygg menyen for fysikk
// Build the menu for physics
function buildPhysicsMenu() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Fysikk</h2>
        <button onclick="kraftOgBevegelse()">Kraft og Bevegelse</button>
        <button onclick="energiOgArbeid()">Energi og Arbeid</button>
        <button onclick="bølgerOgLyd()">Bølger og Lyd</button>
        <button onclick="elektrisitetOgMagnetisme()">Elektrisitet og Magnetisme</button>
        <button onclick="kvantefysikk()">Kvantefysikk</button>
    `;
}

// Kraft og Bevegelse
// Force and Motion
function kraftOgBevegelse() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Kraft og Bevegelse</h2>
        <p>
            Kraft og bevegelse dekker emner som Newtons lover, akselerasjon, og hastighet. Studenter lærer hvordan krefter påvirker 
            objekter i bevegelse.
        </p>
        <p>
            Force and motion cover topics such as Newton's laws, acceleration, and velocity. Students learn how forces affect 
            objects in motion.
        </p>
        <label for="masse">Masse (kg):</label>
        <input type="number" id="masse">
        <label for="akselerasjon">Akselerasjon (m/s^2):</label>
        <input type="number" id="akselerasjon">
        <button onclick="beregnKraft()">Beregn Kraft</button>
        <div id="resultat"></div>
    `;
}

// Beregn kraft ved hjelp av Newtons andre lov
// Calculate force using Newton's second law
function beregnKraft() {
    const masse = parseFloat(document.getElementById('masse').value);
    const akselerasjon = parseFloat(document.getElementById('akselerasjon').value);
    const resultat = document.getElementById('resultat');

    if (isNaN(masse) || isNaN(akselerasjon)) {
        resultat.innerHTML = '<p>Vennligst oppgi gyldige verdier for masse og akselerasjon.</p>';
        return;
    }

    const kraft = masse * akselerasjon;
    resultat.innerHTML = `
        <p>Kraften er ${kraft.toFixed(2)} N (Newton).</p>
        <p><strong>Forklaring på norsk:</strong> Kraften beregnes ved å multiplisere massen med akselerasjonen (F = m * a).</p>
        <p><strong>Explanation in English:</strong> The force is calculated by multiplying the mass by the acceleration (F = m * a).</p>
    `;
}

// Energi og Arbeid
// Energy and Work
function energiOgArbeid() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Energi og Arbeid</h2>
        <p>
            Energi og arbeid dekker emner som kinetisk energi, potensiell energi, og arbeid. Studenter lærer hvordan energi omdannes 
            og brukes til å utføre arbeid.
        </p>
        <p>
            Energy and work cover topics such as kinetic energy, potential energy, and work. Students learn how energy is transformed 
            and used to perform work.
        </p>
        <label for="kraft">Kraft (N):</label>
        <input type="number" id="kraft">
        <label for="distanse">Distanse (m):</label>
        <input type="number" id="distanse">
        <button onclick="beregnArbeid()">Beregn Arbeid</button>
        <div id="resultat"></div>
    `;
}

// Beregn arbeid
// Calculate work
function beregnArbeid() {
    const kraft = parseFloat(document.getElementById('kraft').value);
    const distanse = parseFloat(document.getElementById('distanse').value);
    const resultat = document.getElementById('resultat');

    if (isNaN(kraft) || isNaN(distanse)) {
        resultat.innerHTML = '<p>Vennligst oppgi gyldige verdier for kraft og distanse.</p>';
        return;
    }

    const arbeid = kraft * distanse;
    resultat.innerHTML = `
        <p>Arbeidet er ${arbeid.toFixed(2)} J (Joule).</p>
        <p><strong>Forklaring på norsk:</strong> Arbeidet beregnes ved å multiplisere kraften med distansen (W = F * d).</p>
        <p><strong>Explanation in English:</strong> The work is calculated by multiplying the force by the distance (W = F * d).</p>
    `;
}

// Bølger og Lyd
// Waves and Sound
function bølgerOgLyd() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Bølger og Lyd</h2>
        <p>
            Bølger og lyd dekker emner som bølgelengde, frekvens, og amplitude. Studenter lærer hvordan bølger overfører energi og hvordan 
            lyd reiser gjennom ulike medier.
        </p>
        <p>
            Waves and sound cover topics such as wavelength, frequency, and amplitude. Students learn how waves transfer energy and how 
            sound travels through different media.
        </p>
    `;
}

// Elektrisitet og Magnetisme
// Electricity and Magnetism
function elektrisitetOgMagnetisme() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Elektrisitet og Magnetisme</h2>
        <p>
            Elektrisitet og magnetisme dekker emner som elektrisk ladning, elektrisk felt, og magnetiske krefter. Studenter lærer om 
            sammenhengen mellom elektrisitet og magnetisme.
        </p>
        <p>
            Electricity and magnetism cover topics such as electric charge, electric field, and magnetic forces. Students learn about 
            the relationship between electricity and magnetism.
        </p>
        <label for="ladning">Elektrisk ladning (C):</label>
        <input type="number" id="ladning">
        <label for="feltstyrke">Elektrisk feltstyrke (N/C):</label>
        <input type="number" id="feltstyrke">
        <button onclick="beregnKraftElektriskFelt()">Beregn Kraft</button>
        <div id="resultat"></div>
    `;
}

// Beregn kraft i et elektrisk felt
// Calculate force in an electric field
function beregnKraftElektriskFelt() {
    const ladning = parseFloat(document.getElementById('ladning').value);
    const feltstyrke = parseFloat(document.getElementById('feltstyrke').value);
    const resultat = document.getElementById('resultat');

    if (isNaN(ladning) || isNaN(feltstyrke)) {
        resultat.innerHTML = '<p>Vennligst oppgi gyldige verdier for elektrisk ladning og feltstyrke.</p>';
        return;
    }

    const kraft = ladning * feltstyrke;
    resultat.innerHTML = `
        <p>Kraften er ${kraft.toFixed(2)} N (Newton).</p>
        <p><strong>Forklaring på norsk:</strong> Kraften beregnes ved å multiplisere ladningen med feltstyrken (F = q * E).</p>
        <p><strong>Explanation in English:</strong> The force is calculated by multiplying the charge by the field strength (F = q * E).</p>
    `;
}

// Kvantefysikk
// Quantum Physics
function kvantefysikk() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Kvantefysikk</h2>
        <p>
            Kvantefysikk dekker emner som kvantemekanikk, fotoner, og kvantefelt. Studenter lærer om de grunnleggende prinsippene som styrer 
            atomer og subatomære partikler.
        </p>
        <p>
            Quantum physics covers topics such as quantum mechanics, photons, and quantum fields. Students learn about the fundamental 
            principles governing atoms and subatomic particles.
        </p>
    `;
}