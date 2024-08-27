<script>
  import { onMount } from 'svelte';
  import { Chart, registerables } from 'chart.js';
  Chart.register(...registerables);

  let temperatureData = [];
  let humidityData = [];

  onMount(async () => {
    // Hent data fra IoT-enheter (f.eks. via MQTT eller en API)
    const response = await fetch('/api/sensor_data');
    const data = await response.json();
    temperatureData = data.temperature;
    humidityData = data.humidity;

    // Opprett Chart.js-graf
    new Chart(document.getElementById('chart'), {
      type: 'line',
      data: {
        labels: [...Array(temperatureData.length).keys()], // Tidsstempler
        datasets: [{
          label: 'Temperatur',
          data: temperatureData,
          borderColor: 'rgb(255, 99, 132)',
          tension: 0.1
        }, {
          label: 'Fuktighet',
          data: humidityData,
          borderColor: 'rgb(54, 162, 235)',
          tension: 0.1
        }]
      }
    });
  });
</script>

<canvas id="chart"></canvas>