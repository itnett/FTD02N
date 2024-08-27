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
      <input type="number" id="num1" placeholder="Tall 1">
      <select id="operator">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select>
      <input type="number" id="num2" placeholder="Tall 2">
      <button type="button" onclick="calculateArithmetic()">Calculate</button>
      <button class="generateCodeButton" data-topic="regneregler">Generate Code</button>
    </form>
    <p id="resultat"></p>
    <p id="forklaring"></p>
  `;
}

function calculateArithmetic() {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const operator = document.getElementById('operator').value;

  let result;
  switch (operator) {
    case "+":
      result = num1 + num2;
      break;
    case "-":
      result = num1 - num2;
      break;
    case "*":
      result = num1 * num2;
      break;
    case "/":
      if (num2 !== 0) {
        result = num1 / num2;
      } else {
        alert("Kan ikke dele med null.");
        return;
      }
      break;
    default:
      alert("Ugyldig operator.");
      return;
  }

  document.getElementById("resultat").textContent = `${num1} ${operator} ${num2} = ${result}`;
  const forklaringNorsk = `Dette er en enkel regneoperasjon. Operatoren "${operator}" angir hvilken regneoperasjon som skal utføres.`;
  const forklaringEngelsk = `This is a simple arithmetic operation. The operator "${operator}" indicates which operation to perform.`;
  document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}