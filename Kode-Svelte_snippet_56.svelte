<script>
      import { onMount } from 'svelte';

      let serverStatus = [];

      onMount(async () => {
        const response = await fetch('/api/server_status');
        serverStatus = await response.json();
      });
    </script>

    <h2>Windows Server Status</h2>
    <ul>
      {#each serverStatus as status}
        <li>{status.name}: {status.status}</li>
      {/each}
    </ul>