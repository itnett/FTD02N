<script>
      import { onMount } from 'svelte';

      let networkStats = [];

      onMount(async () => {
        const response = await fetch('/api/network_stats');
        networkStats = await response.json();
      });
    </script>

    <h2>Nettverksovervåkning</h2>
    <ul>
      {#each networkStats as stat}
        <li>{stat.interface}: {stat.bandwidth} Mbps</li>
      {/each}
    </ul>