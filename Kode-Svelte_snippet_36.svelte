<script>
      import { onMount } from 'svelte';
      import { drawERD } from './erdVisualization';

      let entities = [
        { name: 'Kunde', attributes: ['kunde_id', 'navn', 'epost'] },
        { name: 'Ordre', attributes: ['ordre_id', 'kunde_id', 'dato'] }
      ];

      let relationships = [
        { from: 'Kunde', to: 'Ordre', type: '1-N' } 
      ];

      onMount(() => {
        drawERD(document.getElementById('erd'), entities, relationships);
      });
    </script>

    <div id="erd"></div>