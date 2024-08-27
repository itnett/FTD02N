// chart example in a module
function renderExampleChart() {
  const subContentDiv = document.getElementById('sub-content');
  subContentDiv.innerHTML = `
    <div class="card">
      <canvas id="exampleChart" width="400" height="200"></canvas>
    </div>
  `;

  const ctx = document.getElementById('exampleChart').getContext('2d');
  const exampleChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',