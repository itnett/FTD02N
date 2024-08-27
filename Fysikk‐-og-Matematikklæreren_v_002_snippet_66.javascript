function algebraMenu() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h2>Algebra</h2>
    <button onclick="regneregler()">Regneregler</button>
    <button onclick="brøkOgProsentregning()">Brøk og Prosentregning</button>
    <button onclick="potenser()">Potenser</button>
    <button onclick="tallPåStandardform()">Tall på Standardform</button>
    <button onclick="sammentrekningOgFaktorisering()">Sammentrekning og Faktorisering</button>
    <button onclick="løsFørsteGradLikning()">Løs Likninger av Første Grad</button>
    <button onclick="løsAndreGradLikning()">Løs Likninger av Andre Grad</button>
    <button onclick="løsLikningssett()">Løs Likningssett</button>
    <button onclick="tilpasseOgOmformeFormler()">Tilpasse og Omforme Formeluttrykk</button>
  `;
}

function regneregler() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h3>Regneregler</h3>
    <input type="number" id="num1" placeholder="Tall 1">
    <select id="operator">
      <option value="+">+</option>
      <option value="-">-</option>
      <option value="*">*</option>
      <option value="/">/</option>
    </select>
    <input type="number" id="num2" placeholder="Tall 2">
    <button onclick="calculateArithmetic()">Beregn</button>
    <button class="generateCodeButton" data-topic="regneregler">Generer kode</button>
    <p id="resultat"></p>
    <p id="forklaring"></p>
  `;
}

function brøkOgProsentregning() {
  const innholdDiv = document.getElementById("content");
  innholdDiv.innerHTML = `
    <h3>Brøk og Prosentregning</h3>
    <form>
      <input type="number" id="numerator" placeholder="Teller">
      <input type="number" id="denominator" placeholder="Nevner">
      <button type="button" onclick="calculateFraction()">Beregn Brøk</button>
      <button class="generateCodeButton" data-topic="fraction">Generer kode</button>
    </form>
    <form>
      <input type="number" id="percentValue" placeholder="Prosentverdi">
      <input type="number" id="totalValue" placeholder="Totalverdi">
      <button type="button" onclick="calculatePercentage()">Beregn Prosent</button>
      <button class="generateCodeButton" data-topic="percentage">Generer kode</button>
    </form>
    <p id="resultat"></p>
    <p id="forklaring"></p>
  `;
}

function calculateFraction() {
  const numerator = parseFloat(document.getElementById('numerator').value);
  const denominator = parseFloat(document.getElementById('denominator').value);
  const result = numerator / denominator;
  document.getElementById("resultat").textContent = `Resultat: ${result}`;
  const forklaringNorsk = `En brøk er en del av en helhet. Telleren er antall deler vi har, og nevneren er totalt antall deler.`;
  const forklaringEngelsk = `A fraction represents a part of a whole. The numerator is the number of parts we have, and the denominator

 is the total number of parts.`;
  document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk;
}

function calculatePercentage() {
  const percentValue = parseFloat(document.getElementById('percentValue').value);
  const totalValue = parseFloat(document.getElementById('totalValue').value);
  const result = (percentValue / 100) * totalValue;
  document.getElementById("resultat").textContent = `Resultat: ${result}`;
  const forklaringNorsk = `Prosent regnes ut ved å dele prosentverdien på 100 og multiplisere med totalverdien.`;
  const forklaringEngelsk = `Percentage is calculated by dividing the percent value by 100 and multiplying by the total value.`;
  document.getElementById("forklaring").textContent = forklaringNorsk + "\n\n" + forklaringEngelsk.
}