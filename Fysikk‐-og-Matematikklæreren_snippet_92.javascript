// Build the Algebra menu
function buildAlgebraMenu() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Algebra</h2>
        <button onclick="losAndregradslikning()">Løs Andregradslikning</button>
        <!-- Add more algebra topics here -->
    `;
}

// Solve quadratic equation
function losAndregradslikning() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Løs Andregradslikning</h2>
        <p>Forklaring på norsk og engelsk om andregradslikninger og løsningsmetoder...</p>
        <label for="a">a:</label>
        <input type="number" id="a">
        <label for="b">b:</label>
        <input type="number" id="b">
        <label for="c">c:</label>
        <input type="number" id="c">
        <button onclick="beregnAndregradslikning()">Beregn</button>
        <div id="resultat"></div>
    `;
}

// Calculate quadratic equation solutions
function beregnAndregradslikning() {
    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);
    const c = parseFloat(document.getElementById('c').value);
    const resultat = document.getElementById('resultat');
    
    if (isNaN(a) || isNaN(b) || isNaN(c)) {
        resultat.innerHTML = '<p>Vennligst oppgi gyldige tallverdier.</p>';
        return;
    }

    const diskriminant = b * b - 4 * a * c;
    if (diskriminant < 0) {
        resultat.innerHTML = '<p>Ingen reelle røtter.</p>';
    } else {
        const x1 = (-b + Math.sqrt(diskriminant)) / (2 * a);
        const x2 = (-b - Math.sqrt(diskriminant)) / (2 * a);
        resultat.innerHTML = `
            <p>Løsningene er x1 = ${x1} og x2 = ${x2}</p>
        `;
    }
}