<script>
      import { onMount } from 'svelte';
      import { drawADStructure } from './adVisualization';

      let domain = {
        name: 'contoso.com',
        OUs: [{ name: 'Brukere' }, { name: 'Datamaskiner' }],
        users: [{ name: 'John Doe', OU: 'Brukere' }, { name: 'Jane Smith', OU: 'Brukere' }],
        computers: [{ name: 'PC1', OU: 'Datamaskiner' }, { name: 'PC2', OU: 'Datamaskiner' }]
      };

      onMount(() => {
        drawADStructure(document.getElementById('ad'), domain);
      });
    </script>

    <div id="ad"></div>