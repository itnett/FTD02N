<script>
  import { onMount } from 'svelte';
  import { Network } from 'vis-network/standalone';

  let nodes = [
    { id: 1, label: 'Router' },
    { id: 2, label: 'Switch' },
    { id: 3, label: 'PC1' },
    { id: 4, label: 'PC2' }
  ];

  let edges = [
    { from: 1, to: 2 },
    { from: 2, to: 3 },
    { from: 2, to: 4 }
  ];

  onMount(() => {
    new Network(document.getElementById('network'), { nodes, edges }, {});
  });
</script>

<div id="network" style="height: 400px;"></div>