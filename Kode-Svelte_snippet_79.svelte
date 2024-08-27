<script>
      import { onMount } from 'svelte';
      import { renderInfrastructureDiagram } from './iacVisualization';

      let iacCode = '';

      onMount(() => {
        renderInfrastructureDiagram(document.getElementById('iac-diagram'), iacCode);
      });
    </script>

    <textarea bind:value={iacCode}></textarea>
    <div id="iac-diagram"></div>