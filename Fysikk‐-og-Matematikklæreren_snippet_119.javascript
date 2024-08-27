// Bygger menyen for trigonometri og geometri
function trigonometri_og_geometri() {
    const innholdDiv = document.getElementById("innhold");
    innholdDiv.innerHTML = `
        <h2>Trigonometri og Geometri</h2>
        <button onclick="beregn_areal()">Beregn areal</button>
        <button onclick="beregn_omkrets()">Beregn omkrets</button>
        <button onclick="beregn_volum()">Beregn volum</button>
        <button onclick="pythagoras()">Pythagoras' setning</button>
        <button onclick="trigonometri()">Trigonometri i rettvinklede trekanter</button>
        <button onclick="vektorer()">Vektorer</button>
        <button onclick="byggMatematikkMeny()">Tilbake til matematikkmenyen</button>
        <div id="trigGeomInput"></div>
        <p id="resultat"></p>
        <p id="forklaring"></p>
    `;
}

// Funksjoner for arealberegning
function beregn_areal() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn areal</h3>
        <select id="figur">
            <option value="trekant">Trekant</option>
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
            <option value="parallellogram">Parallellogram</option>
            <option value="trapes">Trapes</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtAreal()">Beregn</button>
    `;

    document.getElementById("figur").addEventListener("change", function() {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");

        switch (figur) {
            case "trekant":
            case "parallellogram":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="grunnlinje" placeholder="Grunnlinje">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            case "sirkel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "rektangel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="lengde" placeholder="Lengde">
                    <input type="number" id="bredde" placeholder="Bredde">
                `;
                break;
            case "trapes":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="a" placeholder="Side a">
                    <input type="number" id="b" placeholder="Side b">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            default:
                inputFeltDiv.innerHTML = "";
        }
    });
}

