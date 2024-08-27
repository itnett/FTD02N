<script>
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';

  let salesData = [10, 20, 30, 40, 50];

  onMount(() => {
    new Chart(document.getElementById('salesChart'), {
      type: 'line',
      data: {
        labels: ['Januar', 'Februar', 'Mars', 'April', 'Mai'],
        datasets: [{
          label: 'Salg',
          data: salesData,
        }]
      }
    });
  });
</script>

<main>
  <h1>Økonomisk dashboard</h1>
  <canvas id="salesChart"></canvas>
</main>