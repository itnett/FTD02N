<script>
  import { onMount } from 'svelte';

  let cpuUsage = 0;
  let memoryUsage = 0;

  onMount(async () => {
    const response = await fetch('/api/server_status');
    const data = await response.json();
    cpuUsage = data.cpuUsage;
    memoryUsage = data.memoryUsage;
  });
</script>

<h2>Serverstatus</h2>
<p>CPU-bruk: {cpuUsage}%</p>
<p>Minnebruk: {memoryUsage}%</p>