<script>
      import { onMount } from 'svelte';

      let databaseStatus = [];

      onMount(async () => {
        const response = await fetch('/api/database_status');
        databaseStatus = await response.json();
      });
    </script>

    <h2>Database Status</h2>
    <ul>
      {#each databaseStatus as status}
        <li>{status.name}: {status.status}</li>
      {/each}
    </ul>