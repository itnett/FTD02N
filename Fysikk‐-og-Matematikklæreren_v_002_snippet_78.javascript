function algebraMenu() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h2 class="text-2xl font-bold mb-4">Algebra</h2>
    <div class="grid grid-cols-2 gap-4">
      <button onclick="regneregler()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Regneregler</button>
      <button onclick="brøkOgProsentregning()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Brøk og Prosentregning</button>
      <button onclick="potenser()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Potenser</button>
      <button onclick="tallPåStandardform()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Tall

 på Standardform</button>
    </div>
  `;
}

function regneregler() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h3 class="text-xl font-semibold mb-2">Regneregler</h3>
    <form class="space-y-4">
      <div>
        <input type="number" id="num1" placeholder="Tall 1" class="border p-2 w-full">
      </div>
      <div>
        <select id="operator" class="border p-2 w-full">
          <option value="+">+</option>
          <option value="-">-</option>
          <option value="*">*</option>
          <option value="/">/</option>
        </select>
      </div>
      <div>
        <input type="number" id="num2" placeholder="Tall 2" class="border p-2 w-full">
      </div>
      <div class="flex space-x-2">
        <button type="button" onclick="calculateArithmetic()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Calculate</button>
        <button class="generateCodeButton" data-topic="regneregler">Generate Code</button>
      </div>
    </form>
    <div class="mt-4">
      <p id="resultat" class="text-lg font-semibold"></p>
      <p id="forklaring" class="mt-2 text-gray-600"></p>
    </div>
  `;
}