function regnUtAreal() {
    const figur = document.getElementById("figur").value;
    let areal;
    let forklaringNorsk, forklaringEngelsk;

    switch (figur) {
        case "trekant":
            const grunnlinje = parseFloat(document.getElementById("grunnlinje").value);
            const hoyde = parseFloat(document.getElementById("hoyde").value);
            if (isNaN(grunnlinje) || isNaN(hoyde)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            areal = 0.5 * grunnlinje * hoyde;
            forklaringNorsk = `Arealet av en trekant er halvparten av grunnlinjen multiplisert med høyden.`;
            forklaringEngelsk = `The area of a triangle is half the base multiplied by the height.`;
            break;
        case "sirkel":
            const radius = parseFloat(document.getElementById("radius").value);
            if (isNaN(radius)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            areal = Math.PI * radius ** 2;
            forklaringNorsk = `Arealet av en sirkel er pi (π) multiplisert med radius kvadrert.`;
            forklaringEngelsk = `The area of a circle is pi (π) multiplied by the radius squared.`;
            break;
        case "rektangel":
            const lengde = parseFloat(document.getElementById("lengde").value);
            const bredde = parseFloat(document.getElementById("bredde").value);
            if (isNaN(lengde) || isNaN(bredde)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            areal = lengde * bredde;
            forklaringNorsk = `Arealet av et rektangel er lengden multiplisert med bredden.`;
            forklaringEngelsk = `The area of a rectangle is the length multiplied by the width.`;
            break;
        case "parallellogram":
            const grunnlinjeP = parseFloat(document.getElementById("grunnlinje").value);
            const hoydeP = parseFloat(document.getElementById("hoyde").value);
            if (isNaN(grunnlinjeP) || isNaN(hoydeP)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            areal = grunnlinjeP * hoydeP;
            forklaringNorsk = `Arealet av et parallellogram er grunnlinjen multiplisert med høyden.`;
            forklaringEngelsk = `The area of a parallelogram is the base multiplied by the height.`;
            break;
        case "trapes":
            const a = parseFloat(document.getElementById("a").value);
            const b = parseFloat(document.getElementById("b").value);
            const hoydeT = parseFloat(document.getElementById("hoyde").value);
            if (isNaN(a) || isNaN(b) || isNaN(hoydeT)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            areal = 0.5 * (a + b) * hoydeT;
            forklaringNorsk = `Arealet av et trapes er gjennomsnittet av de parallelle sidene multiplisert med høyden.`;
            forklaringEngelsk = `The area of a trapezoid is the average of the parallel sides multiplied by the height.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Arealet er: ${areal.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for omkretsberegning
function beregn_omkrets() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn omkrets</h3>
        <select id="figur">
            <option value="trekant">Trekant</option>
            <option value="sirkel">Sirkel</option>
            <option value="rektangel">Rektangel</option>
            <option value="parallellogram">Parallellogram</option>
            <option value="trapes">Trapes</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtOmkrets()">Beregn</button>
    `;

    document.getElementById("figur").addEventListener("change", function() {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");

        switch (figur) {
            case "trekant":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="side1" placeholder="Side 1">
                    <input type="number" id="side2" placeholder="Side 2">
                    <input type="number" id="side3" placeholder="Side 3">
                `;
                break;
            case "sirkel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "rektangel":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="lengde" placeholder="Lengde">
                    <input type="number" id="bredde" placeholder="Bredde">
                `;
                break;
            case "parallellogram":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="grunnlinje" placeholder="Grunnlinje">
                    <input type="number" id="s

idelengde" placeholder="Sidelengde">
                `;
                break;
            case "trapes":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="a" placeholder="Side a">
                    <input type="number" id="b" placeholder="Side b">
                    <input type="number" id="c" placeholder="Side c">
                    <input type="number" id="d" placeholder="Side d">
                `;
                break;
            default:
                inputFeltDiv.innerHTML = "";
        }
    });
}

function regnUtOmkrets() {
    const figur = document.getElementById("figur").value;
    let omkrets;
    let forklaringNorsk, forklaringEngelsk;

    switch (figur) {
        case "trekant":
            const side1 = parseFloat(document.getElementById("side1").value);
            const side2 = parseFloat(document.getElementById("side2").value);
            const side3 = parseFloat(document.getElementById("side3").value);
            if (isNaN(side1) || isNaN(side2) || isNaN(side3)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            omkrets = side1 + side2 + side3;
            forklaringNorsk = `Omkretsen av en trekant er summen av de tre sidene.`;
            forklaringEngelsk = `The perimeter of a triangle is the sum of the three sides.`;
            break;
        case "sirkel":
            const radius = parseFloat(document.getElementById("radius").value);
            if (isNaN(radius)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            omkrets = 2 * Math.PI * radius;
            forklaringNorsk = `Omkretsen av en sirkel er 2 multiplisert med pi (π) og radius.`;
            forklaringEngelsk = `The perimeter of a circle is 2 times pi (π) and the radius.`;
            break;
        case "rektangel":
            const lengde = parseFloat(document.getElementById("lengde").value);
            const bredde = parseFloat(document.getElementById("bredde").value);
            if (isNaN(lengde) || isNaN(bredde)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            omkrets = 2 * (lengde + bredde);
            forklaringNorsk = `Omkretsen av et rektangel er to ganger summen av lengden og bredden.`;
            forklaringEngelsk = `The perimeter of a rectangle is twice the sum of the length and the width.`;
            break;
        case "parallellogram":
            const grunnlinjeP = parseFloat(document.getElementById("grunnlinje").value);
            const sidelengdeP = parseFloat(document.getElementById("sidelengde").value);
            if (isNaN(grunnlinjeP) || isNaN(sidelengdeP)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            omkrets = 2 * (grunnlinjeP + sidelengdeP);
            forklaringNorsk = `Omkretsen av et parallellogram er to ganger summen av grunnlinjen og sidelengden.`;
            forklaringEngelsk = `The perimeter of a parallelogram is twice the sum of the base and the side length.`;
            break;
        case "trapes":
            const a = parseFloat(document.getElementById("a").value);
            const b = parseFloat(document.getElementById("b").value);
            const c = parseFloat(document.getElementById("c").value);
            const d = parseFloat(document.getElementById("d").value);
            if (isNaN(a) || isNaN(b) || isNaN(c) || isNaN(d)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            omkrets = a + b + c + d;
            forklaringNorsk = `Omkretsen av et trapes er summen av alle sidene.`;
            forklaringEngelsk = `The perimeter of a trapezoid is the sum of all its sides.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Omkretsen er: ${omkrets.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for volum
function beregn_volum() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Beregn volum</h3>
        <select id="figur">
            <option value="kule">Kule</option>
            <option value="kube">Kube</option>
            <option value="sylinder">Sylinder</option>
            <option value="kjegle">Kjegle</option>
        </select>
        <div id="inputFelt"></div>
        <button onclick="regnUtVolum()">Beregn</button>
    `;

    document.getElementById("figur").addEventListener("change", function() {
        const figur = this.value;
        const inputFeltDiv = document.getElementById("inputFelt");

        switch (figur) {
            case "kule":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                `;
                break;
            case "kube":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="sidelengde" placeholder="Sidelengde">
                `;
                break;
            case "sylinder":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            case "kjegle":
                inputFeltDiv.innerHTML = `
                    <input type="number" id="radius" placeholder="Radius">
                    <input type="number" id="hoyde" placeholder="Høyde">
                `;
                break;
            default:
                inputFeltDiv.innerHTML = "";
        }
    });
}

function regnUtVolum() {
    const figur = document.getElementById("figur").value;
    let volum;
    let forklaringNorsk, forklaringEngelsk;

    switch (figur) {
        case "kule":
            const radius = parseFloat(document.getElementById("radius").value);
            if (isNaN(radius)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            volum = (4 / 3) * Math.PI * radius ** 3;
            forklaringNorsk = `Volumet av en kule er (4/3) * pi (π) * radius i tredje.`;
            forklaringEngelsk = `The volume of a sphere is (4/3) * pi (π) * radius cubed.`;
            break;
        case "kube":
            const sidelengde = parseFloat(document.getElementById("sidelengde").value);
            if (isNaN(sidelengde)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            volum = sidelengde ** 3;
            forklaringNorsk = `Volumet av en kube er sidelengden opphøyd i tredje.`;
            forklaringEngelsk = `The volume of a cube is the side length cubed.`;
            break;
        case "sylinder":
            const radiusS = parseFloat(document.getElementById("radius").value);
            const hoydeS = parseFloat(document.getElementById("hoyde").value);
            if (isNaN(radiusS) || isNaN(hoydeS)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            volum = Math.PI * radiusS ** 2 * hoydeS;
            forklaringNorsk = `Volumet av en sylinder er pi (π) * radius kvadrert * høyden.`;
            forklaringEngelsk = `The volume of a cylinder is pi (π) * radius squared * height.`;
            break;
        case "kjegle":
            const radiusK = parseFloat(document.getElementById("radius").value);
            const hoydeK = parseFloat(document.getElementById("hoyde").value);
            if (isNaN(radiusK) || isNaN(hoydeK)) {
                alert("Vennligst fyll inn gyldige verdier.");
                return;
            }
            volum = (1 / 3) * Math.PI * radiusK ** 2 * hoydeK;
            forklaringNorsk = `Volumet av en kjegle er (1/3) * pi (π) * radius kvadrert * høyden.`;
            forklaringEngelsk = `The volume of a cone is (1/3) *

 pi (π) * radius squared * height.`;
            break;
        default:
            alert("Ugyldig figur.");
            return;
    }

    document.getElementById("resultat").textContent = `Volumet er: ${volum.toFixed(2)}`;
    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for Pythagoras' setning
function pythagoras() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Pythagoras' setning</h3>
        <input type="number" id="sideA" placeholder="Side a">
        <input type="number" id="sideB" placeholder="Side b">
        <button onclick="regnUtPythagoras()">Beregn</button>
    `;
}

function regnUtPythagoras() {
    const sideA = parseFloat(document.getElementById("sideA").value);
    const sideB = parseFloat(document.getElementById("sideB").value);

    if (isNaN(sideA) || isNaN(sideB)) {
        alert("Vennligst fyll inn gyldige verdier.");
        return;
    }

    const hypotenus = Math.sqrt(sideA ** 2 + sideB ** 2);
    document.getElementById("resultat").textContent = `Hypotenusen er: ${hypotenus.toFixed(2)}`;

    const forklaringNorsk = `
        Pythagoras' setning sier at i en rettvinklet trekant er kvadratet av hypotenusen (den lengste siden) 
        lik summen av kvadratene av de to andre sidene. 
        I denne trekanten er hypotenusen √(a² + b²).
    `;

    const forklaringEngelsk = `
        Pythagoras' theorem states that in a right-angled triangle, the square of the hypotenuse (the longest side) 
        is equal to the sum of the squares of the other two sides. 
        In this triangle, the hypotenuse is √(a² + b²).
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for trigonometri
function trigonometri() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Trigonometri i rettvinklede trekanter</h3>
        <input type="number" id="vinkel" placeholder="Vinkel (i grader)">
        <input type="number" id="hypotenus" placeholder="Hypotenus">
        <button onclick="regnUtTrigonometri()">Beregn</button>
    `;
}

function regnUtTrigonometri() {
    const vinkel = parseFloat(document.getElementById("vinkel").value);
    const hypotenus = parseFloat(document.getElementById("hypotenus").value);

    if (isNaN(vinkel) || isNaN(hypotenus)) {
        alert("Vennligst fyll inn gyldige verdier.");
        return;
    }

    const radianer = (vinkel * Math.PI) / 180;
    const motstående = Math.sin(radianer) * hypotenus;
    const hosliggende = Math.cos(radianer) * hypotenus;

    document.getElementById("resultat").textContent = `Motstående side: ${motstående.toFixed(2)}, Hosliggende side: ${hosliggende.toFixed(2)}`;

    const forklaringNorsk = `
        I en rettvinklet trekant kan vi bruke trigonometri til å finne lengdene av sidene basert på vinkelen og hypotenusen. 
        Motstående side = sin(vinkel) * hypotenus. 
        Hosliggende side = cos(vinkel) * hypotenus.
    `;

    const forklaringEngelsk = `
        In a right-angled triangle, we can use trigonometry to find the lengths of the sides based on the angle and the hypotenuse. 
        Opposite side = sin(angle) * hypotenuse. 
        Adjacent side = cos(angle) * hypotenuse.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

// Funksjoner for vektorer
function vektorer() {
    const trigGeomInputDiv = document.getElementById("trigGeomInput");
    trigGeomInputDiv.innerHTML = `
        <h3>Vektorer</h3>
        <input type="number" id="vektorX" placeholder="Vektor X-komponent">
        <input type="number" id="vektorY" placeholder="Vektor Y-komponent">
        <button onclick="regnUtVektorer()">Beregn</button>
    `;
}

function regnUtVektorer() {
    const vektorX = parseFloat(document.getElementById("vektorX").value);
    const vektorY = parseFloat(document.getElementById("vektorY").value);

    if (isNaN(vektorX) || isNaN(vektorY)) {
        alert("Vennligst fyll inn gyldige verdier.");
        return;
    }

    const magnitude = Math.sqrt(vektorX ** 2 + vektorY ** 2);
    const direction = Math.atan2(vektorY, vektorX) * (180 / Math.PI);

    document.getElementById("resultat").textContent = `Lengde: ${magnitude.toFixed(2)}, Retning: ${direction.toFixed(2)} grader`;

    const forklaringNorsk = `
        En vektor har både størrelse (lengde) og retning. 
        Størrelsen av vektoren er √(x² + y²). 
        Retningen av vektoren er arctan(y/x) omgjort til grader.
    `;

    const forklaringEngelsk = `
        A vector has both magnitude (length) and direction. 
        The magnitude of the vector is √(x² + y²). 
        The direction of the vector is arctan(y/x) converted to degrees.
    `;

    document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}