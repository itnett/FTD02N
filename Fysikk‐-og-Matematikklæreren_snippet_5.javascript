document.addEventListener('DOMContentLoaded', () => {
    buildMainMenu();
});

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

function showAlgebraMenu() {
    // Load algebra menu
    buildAlgebraMenu();
}

function showTrigGeoMenu() {
    // Load trigonometry and geometry menu
    buildTrigGeoMenu();
}

function showFunctionsMenu() {
    // Load functions and graphs menu
    buildFunctionsMenu();
}

function showPhysicsMenu() {
    // Load physics menu
    buildPhysicsMenu();
}

function showStudyMenu() {
    // Load study direction menu
    buildStudyMenu();
}