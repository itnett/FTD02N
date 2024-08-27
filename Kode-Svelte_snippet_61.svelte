<script>
      import { onMount } from 'svelte';
      import { drawContainerDiagram } from './containerVisualization';

      let containers = [
        { name: 'web', image: 'nginx', ports: ['80:80'] },
        { name: 'db', image: 'postgres', ports: ['5432:5432'] },
        // ...
      ];

      onMount(() => {
        drawContainerDiagram(document.getElementById('container-vis'), containers);
      });
    </script>

    <div id="container-vis"></div>