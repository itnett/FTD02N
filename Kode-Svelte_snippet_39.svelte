<script>
      import { onMount } from 'svelte';
      import { Chart, registerables } from 'chart.js';
      Chart.register(...registerables);

      let salesData = [];

      onMount(async () => {
        const response = await fetch('/api/sales_data');
        salesData = await response.json();

        new Chart(document.getElementById('salesChart'), {
          type: 'bar',
          data: {
            labels: salesData.map(item => item.month),
            datasets: [{
              label: 'Salg',
              data: salesData.map(item => item.amount)
            }]
          }
        });
      });
    </script>

    <canvas id="salesChart"></canvas>