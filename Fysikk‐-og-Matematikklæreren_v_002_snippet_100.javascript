// generate_code.js
function generatePythonCode(topic, input) {
  let code = "";

  switch (topic) {
    case "regneregler":
      const num1 = input.num1;
      const operator = input.operator;
      const num2 = input.num2;
      code = `
# Python code for regneregler
num1 = ${num1}
num2 = ${num2}
operator = '${operator}'

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
    // Add more cases for other topics
  }

  return code;
}

// Handling button click for generating code
document.addEventListener('click', function(event) {
  if (event.target.classList.contains('generateCodeButton')) {
    const topic = event.target.dataset.topic;
    const input = {
      num1: document.getElementById('num1').value,
      operator: document.getElementById('operator').value,
      num2: document.getElementById('num2').value
    };
    const code = generatePythonCode(topic, input);
    displayCode(code);
  }
});

function displayCode(code) {
  const resultDiv = document.getElementById('resultat');
  resultDiv.innerHTML = `
    <h3 class="text-lg font-semibold mb-2">Generated Python Code:</h3>
    <pre class="bg-gray-800 p-4 rounded">${code}</pre>
  `;
}