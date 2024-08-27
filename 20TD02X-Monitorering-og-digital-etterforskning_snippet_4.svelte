<script>
      import { onMount } from 'svelte';
      import { Chart } from 'chart.js';

      let networkTrafficData = [];

      onMount(async () => {
        const response = await fetch('/api/network_traffic');
        networkTrafficData = await response.json();

        new Chart(document.getElementById('trafficChart'), {
          type: 'line',
          data: {
            labels: networkTrafficData.map(item => item.timestamp),
            datasets: [{
              label: 'Nettverkstrafikk',
              data: networkTrafficData.map(item => item.bytes)
            }]
          }
        });
      });
    </script>

    <canvas id="trafficChart"></canvas>