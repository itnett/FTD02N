<script>
      import { onMount } from 'svelte';
      import { simulateSecurityIncident } from './incidentSimulation';

      onMount(() => {
        simulateSecurityIncident(document.getElementById('incident-sim'));
      });
    </script>

    <div id="incident-sim"></div>