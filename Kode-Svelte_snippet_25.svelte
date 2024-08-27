<script>
      import { onMount } from 'svelte';
      import { drawAttackGraph } from './attackGraph';

      onMount(() => {
        drawAttackGraph(document.getElementById('attackGraph'));
      });
    </script>

    <div id="attackGraph"></div>