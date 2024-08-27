<script>
      import { onMount } from 'svelte';

      let serverData = {};

      onMount(async () => {
        const response = await fetch('/api/server_data');
        serverData = await response.json();
      });
    </script>

    <h2>Serverstatus</h2>
    <p>CPU-bruk: {serverData.cpuUsage}%</p>
    <p>Minnebruk: {serverData.memoryUsage}%</p>
    <p>Diskbruk: {serverData.diskUsage}%</p>