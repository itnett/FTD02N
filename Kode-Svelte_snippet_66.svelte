<script>
      import { onMount } from 'svelte';
      import { Chart, registerables } from 'chart.js';
      Chart.register(...registerables);

      let networkTrafficData = [];
      let securityEventsData = [];

      onMount(async () => {
        // Hent data fra overvåkningssystemer
        const response = await fetch('/api/monitoring_data');
        const data = await response.json();
        networkTrafficData = data.networkTraffic;
        securityEventsData = data.securityEvents;

        // Opprett diagrammer
        new Chart(document.getElementById('networkTrafficChart'), {
          type: 'line',
          data: {
            labels: [...Array(networkTrafficData.length).keys()], // Tidsstempler
            datasets: [{
              label: 'Nettverkstrafikk',
              data: networkTrafficData
            }]
          }
        });

        new Chart(document.getElementById('securityEventsChart'), {
          type: 'bar',
          data: {
            labels: ['Innlogginger', 'Feil', 'Intrusjoner'],
            datasets: [{
              label: 'Sikkerhetshendelser',
              data: securityEventsData
            }]
          }
        });
      });
    </script>

    <div>
      <canvas id="networkTrafficChart"></canvas>
      <canvas id="securityEventsChart"></canvas>
    </div>