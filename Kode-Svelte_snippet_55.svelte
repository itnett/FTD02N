<script>
      import { onMount } from 'svelte';
      import { simulateVM } from './vmSimulation';

      onMount(() => {
        simulateVM(document.getElementById('vm-sim'), {
          os: 'Windows Server 2022',
          cpu: 4,
          memory: 8192,
          disk: 50
        });
      });
    </script>

    <div id="vm-sim"></div>