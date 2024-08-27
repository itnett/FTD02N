<script>
  import { onMount } from 'svelte';
  let servers = [];

  onMount(async () => {
    const response = await fetch('/api/servers');
    servers = await response.json();
  });
</script>

<main>
  <h1>Serverstatus</h1>
  <ul>
    {#each servers as server}
      <li>{server.name}: {server.status}</li>
    {/each}
  </ul>
</main>