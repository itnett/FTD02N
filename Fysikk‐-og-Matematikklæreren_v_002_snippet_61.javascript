document.getElementById('mathematics-menu').addEventListener('click', function() {
  document.getElementById('content').innerHTML = `
    <h1>Mathematics Menu</h1>
    <ul>
      <li><a href="#" onclick="showRegneregler()">Regneregler</a></li>
      <li><a href="#" onclick="showCalculateArithmetic()">Calculate Arithmetic</a></li>
    </ul>
  `;
});

function showRegneregler() {
  document.getElementById('content').innerHTML = `
    <h1>Regneregler</h1>
    <form>
      <input type="text" placeholder="Enter value" />
      <button type="submit">Calculate</button>
    </form>
  `;
}

function showCalculateArithmetic() {
  document.getElementById('content').innerHTML = `
    <h1>Calculate Arithmetic</h1>
    <form>
      <input type="text" placeholder="Enter value" />
      <button type="submit">Calculate</button>
    </form>
  `;
}