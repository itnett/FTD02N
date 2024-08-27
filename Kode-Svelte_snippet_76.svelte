<script>
      import { onMount } from 'svelte';
      import { drawCloudArchitecture } from './cloudVisualization';

      let architecture = {
        resources: [
          { type: 'Virtual Machine', name: 'Web Server' },
          { type: 'Load Balancer', name: 'LB' },
          { type: 'Database', name: 'SQL Database' }
        ],
        connections: [
          { from: 'Web Server', to: 'LB' },
          { from: 'LB', to: 'SQL Database' }
        ]
      };

      onMount(() => {
        drawCloudArchitecture(document.getElementById('cloud-diagram'), architecture);
      });
    </script>

    <div id="cloud-diagram"></div>