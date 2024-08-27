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

  document.getElementById("figur").addEventListener("change", function() {
    const figur = this.value;
    const inputFieldsDiv = document.getElementById("inputFields");

    switch (figur) {
      case "trekant":
        inputFieldsDiv.innerHTML = `
          <input type="number" id="grunnlinje" placeholder="Grunnlinje">
          <input type="number" id="hoyde" placeholder="Høyde">
        `;
        break;
      case "sirkel":
        inputFieldsDiv.innerHTML = `
          <input type="number" id="radius" placeholder="Radius">
        `;
        break;
      case "rektangel":
        inputFieldsDiv.innerHTML = `
          <input type="number" id="lengde" placeholder="Lengde">
          <input type="number" id="bredde" placeholder="Bredde">
        `;
        break;
      default:
        inputFieldsDiv.innerHTML = "";
    }
  });
}

function calculateArea() {
  const figur = document.getElementById("figur").value;
  let area;
  let forklaringNorsk, forklaringEngelsk;

  switch (figur) {
    case "trekant":
      const grunnlinje = parseFloat(document.getElementById("grunnlinje").value);
      const hoyde = parseFloat(document.getElementById("hoyde").value);
      area = 0.5 * grunnlinje * hoyde;
      forklaringNorsk = `Arealet av en trekant er halvparten av grunnlinjen multiplisert med høyden.`;
      forklaringEngelsk = `The area of a triangle is half the base multiplied by the height.`;
      break;
    case "sirkel":
      const radius = parseFloat(document.getElementById("radius").value);
      area = Math.PI * radius * radius;
      forklaringNorsk = `Arealet av en sirkel er pi (π) multiplisert med radius kvadrert.`;
      forklaringEngelsk = `The area of a circle is pi (π) multiplied by the radius squared.`;
      break;
    case "rektangel":
      const lengde = parseFloat(document.getElementById("lengde").value);
      const bredde = parseFloat(document.getElementById("bredde").value);
      area = lengde * bredde;
      forklaringNorsk = `Arealet av et rektangel er lengden multiplisert med bredden.`;
      forklaringEngelsk = `The area of a rectangle is the length multiplied by the width.`;
      break;
    default:
      alert("Ugyldig figur.");
      return;
  }

  document.getElementById("resultat").textContent = `Arealet er: ${area.toFixed(2)}`;
  document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}