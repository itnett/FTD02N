<script>
      import { onMount } from 'svelte';
      import * as d3 from 'd3';

      onMount(() => {
        // Visualiser TCP 3-veis handshake eller andre protokollflyter
        const svg = d3.select("#protocol-vis")
            .append("svg")
            .attr("width", 500)
            .attr("height", 300);

        // ... (legg til noder, kanter og animasjoner for å illustrere protokollen)
      });
    </script>

    <div id="protocol-vis"></div>