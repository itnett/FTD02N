// modules/algebra_modul.js
function algebraMenu() {
  const contentDiv = document.getElementById('content');
  contentDiv.innerHTML = `
    <h3 class="text-xl font-semibold mb-2">Algebra</h3>
    <div class="grid grid-cols-3 gap-4">
      <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" onclick="regneregler()">Regneregler</button>
      <button class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded" onclick="likninger()">Likninger</button>
      <!-- Add more buttons as needed -->
    </div>
    <div id="sub-content" class="mt-4">
      <!-- Sub content will be loaded here -->
    </div>
  `;
}

function regneregler() {
  const subContentDiv = document.getElementById('sub-content');
  subContentDiv.innerHTML = `
    <h4 class="text-lg font-semibold mb-2">Regneregler</h4>
    <form class="space-y-4">
      <input type="number" id="num1" placeholder="Tall 1" class="border p-2 w-full">
      <select id="operator" class="border p-2 w-full">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select>
      <input type="number" id="num2" placeholder="Tall 2" class="border p-2 w-full">
      <div class="flex space-x-2">
        <button type="button" onclick="calculateArithmetic()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Calculate</button>
        <button type="button" class="generateCodeButton bg-gray-600 text-white py-2 px-4 rounded hover:bg-gray-700" data-topic="regneregler">Generate Code</button>
      </div>
    </form>
    <div class="mt-4">
      <p id="resultat" class="text-lg font-semibold"></p>
      <p id="forklaring" class="mt-2 text-gray-600"></p>
    </div>
  `;
}