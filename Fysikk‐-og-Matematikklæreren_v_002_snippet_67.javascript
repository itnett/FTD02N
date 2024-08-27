function trigonometriOgGeometriMenu() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h2>Trigonometri og Geometri</h2>
    <button onclick="beregnAreal()">Beregn Areal</button>
    <button onclick="beregnOmkrets()">Beregn Omkrets</button>
    <button onclick="beregnVolum()">Beregn Volum</button>
    <button onclick="pythagoras()">Pythagoras' Setning</button>
    <button onclick="trigonometri()">Trigonometri i Rettvinklede Trekanter</button>
    <button onclick="vektorer()">Vektorer i Planet</button>
  `;
}

function beregnAreal() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h3>Beregn Areal</h3>
    <form>
      <select id="figur">
        <option value="trekant">Trekant</option>
        <option value="sirkel">Sirkel</option>
        <option value="rektangel">Rektangel</option>
      </select>
      <div id="inputFields"></div>
      <button type="button" onclick="calculateArea()">Beregn</button>
      <button class="generateCodeButton" data-topic="area">Generer kode</button>
    </form>
    <p id="resultat"></p>
    <p id="forklaring"></p>
  `;

  document.getElementById("figur").addEventListener('change', function() {
    const figur = document.getElementById("figur").value;
    let fields = '';
    if (figur === 'trekant') {
      fields = `
        <input type="number" id="base" placeholder="Grunnlinje">
        <input type="number" id="height" placeholder="Høyde">
      `;
    } else if (figur === 'sirkel') {
      fields = `<input type="number" id="radius" placeholder="Radius">`;
    } else if (figur === 'rektangel') {
      fields = `
        <input type="number" id="length" placeholder="Lengde">
        <input type="number" id="width" placeholder="Bredde">
      `;
    }
    document.getElementById("inputFields").innerHTML = fields;
  });
}

function calculateArea() {
  const figur = document.getElementById("figur").value;
  let result = 0;
  let forklaringNorsk = '';
  let forklaringEngelsk = '';

  if (figur === 'trekant') {
    const base = parseFloat(document.getElementById('base').value);
    const height = parseFloat(document.getElementById('height').value);
    result = 0.5 * base * height;
    forklaringNorsk = `Arealet av en trekant er gitt ved formelen 0,5 * grunnlinje * høyde.`;
    forklaringEngelsk = `The area of a triangle is given by the formula 0.5 * base * height.`;
  } else if (figur === 'sirkel') {
    const radius = parseFloat(document.getElementById('radius').value);
    result = Math.PI * radius * radius;
    forklaringNorsk = `Arealet av en sirkel er gitt ved formelen π * radius².`;
    forklaringEngelsk = `The area of a circle is given by the formula π * radius².`;
  } else if (figur === 'rektangel') {
    const length = parseFloat(document.getElementById('length').value);
    const width = parseFloat(document.getElementById('width').value);
    result = length * width;
    forklaringNorsk = `Arealet av et rektangel er gitt ved formelen lengde * bredde.`;
    forklaringEngelsk = `The area of a rectangle is given by the formula length * width.`;
  }

  document.getElementById("resultat").textContent = `Resultat: ${result}`;
  document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}