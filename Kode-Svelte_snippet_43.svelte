<script>
      import { onMount } from 'svelte';
      import { simulateAttack } from './attackSimulation';

      onMount(() => {
        simulateAttack('xss', document.getElementById('attack-sim'));
      });
    </script>

    <div id="attack-sim"></div>