document.getElementById('mathematics-menu').addEventListener('click', function() {
  document.getElementById('content').innerHTML = `
    <h1 class="text-2xl font-bold mb-4">Mathematics Menu</h1>
    <div class="grid grid-cols-2 gap-4">
      <button onclick="showRegneregler()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Regneregler</button>
      <button onclick="showCalculateArithmetic()" class="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700">Calculate Arithmetic</button>
    </div>
  `;
});

function showRegneregler() {
  document.getElementById('content').innerHTML = `
    <h1 class="text-2xl font-bold mb-4">Regneregler</h1>
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

document.addEventListener('click', function(event) {
  if (event.target.classList.contains('generateCodeButton')) {
    const topic = event.target.dataset.topic;
    const input = getTopicInputValues(topic);
    const code = generateCodeForTrinket(topic, input);
    displayGeneratedCode(code);
  }
});

function getTopicInputValues(topic) {
  let input = {};
  switch (topic) {
    case "regneregler":
      input.tall1 = parseFloat(document.getElementById('num1').value);
      input.operator = document.getElementById('operator').value;
      input.tall2 = parseFloat(document.getElementById('num2').value);
      break;
    // Additional cases for other topics
  }
  return input;
}

function generateCodeForTrinket(topic, input) {
  let code = "";
  switch (topic) {
    case "regneregler":
      code = `
# Python code for regneregler
num1 = ${input.tall1}
num2 = ${input.tall2}
operator = '${input.operator}'

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")

if 'result' in locals():
    print(f"{num1} {operator} {num2} = {result}")
      `;
      break;
    // Additional cases for other topics
  }
  return code;
}

function displayGeneratedCode(code) {
  const resultDiv = document.getElementById('resultat');
  resultDiv.innerHTML += `
    <h3 class="text-lg font-bold mt-4">Generated code for Trinket:</h3>
    <pre class="bg-gray-200 p-4 rounded">${code}</pre>
  `;
}