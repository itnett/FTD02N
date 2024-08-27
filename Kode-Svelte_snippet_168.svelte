<script>
  import { onMount } from 'svelte';
  let logs = [];

  onMount(async () => {
    const response = await fetch('/api/logs');
    logs = await response.json();
  });
</script>

<main>
  <h1>Sikkerhetslogger</h1>
  <ul>
    {#each logs as log}
      <li>{log.timestamp}: {log.message}</li>
    {/each}
  </ul>
</main>