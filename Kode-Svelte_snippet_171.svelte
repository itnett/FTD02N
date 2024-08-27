<script>
  import { onMount } from 'svelte';
  let systemStats = {};

  onMount(async () => {
    const response = await fetch('/api/system-stats');
    systemStats = await response.json();
  });
</script>

<main>
  <h1>Systemovervåkning</h1>
  <p>CPU-bruk: {systemStats.cpu}%</p>
  <p>Minnebruk: {systemStats.memory}%</p>
</main>