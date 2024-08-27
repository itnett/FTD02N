<script>
  import { onMount } from 'svelte';

  let serverInfo = {};

  onMount(async () => {
    const response = await fetch('/api/server_info');
    serverInfo = await response.json();
  });
</script>

<h2>ServerInfo</h2>
<p>Navn: {serverInfo.name}</p>
<p>Operativsystem: {serverInfo.os}</p>
<p>CPU: {serverInfo.cpu}</p>
<p>Minne: {serverInfo.memory}</p>