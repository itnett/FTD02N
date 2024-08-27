// Bygg menyen for studieretning
// Build the menu for study direction
function buildStudyMenu() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Studieretning</h2>
        <button onclick="introduksjon()">Introduksjon</button>
        <button onclick="teknologi()">Teknologi</button>
        <button onclick="okonomi()">Økonomi</button>
        <button onclick="biologi()">Biologi</button>
        <button onclick="samfunnsfag()">Samfunnsfag</button>
    `;
}

// Introduksjon til studieretning
// Introduction to study direction
function introduksjon() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Introduksjon</h2>
        <p>
            Studieretning omfatter ulike fagområder som forbereder studenter på spesifikke yrker og akademiske veier. 
            Denne modulen gir en oversikt over de viktigste studieretningene og deres kjerneinnhold.
        </p>
        <p>
            The study direction encompasses various fields of study that prepare students for specific careers and academic paths.
            This module provides an overview of the main study directions and their core content.
        </p>
    `;
}

// Teknologistudier
// Technology studies
function teknologi() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Teknologi</h2>
        <p>
            Teknologistudier dekker områder som informatikk, ingeniørfag, og informasjonsteknologi. Studenter lærer om 
            programmering, systemdesign, og utvikling av teknologiske løsninger.
        </p>
        <p>
            Technology studies cover areas such as computer science, engineering, and information technology. Students learn 
            about programming, system design, and the development of technological solutions.
        </p>
        <label for="techField">Velg felt:</label>
        <select id="techField">
            <option value="informatikk">Informatikk</option>
            <option value="elektro">Elektroingeniør</option>
            <option value="mekanisk">Mekanisk ingeniør</option>
        </select>
        <button onclick="visTeknologiDetaljer()">Vis detaljer</button>
        <div id="techDetails"></div>
    `;

    document.getElementById('techField').addEventListener('change', visTeknologiDetaljer);
}

// Vis detaljer om valgt teknologifelt
// Display details about the selected technology field
function visTeknologiDetaljer() {
    const techField = document.getElementById('techField').value;
    const techDetails = document.getElementById('techDetails');

    if (techField === 'informatikk') {
        techDetails.innerHTML = `
            <h3>Informatikk</h3>
            <p>Informatikk omhandler studiet av algoritmer, datastrukturer, og programvareutvikling. 
               Studenter lærer programmering og systemdesign.</p>
            <p>Computer science involves the study of algorithms, data structures, and software development. 
               Students learn programming and system design.</p>
        `;
    } else if (techField === 'elektro') {
        techDetails.innerHTML = `
            <h3>Elektroingeniør</h3>
            <p>Elektroingeniør dekker studiet av elektriske systemer, kretsdesign, og signalbehandling. 
               Studenter lærer om kraftsystemer og elektronikk.</p>
            <p>Electrical engineering covers the study of electrical systems, circuit design, and signal processing. 
               Students learn about power systems and electronics.</p>
        `;
    } else if (techField === 'mekanisk') {
        techDetails.innerHTML = `
            <h3>Mekanisk ingeniør</h3>
            <p>Mekanisk ingeniør inkluderer studiet av mekaniske systemer, materialvitenskap, og termodynamikk. 
               Studenter lærer om maskindesign og produksjonsteknikker.</p>
            <p>Mechanical engineering includes the study of mechanical systems, materials science, and thermodynamics. 
               Students learn about machine design and manufacturing techniques.</p>
        `;
    }
}

// Økonomistudier
// Economics studies
function okonomi() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Økonomi</h2>
        <p>
            Økonomistudier fokuserer på forståelse av økonomiske systemer, finans, og markedsteori. 
            Studenter lærer om regnskap, bedriftsøkonomi, og makroøkonomi.
        </p>
        <p>
            Economics studies focus on understanding economic systems, finance, and market theory. 
            Students learn about accounting, business economics, and macroeconomics.
        </p>
    `;
}

// Biologistudier
// Biology studies
function biologi() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Biologi</h2>
        <p>
            Biologistudier dekker livsvitenskapene, inkludert studier av celler, organismer, og økosystemer. 
            Studenter lærer om genetikk, evolusjon, og biokjemi.
        </p>
        <p>
            Biology studies cover the life sciences, including the study of cells, organisms, and ecosystems. 
            Students learn about genetics, evolution, and biochemistry.
        </p>
    `;
}

// Samfunnsfagstudier
// Social studies
function samfunnsfag() {
    const content = document.getElementById('innhold');
    content.innerHTML = `
        <h2>Samfunnsfag</h2>
        <p>
            Samfunnsfagstudier omfatter emner som sosiologi, psykologi, og politiske vitenskaper. 
            Studenter lærer om samfunnsstrukturer, menneskelig atferd, og politiske systemer.
        </p>
        <p>
            Social studies encompass subjects such as sociology, psychology, and political sciences. 
            Students learn about social structures, human behavior, and political systems.
        </p>
    `;
}