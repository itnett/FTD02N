<script>
      import { onMount } from 'svelte';
      import { Chart } from 'chart.js';

      let firewallLogs = [];
      let intrusionAttempts = 0;

      onMount(async () => {
        // Hent data fra brannmurlogger og IDS/IPS
        const response = await fetch('/api/security_logs');
        firewallLogs = await response.json();
        intrusionAttempts = firewallLogs.filter(log => log.type === 'intrusion').length;

        // Opprett diagram for å visualisere trusler over tid
        new Chart(document.getElementById('threatChart'), {
          type: 'line',
          data: {
            // ... (data for trusseldiagram)
          }
        });
      });
    </script>

    <h2>Nettverkssikkerhet</h2>
    <p>Intrusjonsforsøk: {intrusionAttempts}</p>
    <canvas id="threatChart"></canvas>