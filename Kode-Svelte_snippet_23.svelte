<script>
  import { onMount } from 'svelte';
  import vis from 'vis-network';

  let nodes = [];
  let edges = [];

  onMount(async () => {
    const response = await fetch('/api/network_topology');
    const data = await response.json();
    nodes = data.nodes;
    edges = data.edges;

    new vis.Network(document.getElementById('network'), { nodes, edges }, {});
  });
</script>

<div id="network"></div>