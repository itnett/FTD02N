// script.js
document.getElementById('mathematics-menu').addEventListener('click', loadMathematicsMenu);
document.getElementById('physics-menu').addEventListener('click', loadPhysicsMenu);
document.getElementById('special-topics-menu').addEventListener('click', loadSpecialTopicsMenu);

function loadMathematicsMenu() {
  document.getElementById('content').innerHTML = `
    <h2 class="text-2xl font-bold mb-4">Mathematics</h2>
    <div class="grid grid-cols-3 gap-4">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="algebraMenu()">Algebra</button>
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="trigonometryMenu()">Trigonometry & Geometry</button>
      <!-- Add more buttons as needed -->
    </div>
  `;
}

function loadPhysicsMenu() {
  document.getElementById('content').innerHTML = `
    <h2 class="text-2xl font-bold mb-4">Physics</h2>
    <div class="grid grid-cols-3 gap-4">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="introductoryPhysicsMenu()">Introductory Physics</button>
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="advancedPhysicsMenu()">Advanced Physics</button>
      <!-- Add more buttons as needed -->
    </div>
  `;
}

function loadSpecialTopicsMenu() {
  document.getElementById('content').innerHTML = `
    <h2 class="text-2xl font-bold mb-4">Special Topics</h2>
    <div class="grid grid-cols-3 gap-4">
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="combinatoricsMenu()">Combinatorics</button>
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onclick="statisticsMenu()">Statistics</button>
      <!-- Add more buttons as needed -->
    </div>
  `;
}