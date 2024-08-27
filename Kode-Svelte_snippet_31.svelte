<script>
      import { onMount } from 'svelte';
      import { simulateNetworkTraffic } from './networkSimulation';

      onMount(() => {
        simulateNetworkTraffic(document.getElementById('simulation'));
      });
    </script>

    <div id="simulation"></div>