<script>
      let vms = [];

      async function getVMs() {
        const response = await fetch('/api/vms');
        vms = await response.json();
      }
    </script>

    <button on:click={getVMs}>Hent virtuelle maskiner</button>
    <ul>
      {#each vms as vm}
        <li>{vm.name} - {vm.status}</li>
      {/each}
    </ul>