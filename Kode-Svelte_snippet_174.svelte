<script>
  import { onMount } from 'svelte';
  let serverData = {};

  onMount(async () => {
    const response = await fetch('/api/windows-server');
    serverData = await response.json();
  });
</script>

<main>
  <h1>Windows Server Monitor</h1>
  <p>CPU-bruk: {serverData.cpu}%</p>
  <p>Minnebruk: {serverData.memory}%</p>
</main>