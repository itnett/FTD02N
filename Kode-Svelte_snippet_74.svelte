<script>
      import { onMount } from 'svelte';
      import { drawSVS } from './svsVisualization';

      onMount(() => {
        drawSVS(document.getElementById('svs'));
      });
    </script>

    <div id="svs"></div>