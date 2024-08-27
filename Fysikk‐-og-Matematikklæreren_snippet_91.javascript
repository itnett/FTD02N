document.addEventListener('DOMContentLoaded', () => {
    buildMainMenu();
});

// Function to build the main menu
function buildMainMenu() {
    const menu = document.getElementById('meny');
    menu.innerHTML = `
        <button onclick="showAlgebraMenu()">Algebra</button>
        <button onclick="showTrigGeoMenu()">Trigonometri og Geometri</button>
        <button onclick="showFunctionsMenu()">Funksjoner og Grafer</button>
        <button onclick="showPhysicsMenu()">Fysikk</button>
        <button onclick="showStudyMenu()">Studieretning</button>
    `;
}

// Function to show Algebra menu
function showAlgebraMenu() {
    buildAlgebraMenu();
}

// Function to show Trigonometry and Geometry menu
function showTrigGeoMenu() {
    buildTrigGeoMenu();
}

// Function to show Functions and Graphs menu
function showFunctionsMenu() {
    buildFunctionsMenu();
}

// Function to show Physics menu
function showPhysicsMenu() {
    buildPhysicsMenu();
}

// Function to show Study Direction menu
function showStudyMenu() {
    buildStudyMenu();
}