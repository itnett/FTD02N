function generateCodeForTrinket(topic, input) {
  let code = "";

  switch (topic) {
    case "regneregler":
      const tall1 = input.tall1;
      const operator = input.operator;
      const tall2 = input.tall2;
      code = `
# Python kode for regneregler
tall1 = ${tall1}
tall2 = ${tall2}
operator = '${operator}'

if operator == '+':
    resultat = tall1 + tall2
elif operator == '-':
    resultat = tall1 - tall2
elif operator == '*':
    resultat = tall1 * tall2
elif operator == '/':
    if tall2 != 0:
        resultat = tall1 / tall2
    else:
        print("Kan ikke dele med null.")
else:
    print("Ugyldig operator.")

if 'resultat' in locals():
    print(f"{tall1} {operator} {tall2} = {resultat}")
`;
      break;
    // Additional cases for other topics
  }

  return code;
}

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

document.addEventListener('click', function(event) {
  if (event.target.classList.contains('generateCodeButton')) {
    const topic = event.target.dataset.topic;
    const input = getTopicInputValues(topic);
    const code = generateCodeForTrinket(topic, input);
    displayGeneratedCode(code);
  }
});

function displayGeneratedCode(code) {
  const resultDiv = document.getElementById('resultat');
  resultDiv.innerHTML += `
    <h3>Generert kode for Trinket:</h3>
    <pre>${code}</pre>
  `;
}