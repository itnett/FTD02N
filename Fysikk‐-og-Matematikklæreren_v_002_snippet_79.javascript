function trigonometriOgGeometriMenu() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h2 class="text-2xl font-bold mb-4">Trigonometri og Geometri</h2>
    <div class="grid grid-cols-2 gap-4">
      <button onclick="beregnAreal()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Beregn Areal</button>
      <button onclick="beregnOmkrets()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Beregn Omkrets</button>
      <button onclick="beregnVolum()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Beregn Volum</button>
      <button onclick="pythagoras()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Pythagoras' Setning</button>
      <button onclick="trigonometri()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Trigonometri i Rettvinklede Trekanter</button>
      <button onclick="vektorer()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Vektorer i Planet</button>
    </div>
  `;
}

function beregnAreal() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h3 class="text-xl font-semibold mb-2">Beregn Areal</h3>
    <form class="space-y-4">
      <select id="figur" class="border p-2 w-full">
        <option value="trekant">Trekant</option>
        <option value="sirkel">Sirkel</option>
        <option value="rektangel">Rektangel</option>
      </select>
      <div id="inputFields"></div>
      <div class="flex space-x-2">
        <button type="button" onclick="calculateArea()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Beregn</button>
        <button class="generateCodeButton" data-topic="area">Generate Code</button>
      </div>
    </form>
    <div class="mt-4">
      <p id="resultat" class="text-lg font-semibold"></p>
      <p id="forklaring" class="mt-2 text-gray-600"></p>
    </div>
  `;

  document.getElementById("figur").addEventListener("change", function() {
    const figur = this.value;
    const inputFieldsDiv = document.getElementById("inputFields");

    switch (figur) {
      case "trekant":
        inputFieldsDiv.innerHTML = `
          <input type="number" id="grunnlinje" placeholder="Grunnlinje" class="border p-2 w-full">
          <input type="number" id="hoyde" placeholder="Høyde" class="border p-2 w-full">
        `;
        break;
      case "sirkel":
        inputFieldsDiv.innerHTML = `
          <input type="number" id="radius" placeholder="Radius" class="border p-2 w-full">
        `;
        break;
      case "rektangel":
        inputFieldsDiv.innerHTML = `
          <input type="number" id="lengde" placeholder="Lengde" class="border p-2 w-full">
          <input type="number" id="bredde" placeholder="Bredde" class="border p-2 w-full">
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